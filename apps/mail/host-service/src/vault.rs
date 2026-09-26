//! Where the mail service keeps passwords: the platform's own secret store.
//!
//! - macOS and iOS: the keychain, one item per account.
//! - Android: a file per account under the service's directory, encrypted
//!   with an AES key that lives in the Android Keystore and never leaves it.
//! - Elsewhere: an owner-only file under the service's directory.
//!
//! A password kept as a plain file by an earlier build is moved into the
//! store the first time it is read.
use std::path::{Path, PathBuf};

pub trait Vault: Send + Sync {
    /// `dir` is the service's own directory; `id` the account.
    fn put(&self, dir: &Path, id: &str, secret: &str) -> Result<(), String>;
    fn get(&self, dir: &Path, id: &str) -> Result<String, String>;
    fn remove(&self, dir: &Path, id: &str);
}

fn missing() -> String {
    "The account's password is missing; sign in again.".into()
}

fn secret_path(dir: &Path, id: &str) -> PathBuf {
    dir.join("secrets").join(id)
}

fn write_private(path: &Path, bytes: &[u8]) -> Result<(), String> {
    if let Some(parent) = path.parent() {
        std::fs::create_dir_all(parent).map_err(|e| format!("Cannot store the password: {e}"))?;
    }
    let temp = path.with_extension("tmp");
    #[cfg(unix)]
    {
        use std::io::Write;
        use std::os::unix::fs::OpenOptionsExt;
        let mut file = std::fs::OpenOptions::new()
            .write(true)
            .create(true)
            .truncate(true)
            .mode(0o600)
            .open(&temp)
            .map_err(|e| format!("Cannot store the password: {e}"))?;
        file.write_all(bytes).map_err(|e| format!("Cannot store the password: {e}"))?;
    }
    #[cfg(not(unix))]
    std::fs::write(&temp, bytes).map_err(|e| format!("Cannot store the password: {e}"))?;
    std::fs::rename(&temp, path).map_err(|e| format!("Cannot store the password: {e}"))
}

/// An owner-only file per account.
pub struct FileVault;

impl Vault for FileVault {
    fn put(&self, dir: &Path, id: &str, secret: &str) -> Result<(), String> {
        write_private(&secret_path(dir, id), secret.as_bytes())
    }
    fn get(&self, dir: &Path, id: &str) -> Result<String, String> {
        std::fs::read_to_string(secret_path(dir, id)).map_err(|_| missing())
    }
    fn remove(&self, dir: &Path, id: &str) {
        let _ = std::fs::remove_file(secret_path(dir, id));
    }
}

/// A plain file left by an earlier build, if any: read, and moved into
/// `vault` on success.
fn migrate(vault: &dyn Vault, dir: &Path, id: &str) -> Option<String> {
    let secret = std::fs::read_to_string(secret_path(dir, id)).ok()?;
    if vault.put(dir, id, &secret).is_ok() {
        // Android's vault rewrites the same file; elsewhere it goes.
        if std::fs::read_to_string(secret_path(dir, id)).ok().as_deref() == Some(secret.as_str()) {
            let _ = std::fs::remove_file(secret_path(dir, id));
        }
    }
    Some(secret)
}

/// The store for this platform. `OCTOSENSE_MAIL_VAULT=file` picks the file
/// store instead: macOS asks the person again for every rebuilt, unsigned
/// development binary that reads a keychain item.
pub fn platform() -> std::sync::Arc<dyn Vault> {
    if std::env::var("OCTOSENSE_MAIL_VAULT").is_ok_and(|v| v == "file") {
        return std::sync::Arc::new(FileVault);
    }
    #[cfg(any(target_os = "macos", target_os = "ios"))]
    return std::sync::Arc::new(keychain::Keychain);
    #[cfg(target_os = "android")]
    return std::sync::Arc::new(android::Keystore);
    #[allow(unreachable_code)]
    std::sync::Arc::new(FileVault)
}

#[cfg(any(target_os = "macos", target_os = "ios"))]
pub mod keychain {
    use super::*;

    /// One keychain item per account. The item's service names the host
    /// directory too, so two profiles on one machine keep separate items.
    pub struct Keychain;

    fn entry(dir: &Path, id: &str) -> Result<keyring::Entry, String> {
        let dir = std::fs::canonicalize(dir).unwrap_or_else(|_| dir.to_path_buf());
        let profile = crate::network::hash(&dir.to_string_lossy());
        keyring::Entry::new(&format!("OctoSense Mail {}", &profile[..12]), id).map_err(|e| format!("The keychain is unavailable: {e}"))
    }

    impl Vault for Keychain {
        fn put(&self, dir: &Path, id: &str, secret: &str) -> Result<(), String> {
            entry(dir, id)?.set_password(secret).map_err(|e| format!("Cannot store the password in the keychain: {e}"))
        }
        fn get(&self, dir: &Path, id: &str) -> Result<String, String> {
            match entry(dir, id)?.get_password() {
                Ok(secret) => Ok(secret),
                Err(keyring::Error::NoEntry) => migrate(self, dir, id).ok_or_else(missing),
                Err(e) => Err(format!("Cannot read the password from the keychain: {e}")),
            }
        }
        fn remove(&self, dir: &Path, id: &str) {
            if let Ok(entry) = entry(dir, id) {
                let _ = entry.delete_credential();
            }
            let _ = std::fs::remove_file(secret_path(dir, id));
        }
    }
}

#[cfg(target_os = "android")]
mod android {
    //! AES-256-GCM with a key generated inside the Android Keystore under
    //! [`ALIAS`]. The key cannot be exported: a copy of the files decrypts
    //! nothing off this device or outside this app.
    use super::*;
    use makepad_jni_sys as jni;
    use std::ffi::CString;
    use std::ptr::null_mut;

    const ALIAS: &str = "octosense.mail.v1";
    /// What an encrypted file starts with; a file without it is an older
    /// plain one.
    const MAGIC: &[u8] = b"OSK1";

    pub struct Keystore;

    impl Vault for Keystore {
        fn put(&self, dir: &Path, id: &str, secret: &str) -> Result<(), String> {
            let (iv, sealed) = unsafe { with_env(|env| crypt(env, true, &[], secret.as_bytes())) }?;
            let mut bytes = MAGIC.to_vec();
            bytes.push(iv.len() as u8);
            bytes.extend_from_slice(&iv);
            bytes.extend_from_slice(&sealed);
            write_private(&secret_path(dir, id), &bytes)
        }
        fn get(&self, dir: &Path, id: &str) -> Result<String, String> {
            let bytes = std::fs::read(secret_path(dir, id)).map_err(|_| missing())?;
            let Some(rest) = bytes.strip_prefix(MAGIC) else {
                return migrate(self, dir, id).ok_or_else(missing);
            };
            let iv_len = *rest.first().ok_or_else(missing)? as usize;
            let iv = rest.get(1..1 + iv_len).ok_or_else(missing)?;
            let sealed = &rest[1 + iv_len..];
            let (_, plain) = unsafe { with_env(|env| crypt(env, false, iv, sealed)) }?;
            String::from_utf8(plain).map_err(|_| missing())
        }
        fn remove(&self, dir: &Path, id: &str) {
            let _ = std::fs::remove_file(secret_path(dir, id));
        }
    }

    /// This thread's JNI environment, attached for the call if it was not.
    unsafe fn with_env<T>(f: impl FnOnce(*mut jni::JNIEnv) -> Result<T, String>) -> Result<T, String> {
        let vm = makepad_android_state::get_java_vm();
        if vm.is_null() {
            return Err("The Android keystore is unavailable.".into());
        }
        let mut env: *mut std::ffi::c_void = null_mut();
        let attached_here = ((**vm).GetEnv.unwrap())(vm, &mut env, jni::JNI_VERSION_1_6) != 0;
        if attached_here {
            let mut fresh: *mut jni::JNIEnv = null_mut();
            if ((**vm).AttachCurrentThread.unwrap())(vm, &mut fresh, null_mut()) != 0 {
                return Err("The Android keystore is unavailable.".into());
            }
            env = fresh as _;
        }
        let env = env as *mut jni::JNIEnv;
        ((**env).PushLocalFrame.unwrap())(env, 64);
        let result = f(env);
        ((**env).PopLocalFrame.unwrap())(env, null_mut());
        if attached_here {
            ((**vm).DetachCurrentThread.unwrap())(vm);
        }
        result
    }

    fn c(s: &str) -> CString {
        CString::new(s).unwrap()
    }

    unsafe fn check(env: *mut jni::JNIEnv, what: &str) -> Result<(), String> {
        if ((**env).ExceptionCheck.unwrap())(env) != 0 {
            ((**env).ExceptionClear.unwrap())(env);
            return Err(format!("The Android keystore failed ({what})."));
        }
        Ok(())
    }

    unsafe fn class(env: *mut jni::JNIEnv, name: &str) -> Result<jni::jclass, String> {
        let class = ((**env).FindClass.unwrap())(env, c(name).as_ptr());
        check(env, name)?;
        Ok(class)
    }

    unsafe fn method(env: *mut jni::JNIEnv, class: jni::jclass, name: &str, sig: &str) -> Result<jni::jmethodID, String> {
        let id = ((**env).GetMethodID.unwrap())(env, class, c(name).as_ptr(), c(sig).as_ptr());
        check(env, name)?;
        Ok(id)
    }

    unsafe fn static_method(env: *mut jni::JNIEnv, class: jni::jclass, name: &str, sig: &str) -> Result<jni::jmethodID, String> {
        let id = ((**env).GetStaticMethodID.unwrap())(env, class, c(name).as_ptr(), c(sig).as_ptr());
        check(env, name)?;
        Ok(id)
    }

    unsafe fn string(env: *mut jni::JNIEnv, s: &str) -> jni::jobject {
        ((**env).NewStringUTF.unwrap())(env, c(s).as_ptr())
    }

    unsafe fn string_array(env: *mut jni::JNIEnv, items: &[&str]) -> Result<jni::jobject, String> {
        let string_class = class(env, "java/lang/String")?;
        let array = ((**env).NewObjectArray.unwrap())(env, items.len() as i32, string_class, null_mut());
        for (i, item) in items.iter().enumerate() {
            ((**env).SetObjectArrayElement.unwrap())(env, array, i as i32, string(env, item));
        }
        Ok(array)
    }

    unsafe fn bytes_in(env: *mut jni::JNIEnv, bytes: &[u8]) -> jni::jobject {
        let array = ((**env).NewByteArray.unwrap())(env, bytes.len() as i32);
        ((**env).SetByteArrayRegion.unwrap())(env, array, 0, bytes.len() as i32, bytes.as_ptr() as *const i8);
        array
    }

    unsafe fn bytes_out(env: *mut jni::JNIEnv, array: jni::jobject) -> Vec<u8> {
        if array.is_null() {
            return Vec::new();
        }
        let len = ((**env).GetArrayLength.unwrap())(env, array) as usize;
        let mut out = vec![0u8; len];
        ((**env).GetByteArrayRegion.unwrap())(env, array, 0, len as i32, out.as_mut_ptr() as *mut i8);
        out
    }

    /// The key under [`ALIAS`], made on first use.
    unsafe fn key(env: *mut jni::JNIEnv) -> Result<jni::jobject, String> {
        let keystore_class = class(env, "java/security/KeyStore")?;
        let get_instance = static_method(env, keystore_class, "getInstance", "(Ljava/lang/String;)Ljava/security/KeyStore;")?;
        let keystore = ((**env).CallStaticObjectMethod.unwrap())(env, keystore_class, get_instance, string(env, "AndroidKeyStore"));
        check(env, "KeyStore.getInstance")?;
        let load = method(env, keystore_class, "load", "(Ljava/security/KeyStore$LoadStoreParameter;)V")?;
        ((**env).CallVoidMethod.unwrap())(env, keystore, load, null_mut::<std::ffi::c_void>());
        check(env, "KeyStore.load")?;
        let get_key = method(env, keystore_class, "getKey", "(Ljava/lang/String;[C)Ljava/security/Key;")?;
        let key = ((**env).CallObjectMethod.unwrap())(env, keystore, get_key, string(env, ALIAS), null_mut::<std::ffi::c_void>());
        check(env, "KeyStore.getKey")?;
        if !key.is_null() {
            return Ok(key);
        }
        let builder_class = class(env, "android/security/keystore/KeyGenParameterSpec$Builder")?;
        let init = method(env, builder_class, "<init>", "(Ljava/lang/String;I)V")?;
        // PURPOSE_ENCRYPT | PURPOSE_DECRYPT
        let builder = ((**env).NewObject.unwrap())(env, builder_class, init, string(env, ALIAS), 3 as jni::jint);
        check(env, "KeyGenParameterSpec.Builder")?;
        let builder_sig = "([Ljava/lang/String;)Landroid/security/keystore/KeyGenParameterSpec$Builder;";
        let set_modes = method(env, builder_class, "setBlockModes", builder_sig)?;
        ((**env).CallObjectMethod.unwrap())(env, builder, set_modes, string_array(env, &["GCM"])?);
        let set_padding = method(env, builder_class, "setEncryptionPaddings", builder_sig)?;
        ((**env).CallObjectMethod.unwrap())(env, builder, set_padding, string_array(env, &["NoPadding"])?);
        let set_size = method(env, builder_class, "setKeySize", "(I)Landroid/security/keystore/KeyGenParameterSpec$Builder;")?;
        ((**env).CallObjectMethod.unwrap())(env, builder, set_size, 256 as jni::jint);
        check(env, "KeyGenParameterSpec settings")?;
        let build = method(env, builder_class, "build", "()Landroid/security/keystore/KeyGenParameterSpec;")?;
        let spec = ((**env).CallObjectMethod.unwrap())(env, builder, build);
        check(env, "KeyGenParameterSpec.build")?;
        let generator_class = class(env, "javax/crypto/KeyGenerator")?;
        let generator_instance =
            static_method(env, generator_class, "getInstance", "(Ljava/lang/String;Ljava/lang/String;)Ljavax/crypto/KeyGenerator;")?;
        let generator =
            ((**env).CallStaticObjectMethod.unwrap())(env, generator_class, generator_instance, string(env, "AES"), string(env, "AndroidKeyStore"));
        check(env, "KeyGenerator.getInstance")?;
        let generator_init = method(env, generator_class, "init", "(Ljava/security/spec/AlgorithmParameterSpec;)V")?;
        ((**env).CallVoidMethod.unwrap())(env, generator, generator_init, spec);
        check(env, "KeyGenerator.init")?;
        let generate = method(env, generator_class, "generateKey", "()Ljavax/crypto/SecretKey;")?;
        let key = ((**env).CallObjectMethod.unwrap())(env, generator, generate);
        check(env, "KeyGenerator.generateKey")?;
        Ok(key)
    }

    /// Seal (`encrypt`) or open `data`; sealing picks a fresh IV and returns it.
    unsafe fn crypt(env: *mut jni::JNIEnv, encrypt: bool, iv: &[u8], data: &[u8]) -> Result<(Vec<u8>, Vec<u8>), String> {
        let key = key(env)?;
        let cipher_class = class(env, "javax/crypto/Cipher")?;
        let get_instance = static_method(env, cipher_class, "getInstance", "(Ljava/lang/String;)Ljavax/crypto/Cipher;")?;
        let cipher = ((**env).CallStaticObjectMethod.unwrap())(env, cipher_class, get_instance, string(env, "AES/GCM/NoPadding"));
        check(env, "Cipher.getInstance")?;
        if encrypt {
            let init = method(env, cipher_class, "init", "(ILjava/security/Key;)V")?;
            ((**env).CallVoidMethod.unwrap())(env, cipher, init, 1 as jni::jint, key);
        } else {
            let spec_class = class(env, "javax/crypto/spec/GCMParameterSpec")?;
            let spec_init = method(env, spec_class, "<init>", "(I[B)V")?;
            let spec = ((**env).NewObject.unwrap())(env, spec_class, spec_init, 128 as jni::jint, bytes_in(env, iv));
            check(env, "GCMParameterSpec")?;
            let init = method(env, cipher_class, "init", "(ILjava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;)V")?;
            ((**env).CallVoidMethod.unwrap())(env, cipher, init, 2 as jni::jint, key, spec);
        }
        check(env, "Cipher.init")?;
        let iv = if encrypt {
            let get_iv = method(env, cipher_class, "getIV", "()[B")?;
            bytes_out(env, ((**env).CallObjectMethod.unwrap())(env, cipher, get_iv))
        } else {
            Vec::new()
        };
        let do_final = method(env, cipher_class, "doFinal", "([B)[B")?;
        let out = ((**env).CallObjectMethod.unwrap())(env, cipher, do_final, bytes_in(env, data));
        check(env, "Cipher.doFinal")?;
        Ok((iv, bytes_out(env, out)))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn a_file_vault_keeps_secrets_owner_only() {
        let dir = std::env::temp_dir().join(format!("mail-vault-{}", std::process::id()));
        FileVault.put(&dir, "a1", "pa ss").unwrap();
        assert_eq!(FileVault.get(&dir, "a1").unwrap(), "pa ss");
        #[cfg(unix)]
        {
            use std::os::unix::fs::PermissionsExt;
            let mode = std::fs::metadata(secret_path(&dir, "a1")).unwrap().permissions().mode();
            assert_eq!(mode & 0o777, 0o600);
        }
        FileVault.remove(&dir, "a1");
        assert!(FileVault.get(&dir, "a1").is_err());
        let _ = std::fs::remove_dir_all(&dir);
    }

    /// Touches the login keychain, so it runs only when asked:
    /// `cargo test -- --ignored keychain`.
    #[cfg(target_os = "macos")]
    #[test]
    #[ignore]
    fn the_keychain_keeps_a_secret_and_takes_over_an_old_file() {
        let dir = std::env::temp_dir().join(format!("mail-keychain-{}", std::process::id()));
        FileVault.put(&dir, "old", "from a file").unwrap();
        let vault = keychain::Keychain;
        assert_eq!(vault.get(&dir, "old").unwrap(), "from a file");
        assert!(!secret_path(&dir, "old").exists(), "the file moved into the keychain");
        assert_eq!(vault.get(&dir, "old").unwrap(), "from a file");
        vault.put(&dir, "new", "s3cret").unwrap();
        assert_eq!(vault.get(&dir, "new").unwrap(), "s3cret");
        vault.remove(&dir, "old");
        vault.remove(&dir, "new");
        assert!(vault.get(&dir, "new").is_err());
        let _ = std::fs::remove_dir_all(&dir);
    }
}

#!/bin/sh
# Build the native-widget camera app for a HarmonyOS phone: cargo (aarch64 OHOS)
# → stage the .so → sign → hvigor → install → launch.
#   build.sh [--no-launch] [--build-only|--app]
#
# Signing, chosen by SIGNING:
#   debug   (default) the DevEco auto-signing profile of the project named by
#           DEVECO_PROJECT. A debug profile only installs on the phones whose
#           UDID it lists, and it is bound to that project's bundle, so set
#           BUNDLE to match (the template one is com.example.myapplication).
#   release the certificate and profile issued by AppGallery Connect, given as
#           RELEASE_CERT, RELEASE_PROFILE, RELEASE_STORE, RELEASE_STORE_PASSWORD,
#           RELEASE_KEY_ALIAS and RELEASE_KEY_PASSWORD. Use --app to produce the
#           App Pack (.app) that AppGallery Connect takes for beta testing.
set -eu
BUNDLE=${BUNDLE:-dev.makepad.octosense.camera}
# AppGallery Connect refuses an upload whose version code it has seen before.
VERSION_CODE=${VERSION_CODE:-}
VERSION_NAME=${VERSION_NAME:-}
SIGNING=${SIGNING:-debug}
# Whose debug signing block to borrow. DevEco writes the material into the
# build-profile.json5 of whatever project is open, so the default is this
# project itself; point it at another project to reuse that one's profile.
DEVECO_PROJECT=${DEVECO_PROJECT:-}
# Where a built App Pack is kept. Outside the repository: the packs are
# release artifacts, they carry a signature, and one of them is whatever a
# tester installed.
ARCHIVE=${ARCHIVE:-$HOME/octosense-app-builds}
HERE=$(cd "$(dirname "$0")" && pwd)
: "${DEVECO_PROJECT:=$HERE/deveco}"
DEVECO=/Applications/DevEco-Studio.app/Contents
export JAVA_HOME=$DEVECO/jbr/Contents/Home
export PATH=$JAVA_HOME/bin:$DEVECO/tools/node/bin:$DEVECO/sdk/default/openharmony/toolchains:$PATH
export DEVECO_SDK_HOME=$DEVECO/sdk NODE_HOME=$DEVECO/tools/node
D=${DEVICE:-5ZGYD25B13020968}
cd "$HERE"
TMP_PROFILE=$(mktemp); TMP_APP=$(mktemp)
echo "==> cargo"
cargo build --release --target aarch64-unknown-linux-ohos 2>&1 | grep -E "^error|Finished" -A 6 | head -40
cp target/aarch64-unknown-linux-ohos/release/libcamera_oh.so deveco/entry/libs/arm64-v8a/
cp "$DEVECO/sdk/default/openharmony/native/llvm/lib/aarch64-linux-ohos/libc++_shared.so" deveco/entry/libs/arm64-v8a/
cd deveco
# The signing block carries paths and passwords, and the bundle is a build-time
# choice: inject both, then put the committed files back whatever happens.
cp build-profile.json5 "$TMP_PROFILE"; cp AppScope/app.json5 "$TMP_APP"
trap 'cp "$TMP_PROFILE" "$HERE/deveco/build-profile.json5"; cp "$TMP_APP" "$HERE/deveco/AppScope/app.json5"; rm -f "$TMP_PROFILE" "$TMP_APP"' EXIT INT TERM
BUNDLE="$BUNDLE" SIGNING="$SIGNING" DEVECO_PROJECT="$DEVECO_PROJECT" VERSION_CODE="$VERSION_CODE" VERSION_NAME="$VERSION_NAME" python3 - <<'PY'
import json, os, re
bundle, signing, project = os.environ["BUNDLE"], os.environ["SIGNING"], os.environ["DEVECO_PROJECT"]
if signing == "release":
    material = {
        "certpath": os.environ["RELEASE_CERT"],
        "keyAlias": os.environ.get("RELEASE_KEY_ALIAS", "key"),
        "keyPassword": os.environ["RELEASE_KEY_PASSWORD"],
        "profile": os.environ["RELEASE_PROFILE"],
        "signAlg": "SHA256withECDSA",
        "storeFile": os.environ["RELEASE_STORE"],
        "storePassword": os.environ["RELEASE_STORE_PASSWORD"],
    }
    block = '"signingConfigs": [{"name": "default", "type": "HarmonyOS", "material": %s}],' % json.dumps(material)
else:
    src = open(os.path.expanduser(project + "/build-profile.json5")).read()
    block = re.search(r'"signingConfigs":\s*\[(.*?)\n\s*\],', src, re.S).group(0)
bp = 'build-profile.json5'; s = open(bp).read()
s = re.sub(r'"signingConfigs":\s*\[.*?\n\s*\],', block.rstrip(',') + ',', s, count=1, flags=re.S)
s = re.sub(r'"compatibleSdkVersion":\s*"[^"]+"', '"compatibleSdkVersion": "6.0.1(21)"', s)
open(bp, 'w').write(s)
a = 'AppScope/app.json5'; t = open(a).read()
t = re.sub(r'"bundleName": "[^"]+"', '"bundleName": "%s"' % bundle, t)
if os.environ.get("VERSION_CODE"):
    t = re.sub(r'"versionCode": \d+', '"versionCode": %s' % os.environ["VERSION_CODE"], t)
if os.environ.get("VERSION_NAME"):
    t = re.sub(r'"versionName": "[^"]+"', '"versionName": "%s"' % os.environ["VERSION_NAME"], t)
open(a, 'w').write(t)
print("signing:", signing, "| bundle:", bundle)
PY
if [ "${1:-}" = "--app" ]; then
    echo "==> hvigor (App Pack for AppGallery Connect)"
    node $DEVECO/tools/hvigor/bin/hvigorw.js assembleApp --mode project -p product=default -p buildMode=release --no-daemon 2>&1 | tail -3
    PACK=$(ls build/outputs/default/*-signed.app 2>/dev/null | head -1)
    [ -n "$PACK" ] || PACK=$(ls */build/outputs/default/*-signed.app 2>/dev/null | head -1)
    [ -n "$PACK" ] || { echo "no signed App Pack was produced"; exit 1; }
    # hvigor empties build/ on the next run, so keep the pack that was uploaded:
    # a build that is on someone's phone has to stay reproducible from a file.
    VC=$(python3 -c "import json,re,sys; print(json.loads(re.sub(r'(?m)^\s*//.*$','',open('AppScope/app.json5').read()))['app']['versionCode'])")
    VN=$(python3 -c "import json,re,sys; print(json.loads(re.sub(r'(?m)^\s*//.*$','',open('AppScope/app.json5').read()))['app']['versionName'])")
    OUT=$ARCHIVE/$BUNDLE-$VN-$VC-$SIGNING
    mkdir -p "$OUT"
    cp "$PACK" "$OUT/$BUNDLE-$VN-$VC-$SIGNING.app"
    cp build/outputs/default/pack.info "$OUT/" 2>/dev/null || true
    shasum -a 256 "$OUT/$BUNDLE-$VN-$VC-$SIGNING.app" > "$OUT/sha256.txt"
    ls -la "$OUT"
    echo "==> saved to $OUT"
    exit 0
fi

echo "==> hvigor"
node $DEVECO/tools/hvigor/bin/hvigorw.js assembleHap --mode module -p product=default -p buildMode=release --no-daemon 2>&1 | sed 's/\x1b\[[0-9;]*m//g' | grep -E "Error Message|ERROR|BUILD" | sort -u
[ "${1:-}" = "--build-only" ] && exit 0
# The module is named like the Makepad host's ("makepad"): both HAPs share the bundle, and only a HAP
# with the same module name installs in place, keeping the permission grants across a host swap.
H=entry/build/default/outputs/default/makepad-default-signed.hap
ls -la "$H" | awk '{print "hap", $5, "bytes"}'
hdc -t $D shell "aa force-stop $BUNDLE" >/dev/null 2>&1 || true
hdc -t $D file send "$H" /data/local/tmp/camera.hap | tail -1
hdc -t $D shell bm install -p /data/local/tmp/camera.hap 2>&1 | grep -q success || { hdc -t $D shell "bm uninstall -n $BUNDLE" >/dev/null; hdc -t $D shell bm install -p /data/local/tmp/camera.hap 2>&1 | tail -1; }
[ "${1:-}" = "--no-launch" ] && exit 0
hdc -t $D shell "power-shell wakeup; hilog -r; aa start -a EntryAbility -b $BUNDLE" | tail -1
sleep ${SETTLE:-6}
hdc -t $D shell "hilog -x" | LC_ALL=C sed 's/\x1b\[[0-9;]*m//g' | LC_ALL=C grep -a "camera-oh\|xcomp:" | sed 's/.*camera-oh: //' | cut -c 1-180 | tail -20

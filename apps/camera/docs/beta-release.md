# Sharing the HarmonyOS camera app

The app in `apps/camera/oh` is a standalone HarmonyOS app: its own bundle
(`dev.makepad.octosense.camera`), its own ability and icon, and no dependency on
the OctoSense shell. What follows is how to get it onto someone else's phone.

## Build

    sh apps/camera/oh/build.sh --build-only     # a signed HAP for a phone
    sh apps/camera/oh/build.sh --app            # the App Pack (.app) that AppGallery Connect takes

`BUNDLE`, `VERSION_CODE` and `VERSION_NAME` override the identity;
`SIGNING=debug` (the default) reuses the DevEco auto-signing profile of the
project named by `DEVECO_PROJECT`, and `SIGNING=release` uses the certificate and
profile that AppGallery Connect issues:

    SIGNING=release VERSION_CODE=1000001 VERSION_NAME=1.0.1 \
    RELEASE_CERT=~/agc/release.cer RELEASE_PROFILE=~/agc/release.p7b \
    RELEASE_STORE=~/agc/release.p12 RELEASE_STORE_PASSWORD=… \
    RELEASE_KEY_ALIAS=… RELEASE_KEY_PASSWORD=… \
    sh apps/camera/oh/build.sh --app

A debug profile is bound to one bundle and to the phones whose UDID it lists, and
DevEco writes it for the bundle that `AppScope/app.json5` holds at the moment you
tick "Automatically generate signature". So set the bundle first, save, sync, then
sign. Signing against a stale bundle produces a profile the device rejects at
install with a bundle-name mismatch. A debug profile also lasts fourteen days.

## Where the build is saved

hvigor writes the pack to `deveco/build/outputs/default/` and empties that
directory on the next build, so `--app` copies the signed pack, its `pack.info`
and a sha256 out to

    $HOME/octosense-app-builds/<bundle>-<versionName>-<versionCode>-<signing>/

Set `ARCHIVE` to put it somewhere else. Keep it out of the repository: the packs
are signed release artifacts, and once a version code has gone to a tester the
file is the only record of exactly what they installed.

## Option 1: one or two testers, today

1. Ask each tester for their device UDID (Settings, or `hdc shell bm get --udid`).
2. AppGallery Connect → Users and permissions → Device management: add each one
   (up to 100). Regenerate the debug profile so it lists them.
3. Build the HAP and send it. They install it from a computer:
   `hdc file send camera.hap /data/local/tmp/ && hdc shell bm install -p /data/local/tmp/camera.hap`.

No review, but it needs a computer at their end and the profile expires, so
builds have to be re-signed periodically.

## Option 2: beta (open) testing through AppGallery Connect

Testers install from AppGallery with an invitation, no computer needed.

1. **Account.** A Huawei developer account with identity verification completed.
   An enterprise account is required for some categories; an individual account
   is enough for a test app.
2. **App.** Create the app in AppGallery Connect with bundle
   `dev.makepad.octosense.camera`, category Photography, and the supported
   device type (phone).
3. **Signing.** In AppGallery Connect create a release certificate and a release
   profile for that bundle. Keep the `.cer`, `.p7b` and the `.p12` keystore off
   this repository.
4. **Restricted permission.** The app writes to the system gallery
   (`ohos.permission.WRITE_IMAGEVIDEO`), which is an ACL permission: apply for it
   on the app's permission page and explain that the camera saves the photos and
   videos the person takes. Without approval the release profile will not carry it
   and saving will fail on a tester's phone.
5. **Build** the App Pack with `SIGNING=release … --app`.
6. **Upload** it under Distribute → Beta testing (open testing), add the release
   notes, screenshots and privacy statement, and submit for review. Huawei
   reviews beta builds too, typically in a working day or two.
7. **Countries/regions.** The version page asks where the version is
   distributed. A HarmonyOS app built against API 10 or later can only be
   distributed to the Chinese mainland, so that is the only real choice, and it
   follows that the developer account has to be a Chinese mainland account and
   the testers' Huawei IDs have to be Chinese mainland IDs. An overseas Huawei
   developer account cannot publish this app at all. Uploading the pack from
   DevEco Studio is also mainland-only (Hong Kong, Macau and Taiwan excluded).
8. **Invite** testers by link or by Huawei ID; they install from AppGallery. An
   open test that skips review allows 100 invitations, a reviewed one 200.

## Before you submit

- Replace the app icon if the drawn one is not what you want: it is
  `deveco/AppScope/resources/base/media/app_icon.png` and the layered pair in
  `deveco/entry/src/main/resources/base/media/`.
- The interface deliberately mirrors the Mate 70 Air camera. That is fine for a
  private beta; a public listing would be a trademark and design risk, so keep
  the test closed unless that is reviewed.
- Each upload needs a higher `VERSION_CODE` than the last.

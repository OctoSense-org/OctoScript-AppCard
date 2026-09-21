# AppGallery listing copy

Everything AppGallery Connect asks for when a version is submitted. The assets
beside this file are the icon at the size the console wants and four phone
screenshots taken from the running app on a Mate 70 Air.

## Identity

| field | value |
|---|---|
| bundle | dev.makepad.octosense.camera |
| app name, zh | OctoSense 相机 |
| app name, en | OctoSense Camera |
| category | 摄影摄像 / Photography |
| device type | phone |
| version | 1.0.0, version code 1000000 |

The version code has to rise on every upload. AppGallery rejects one it has
already seen, including from a test version that was never released.

## One-line introduction

- zh: 一款开源实验性相机，用 Makepad 与 Octoscript 构建的原生界面。
- en: An open, experimental camera app with a native interface built on Makepad and Octoscript.

## Description

zh:

    OctoSense 相机是一个开源的实验性相机应用，用于验证 Makepad 与 Octoscript 在
    HarmonyOS 上构建原生界面的能力。

    功能：
    - 前后摄像头实时预览
    - 拍照，照片直接保存到系统图库
    - 变焦、对焦、曝光补偿与闪光灯控制
    - 拍照、人像、闪拍、录像等多种模式

    本版本为测试版本，用于收集反馈。应用不联网、不收集任何个人信息，照片仅保存在本机。

en:

    OctoSense Camera is an open, experimental camera app. It exists to exercise a
    native interface built with Makepad and Octoscript on HarmonyOS.

    What it does:
    - Live preview on the front and back cameras
    - Photo capture, saved straight to the system gallery
    - Zoom, focus, exposure compensation and flash control
    - Photo, portrait, snapshot and video modes

    This is a test build, published to gather feedback. It has no network access,
    collects no personal information, and photos stay on the device.

## Release notes for the test version

zh: 首个测试版本。前后摄像头预览、拍照并保存到图库、变焦与对焦控制。欢迎反馈。

en: First test build. Front and back preview, capture to the gallery, zoom and
focus controls. Feedback welcome.

## Permissions to explain in the form

| permission | why |
|---|---|
| ohos.permission.CAMERA | the preview and capture |
| ohos.permission.MICROPHONE | sound while recording video |
| ohos.permission.WRITE_IMAGEVIDEO | saving a photo to the system gallery, restricted, needs approval |

The gallery permission is the one that takes review time. Apply for it on the
app's permission page and say plainly that the camera saves the photos the
person takes. Without approval the release profile will not carry it and saving
fails on a tester's phone.

## Before submitting

The interface deliberately mirrors the Mate 70 Air camera, which is fine for a
test among invited people and is a trademark and design risk for a public
listing. Keep the test closed until someone has reviewed that. Do not describe
the app as a Huawei product anywhere in the listing.

A privacy policy URL is mandatory. `privacy.md` beside this file is the text;
it has to be served from a public address before the form will accept it.

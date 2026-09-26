# Camera

Camera is an OctoSense system app (`os.camera`, OctoSense ADR 0004): a contained
script app over the runtime's `CameraPreview` widget.

| Path | What it is |
| --- | --- |
| [`script/`](script/) | The app: `manifest.json` (`storage`, `camera`, `microphone`, `library`), `main.splash` and `icon.png`: a full-screen preview with photo and video modes, flash, front/back, 1×/2×/5× zoom, a recording timer and the last capture as a thumbnail. |

The device stays with the runtime: `CameraPreview` draws the preview itself,
saves captures only into the app's own storage, and releases the camera when the
preview stops drawing or the app closes. Capture is implemented on Android and
HarmonyOS.

The earlier native Camera module (`native/`), its host-independent logic
(`logic/`), the ArkUI host (`oh/`), AppCard scenes, design source and fonts were
removed when Camera became a script app; they remain in Git history.

# 卡片应用模板（指引）

[English](README.md) | 简体中文

**卡片应用**是一个 L0 `page.card`，加上它的 `page.data.json` 和 `kit/`，由宿主降级为控件。
它是生成出来的，不是手写的：使用
[image-to-card 流程](../../flows/image-to-card/FLOW.md)（或者用
[Sketch 套件流程](../../flows/kits/sketch/FLOW.md) 生成套件），然后按
[docs/PUBLISHING.md](../../docs/PUBLISHING.md) 发布，此时 bundle 中放的是
`page.card` + `kit/`，而不是 `main.splash`。

卡片 bundle 的元数据脚手架（manifest、listing、图标、agent 说明）在 App Hub 的
[`templates/app/`](https://github.com/OctoSense-org/OctoSense-App-Hub/tree/main/templates/app)。
如果应用有自己的逻辑、状态和请求，请改用 [../script-app](../script-app/README.zh-CN.md)。

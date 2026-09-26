# 空调到家 · 原生服务 App Card

[English](README.md) | 简体中文

这是**同一个 Aircon 应用**，包含 [12 个画面状态](cards/README.md) 和
[14 个可复用的服务卡片变体](service-cards/README.md)。同级示例见 [../](../README.zh-CN.md)。
下面的命令都在本应用目录下运行。

下文中的原生 Studio 启动 / 抓取命令描述的是最初的验证方式。
新的原生测试请使用[内置 instrument](../../flows/core/NATIVE-INSTRUMENT.md)，并隐藏窗口。
历史证据保留其原始路径和哈希。

把同一次 Image 2.0 生成的 12 个 UX 画面转换为 Makepad 原生组件，并从场景中导出 14 个独立 service card 变体。目录独立于 Astro 网站。

服务归属分为订单、物流、安装、日历、支付。文字为原生 Label，操作为原生 KitButton/Button，卡面为原生 View，图标为原生 Svg。商品摄影和师傅头像是经过核对的局部图片素材。运行时不使用整张界面截图或图片热点。

## 入口

- [App Card 与事务 Tile 设计需求](../../docs/app-card-design-requirements.md)：原始邮件 / 消息溯源、原位组合交互、旅行时间线与出行 Sub Tiles，含后续设计验收标准
- [L0–L3、Theme Kit 与 Octos 架构评估](../../docs/layered-architecture-assessment.md)：现有实现、状态与来源差距、组件及外部动作的接入方案
- [事务窗口研究依据](../../docs/matter-centered-ux-research.md)：相关研究、已有系统与产品设计判断
- [image-to-appcard-flow 完整流水线](../../flows/image-to-card/README.zh-CN.md)：单次总图 → 8–12 个场景 → 原生服务卡片 → 交互状态 → WASM → Astro 网站
- [本项目流水线配置](image-to-appcard-flow.json)，命令：`bash ../../tools/image-to-appcard-flow.sh plan --project "$PWD" --manifest image-to-appcard-flow.json`
- [交互式 WASM 向导源码与验证](wizard/README.md)：真实 Makepad 控件，中文 / 英文，用户点击推进

- 启动原生交互演示：`../../flows/image-lib/.venv/bin/python runtime/run-demo.py --frame 6`
- [14 张独立原生卡片](review/service-cards.html)
- [12 个场景参考 / 原生对照](review/index.html)
- [独立卡片目录](service-cards/catalogue.json)：每个卡片都有 `page.card`、`page.data.json`、`kit/native/light/kit.json`、`components.l0`、`mapping.json` 和 `service-actions.json`
- [服务状态与使用方法](service/README.md)
- [Studio 环境与启动方式](runtime/README.md)
- [原始总图](source/atlas.png)与[原始提示词](source/prompt.txt)

## 验证结果

12 个场景的原生结构与语义检查、14 张卡片的独立挂载与输入检查、18 个真实原生流程状态，以及 38 项本地服务测试通过。详细记录见 [转换报告](evidence/conversion-report.md)。精确图像一致性仍有字体、图标和表面效果差异，原始未通过 gate 保留。

## 目录

| 路径 | 内容 |
| --- | --- |
| `source/` | 原始 2400 × 3456 总图、提示词、来源记录和 12 个原始裁切 |
| `cards/aircon-01` … `aircon-12` | 完整场景的原生组件、测量、映射、服务动作和 Studio 验收轮次 |
| `service-cards/<service>/<variant>/` | 可单独挂载的服务卡片，坐标已移至自身原点 |
| `service/` | 共享服务状态、数据契约、事件序列、冲突与幂等校验 |
| `runtime/` | Studio 启动、原生动作监听、状态到 L0 组件的绑定 |
| `measurements/` | 源图坐标与人工修正记录 |
| `evidence/` | 原生流程检查及最终转换报告 |
| `review/` | 本地参考 / 实际原生截图对照 |
| `../../flows/`, `../../tools/` | 共享的 image-to-AppCard 流水线；应用源码保存在当前目录 |

## 转换方法

原图和提示词保持不变。每帧先等比放入 406 × 776 逻辑画板，留边而不拉伸；测量实际像素、OCR 和照片边界，再用 Noto Sans SC 字体度量映射原生文字。`semantic-map.json` 记录每个元素的功能、原生渲染器及素材来源。编译结果采用 L0 + JSON placements + kit tokens。

独立卡片是从原生场景树中提取的组件子树。源图裁切只用于对照及照片素材，卡片的文字和交互仍由 Makepad 绘制。每个卡片保留来源画面及坐标变换记录。

Studio 验收使用其内建 `WidgetTreeDump`、`WidgetQuery`、`WidgetSnapshot`、布局检查、`Screenshot` 和 `Click`，记录实际 build id 和 request nonce。原生结构、图片一致性、服务状态测试分别报告；编译或语义预检不代替运行验收。`review/index.html` 不会将参考图冒充原生截图。

演示默认从选择安装时间开始，可直接操作原生按钮。要查看商品下单入口，使用 `--frame 1`；要直接试付款卡片，使用 `--frame 11`。关闭启动命令（Ctrl+C）会结束本次演示；原图、组件源码与验收记录仍保留。

安装预约成功后，可在另一个终端发送模拟服务回传，继续走到支付：

```sh
python3 runtime/service_session.py --session-dir runtime/demo-session dispatch --event '{"id":"demo-departed-1","action":"installation.technician_departed","actor":"provider"}'
python3 runtime/service_session.py --session-dir runtime/demo-session dispatch --event '{"id":"demo-completed-1","action":"installation.completed","actor":"provider"}'
```

这两个事件代表服务回传，支付仍需要在卡片中点击确认。每次新的业务事件使用新的事件 id；重发同一个 id 不会重复执行。

## 重建组件

在本目录执行：

```sh
../../flows/image-lib/.venv/bin/python scripts/author_cards.py
../../flows/image-lib/.venv/bin/python scripts/export_service_cards.py
python3 service/controller.py demo
python3 scripts/build_review.py
```

`author_cards.py` 会重建测量映射。手工修复过 `mapped.json` 后，仅运行 pipeline 的 `compile,capture,gate` 阶段，避免重新覆盖映射。Studio 抓取与服务交互监听共用宿主，需要分开运行；独立的设计与编译可以并行。

独立卡片验证在其他抓取和服务 watcher 停止后执行：`../../flows/image-lib/.venv/bin/python scripts/verify_standalone_cards.py --build-id '[当前编号]'`。它复用已启动的 Studio RunItem，按目录中每张卡自身的浮点宽高挂载，检查原生树、查询、布局和真实按钮 KitAction；禁用按钮必须不触发激活。`--check-inputs` 只检查导出文件，不连接 Studio。证据保存在 `evidence/standalone/<时间戳>/`，包含原始截图、未经缩放的视口裁切、build/nonce、源码和运行时哈希；`evidence/standalone-latest.json` 提供画廊入口。宿主仅写入该轮 `_runtime/`，其余归档由 `seal.json` 绑定。此检查使用固定 fixture，不代替完整图像验收或服务状态流程测试。

## 交互范围

选择时段会读取共享日历，提交预约时再次检查冲突。确认预约更新同一个安装预约及关联日程。日历“确认”表示已阅；“撤销日程”只移除日历记录，安装预约仍有效。付款采用整数分校验，用户确认前仅显示待支付请求；重复付款只生成一份模拟回执，撤销待付款不等于退款。

服务事件和付款为本地可重放演示。购物应用内部页面来自原图 01–02；其他应用的完整详情页由后续宿主路由接入。这里提供原生卡片及服务状态绑定，不包含商家、物流或支付平台的生产接口。

固定画板的排版可检查，尚不代表手机、桌面任意尺寸的响应式适配。原图的阴影、纸感与字形会有原生重建差异；精确验收状态以各轮 `gate.json` 和最终报告为准。

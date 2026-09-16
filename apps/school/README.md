# 学校邮件 · Service App Card

一封来自林老师的邮件，连接邮件、家庭日历与独立缴费服务。应用内可以读邮件、查看日程和核对凭证；桌面卡片可以直接确认日历更新、撤销日程、支付 ¥120 或撤销缴费请求。

这是本地演示，不连接邮箱、日历或支付账户。林老师只获得日历同步授权，支付始终需要用户点击。

## 体验路线

1. 打开收件箱里的林老师邮件，邮件内已嵌入日历与缴费卡片
2. 返回桌面，确认已更新的日历，或只撤销家庭日历记录；重新加入会恢复同一个事件
3. 在桌面直接支付、撤销缴费，或点击查看费用进入支付应用核对详情
4. 撤销缴费不会扣款，也不会修改日历；重新打开仍是同一张 ¥120 账单
5. 支付完成后查看凭证，再回到邮件查看相同的日程和付款记录

日历应用同样可以撤销或恢复事件，操作立即反映到桌面与邮件卡片。已付款后撤销日历不会退款或抹去凭证。演示的“上一步”恢复完整状态快照；它不是向真实服务发出撤销。

| 界面 | 场景 | 独立服务 |
| --- | --- | --- |
| 01 | 邮件收件箱 | Mail |
| 02 | 原邮件与嵌入卡片 | Calendar + Payment |
| 03 | 桌面已更新日历、待缴费 | Calendar + Payment |
| 04 | 日历撤销、缴费保留 | Calendar + Payment |
| 05 | 恢复同一日程 | Calendar + Payment |
| 06 | 日历详情与来源邮件 | Calendar |
| 07 | 应用内缴费详情 | Payment |
| 08 | 桌面缴费撤销 | Calendar + Payment |
| 09 | 重新打开同一缴费单 | Payment |
| 10 | 桌面支付完成 | Calendar + Payment |
| 11 | 应用内支付凭证 | Payment |
| 12 | 回到已处理的原邮件 | Mail + Calendar + Payment |

## 文件与接口

- `image-to-appcard-flow.json`：12 个实际 crop、14 个明确归属的独立卡片、导出与测试配置
- `source/atlas.png` / `source/prompt.txt`：一次生成的原始 atlas 与完整提示词
- `source/generation.json`：实际 provider、尺寸和原始路径；未暴露的模型保持未知
- `pipeline-output/intake/`：冻结原始输入、SHA-256、无拉伸 crop 和 406×776 @2x letterbox reference，以及双向坐标变换
- `cards/school-01..12/`：原生 contract、mapped、逐项源图测量、SVG、语义映射、L0 `.card` 与 kit
- `pipeline-output/service-cards/`：按 calendar/payment 归属提取的 14 个原生卡片子树
- `wizard/card-bundle/cards.bundle.json`：供原生 WASM 渲染器加载的 12 场景
- `wizard/service.mjs` / `wizard/copy.mjs`：纯 JavaScript 状态与逐帧中英文文案
- `route_test.json`：可用于真实原生点击验证的 4 条路线

`service.mjs` 导出 `scenario`、`createSession`、`getView`、`activateControl`、`nextUpdate`、`goBack`、`restart`、`errorMessage`。调用 `activateControl(session, sourceId, eventId, expectedRenderId)` 返回新的冻结会话，不修改输入。重复 event 幂等；过期 render、不可用操作和不存在的控件被拒绝。`getView` 只返回当前画面实际存在的文字、样式和控件绑定。

场景固定在 2026-09-24；活动为 9 月 25 日 14:00–16:00（UTC+08:00），收款方北辰小学，材料费 ¥120。金额使用整数分 `12000`，恢复事件或重新打开缴费均复用原实体 ID。

## 来源与验收边界

一次 built-in `image_gen` 调用生成全部 12 帧，请求 2400×3456、高质量。原始工具文件实际为 **907×1733**，不是请求尺寸；工具未提供模型名，因此不宣称为 Image 2.0 或已达到最高分辨率。保留原始字节，不通过放大冒充高分辨率生成。

12 个 crop 来自实际可见边框测量，原屏幕比例较窄，统一等比放入 406×776 原生画板，两侧留白。参考 PNG 仅用于比较，导出画面由原生 Label、Button、View、SVG 构成，没有整屏图片与透明热点。

源图桌面缴费卡原本只有“查看费用”。根据交互要求，03/04/05 原生版明确新增“支付 ¥120 / 撤销”，保留小型费用详情链接，并增加相应卡片高度。这是已记录的 UX 修正，不修改生成原图或将新增控件称为源图测量。源图低清晰度产生的文字错误依据固定场景文案修正；纸感、柔和阴影、植物墙纸仅作原生色面近似。

原生语义预检、12 场景编译、14 独立卡片编译、bundle 导出和 14 个状态/双语/绑定测试通过。Studio 实际截图、独立卡片原生输入与视觉相似度 gate 由根任务串行完成，此目录的生成/导出本身不代表这些 gate 已通过。

## 重新构建

在 flow 根目录使用仓库现有 Python venv 与 Node：

```sh
../../lab/image-to-appcard/.venv/bin/python scripts/build_school.py
node --test wizard/service.test.mjs
```

`build_school.py` 编译已测量的原生映射，首次提取独立卡片，并导出 bundle。已有独立卡片保留；修改映射后需为新的提取选择新输出目录再审核，不能把旧提取冒充当前映射。

`scripts/author_school.py` 保存最初测量和文字映射的可重现依据，适用于初次作者阶段。已有 Studio 历史时不应重新运行它覆盖后续视觉修正。图像生成与 Studio 不在这两个脚本中自动执行。

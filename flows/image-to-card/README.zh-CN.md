# image-to-card 设计流程

[English](README.md) | 简体中文

把**一张包含 8–12 个相关 UX 页面的生成图集（atlas）**变成经过测量的原生 Makepad 场景、
可复用的服务 App Card、由点击驱动的服务流程，以及一个供 OctoSense Astro 网站使用的
WebAssembly 包。

它扩展了现有的[图像适配器](../image-lib/README.md)，复用该适配器的语义编译器和 Studio
检测工具。它不会为每个状态单独生成一张图，也不会把截图变成可点击的热区。

```text
service scenario + shared state/actions + bilingual copy
  → one high-resolution atlas, exact submitted prompt, actual generation receipt
  → measured crops + reversible reference transforms
  → reviewed semantic map → native L0 + kit + data + source/widget mapping
  → independently owned service card subtrees
  → service reducer + app/desktop bindings + native KitAction inputs
  → Studio inspection and separate visual review
  → single-threaded Makepad WASM + hashed artwork/font package
  → atomic Astro integration → real native clicks in EN/CN and mobile
```

## 入口

命令在本仓库根目录下运行。步骤约定见 [FLOW.md](FLOW.md)。先安装图像库的
[Python 环境和 Studio 工具](../core/REPRODUCE.md)。服务/浏览器检查需要 Node；
只有在重新构建原生代码时，才需要 Rust WASM target 和匹配版本的 `cargo-makepad`。

```sh
export BEAUTY_PYTHON="$PWD/flows/image-lib/.venv/bin/python"
export FLOW_PROJECT="$PWD/examples/aircon"
export FLOW_SITE="/path/to/Octosense-website"

bash tools/image-to-appcard-flow.sh plan \
  --project "$FLOW_PROJECT" --manifest "$FLOW_PROJECT/image-to-appcard-flow.json"

bash tools/image-to-appcard-flow.sh run \
  --project "$FLOW_PROJECT" --manifest "$FLOW_PROJECT/image-to-appcard-flow.json" \
  --stages intake,semantic,compile,bundle,service-test
```

`tools/beauty-pipeline.sh --image-to-appcard-flow` 是等价的共享入口。
`plan` 打印确切的参数数组但不执行。`run` 在第一个失败处停止，并在
`pipeline-output/runs/` 下保留日志和运行回执（receipt）。`status` 显示最新的回执，
以及其输入指纹是否仍然匹配。命令成功不等于视觉验收：每份回执都会列出未运行的阶段。
重新运行会生成新的回执；失败的运行永远不会被覆盖或被静默重试。
`--node /path/to/node` 或 `SERVICE_NODE` 用于选择已安装的 Node 二进制。
检查命令可以把 `{python}`、`{node}`、`{project}`、`{workspace}` 和 `{website}`
用作完整参数。它们不经过 shell 求值执行。其 `cwd` 相对于服务项目，或者恰好是 `{website}`。

新项目从 [flow.template.json](examples/flow.template.json) 开始：
把它复制为 `<project>/image-to-appcard-flow.json`，并替换所有占位符。
[aircon manifest](examples/aircon.flow.json) 是
[`examples/aircon/image-to-appcard-flow.json`](../../examples/aircon/image-to-appcard-flow.json)
（包含 12 个场景的参考流程）的副本，单元测试读取的就是它。它包含相对路径、源图裁剪测量值、
14 个服务界面声明和测试命令。原始生成图像、服务实现、字体和归档证据保留在
`examples/aircon/` 中；manifest 不会下载或伪造它们。保持这两份副本完全一致。

## 1. 生成之前先完整编写整个体验

使用[图集提示词模板](examples/atlas-prompt.md)。在一次请求中描述 8–12 个状态，
使用同一套配色、字体体系、反复出现的服务标识和测试数据。向所选生成器请求其支持的最高
输出尺寸和质量。把实际输出尺寸与请求尺寸分开记录；放大（upscaling）不等于更高分辨率的生成。
保存确切提交的提示词和原始输出字节。永远不要把凭据写进提示词或 manifest。

每个场景声明 `surface: app` 或 `surface: desktop`。应用保留熟悉的浏览、阅读和编辑方式。
桌面 App Card 属于某个服务：它宣布一项具体的更新，展示相关数据，并提供限定范围的操作。
例如，一个经过授权的学校发件人可以更新日历；日历卡片随后提供确认和撤销。
单独的支付卡片仍然需要明确的支付操作。通用的聊天记录不是导航模型。

流程 manifest 包含 `schema_version: 1`、`id`、`artboard: [406,776]`、
`locales: ["en","cn"]`、`generation`、`scenes`、`cards`、`artwork`、`outputs`、
`browser_modules` 和 `checks`。每个场景提供唯一的字符串 `id`、`design_id`、
相对路径 `directory`、经过评审的图集 `crop: [x,y,width,height]` 以及 surface。
生成器是外部的：本流水线记录提供方/模型信息，但不调用图像 API，也不声称能自动理解视觉内容。

## 2. 保存并测量图集

运行 `--stages intake`。它对照解码后的图集校验每个裁剪区域，拒绝重叠和重复的 ID，
并以原生画板 2× 的底层分辨率保存精确裁剪图和加了留边（letterbox）的参考图。
回执记录原始哈希、实际尺寸、缩放比例、留边、正向/逆向变换以及派生哈希。
原始图集和提示词保持不变。相同输入的重放是幂等的；更改或编辑过的 intake
需要新的输出目录。

按照[映射规则](../image-lib/MAPPING-RULES.md)评审每张参考图、OCR、图稿边界、
原生字体度量和语义意图。在场景目录中，与参考图和提示词放在一起，编写
`contract.json`、`mapped.json`、`semantic-map.json` 和 `service-actions.json`。
intake 不会编写臆造的映射。如果缺少评审过的文件，`native.py` 会明确地失败。

对于新流程，`--stages prepare` 会把冻结的参考图、确切的提示词以及生成/裁剪来源信息
安装到每个新的场景目录中。它拒绝已存在的设计目录。参照
[contract 示例](../core/examples/image-contract.json)编写原生 contract，然后运行
`--stages observe,measure,map`，进行 Apple Vision OCR、源图界面测量和初始原生映射。
在 `semantic,compile` 之前，评审并确定语义决策，并添加服务操作。已存在的 `mapped.json`
会阻止重新执行 map，已存在的 `annotations.json` 会被保留。新的源图测量应使用新的设计版本，
而不是替换已评审的工作。
把请求的布局与观测到的像素分开。保留手工修复；流程运行器永远不会静默地重新运行
`map` 或 `catalogue.py`。

## 3. 编译并抽取服务卡片

`semantic,compile` 复用图像适配器。文本是原生 Label/富文本，控件是原生按钮/输入框，
界面是 View，图标是原生 SVG。只有声明过且哈希校验通过的图稿可以保持为位图。
图表必须绑定原生数值控件。每个源 ID 都与其实际的原生控件保持关联。

`--stages extract` 读取 `cards: [{id, scene, root, owner}]`。它抽取每个声明的原生子树，
平移其原点，过滤操作/语义，携带图稿来源信息，并编译出独立的 L0/kit 卡片。
归属是显式声明的，而不是从标题猜出来的。输出写到 `outputs.cards`；抽取内容变更时使用
新目录，以保留已评审的卡片。卡片的参考裁剪图是评审材料，永远不是其运行时 UI。
仍然需要独立的挂载、输入和布局验证；编译出子树并不代表完成了这些验证。

## 4. 绑定服务状态与交互

应用提供 `browser_modules` 中列出的 reducer、状态到 L0 的绑定以及浏览器控制器。
当前的网站集成期望 `wizard/service.mjs`、`wizard/render.mjs` 和 `wizard/wizard.mjs`。
新的邮件或健康流程需要自己编写的服务规则和对应的网站 UI；本工具不会从图像像素推断业务逻辑。

使用应用视图和桌面视图共享的稳定服务 ID。事件携带唯一 ID、操作者、操作和负载；
拒绝过期状态和重复的副作用。服务提供方的更新不能代替用户批准。确认时重新检查日程冲突；
货币使用整数的最小单位。撤销只影响其指定的服务操作：撤销一条日历条目不会取消预订；
取消一笔待处理的支付不会退款，也不会取消已完成的安装。

只在原生用户操作或明确提供的服务提供方更新时推进状态。动画可以在已确定的状态之间过渡；
它不能安排下一个业务事件。Back/Restart 恢复本地演示快照，并不声称撤回真实交易。
在 `checks.service-test` 中测试 reducer 不变量和所有分支，包括禁用的操作、重复支付、
撤销/恢复、冲突选择以及应用/桌面数据一致性。当前的 aircon reducer 有对应的 Python
和浏览器测试数据；幻灯片索引不是它的服务状态。

## 5. 原生与视觉证据

```sh
bash tools/image-to-appcard-flow.sh run \
  --project "$FLOW_PROJECT" --manifest "$FLOW_PROJECT/image-to-appcard-flow.json" \
  --stages capture --launch
# Inspect/review the current screenshots using the existing review packet tools.
bash tools/image-to-appcard-flow.sh run \
  --project "$FLOW_PROJECT" --manifest "$FLOW_PROJECT/image-to-appcard-flow.json" \
  --stages gate
```

按照复现指南启动匹配的 Studio/bridge/图稿服务器。验收时使用 Studio 的 release RunItem，
永远不要使用单独启动的原生二进制。采集实际的 WidgetTreeDump、WidgetQuery、
WidgetSnapshot、布局与裁剪、Screenshot 和 Click 结果。把证据绑定到构建 ID、请求 nonce
和源文件哈希；禁用的控件不得触发激活。串行化采集和服务监视进程。流程采集锁可以协调
流程运行器的任务，但无法阻止独立启动的监视进程。它只在不存在时创建临时设计别名，
并且永远不替换其他设计的目录。

原生场景挂载有它自己的陷阱；Calendar 移植记录了反复出现的问题——创建时的视口不是
图块尺寸、两个轴使用统一缩放、每个 crate 的降级检查门测试、图标资源策略的矛盾、
真实点击操作的结构、编辑状态渲染，以及验证纪律（每轮重新拟合比较变换、用证据裁剪图而不是
平均差异、走查陷阱、过期二进制检查）——见 [NATIVE-LESSONS.md](NATIVE-LESSONS.md)。
其中有两项需要维护者决定后才能变成代码改动；它们已在原处标出。

原生结构、图像保真度、视觉评审和服务正确性彼此独立。`gate` 保留现有严格的
图像/语义/原生/视觉判定，失败时以非零状态退出。浏览器测试或可运行的原型不能提升
一次未被接受的视觉比较。之前的 Studio 证据保持不可变。

### 不使用 Studio：instrument 路径

当验收目标是一组外部页面，而不是场景自己的 `reference.png` 时——例如 coding agent
根据图集重建应用——`capture` 和 `gate` 不适用，而在此之前根本没有东西检查渲染结果。
[`compare_screens.py`](compare_screens.py) 在全新的 `beauty-host` 中渲染每个编译后的场景
（每个场景一个进程，使用新的请求 nonce），并与对应页面比较：分带差异、每个场景的并排对比图、
对每个放置的文本控件做墨迹探测（是否存在，颜色和字重是否与页面一致）、最大的差异区域及其
矩形和两侧颜色，以及宿主日志中的资源和字体加载失败。`--app-grab` 以同样方式比较运行中
应用的画面，`--forbid-text` 指定应用不得绘制的控件（页面中模拟的状态栏）。
[`VISUAL-CHECKS.md`](VISUAL-CHECKS.md) 是这些数字所服务的规则手册：看并排对比图，
说出差异，修复，重新测量。语义预检现在还会拒绝能编译但无法绘制的取值域缺陷——
超出 0..1 的 `alignx`、小于其行框的文本框——并且 `compile` 会写入 manifest 声明的图稿前缀。

## 6. 打包并集成 WASM

```sh
bash tools/image-to-appcard-flow.sh run \
  --project "$FLOW_PROJECT" --manifest "$FLOW_PROJECT/image-to-appcard-flow.json" \
  --stages bundle,wasm,integrate --website "$FLOW_SITE"

bash tools/image-to-appcard-flow.sh run \
  --project "$FLOW_PROJECT" --manifest "$FLOW_PROJECT/image-to-appcard-flow.json" \
  --stages web-test --website "$FLOW_SITE"
```

`bundle.py` 导出原生场景，以及仅限它们引用且已声明的图稿及其哈希。它排除页面位图，
也不声称视觉已批准。[wasm/](wasm/README.md) 包含可移植的 Makepad 宿主、构建入口、
固定的依赖/补丁回执以及浏览器传输层。源码兼容性改动会被复现，而不会静默修改其他 checkout。
常规的 Astro 构建使用已完成的静态包，不需要 Rust 编译器或 Studio 进程。

渲染器是单线程 WASM，可以在普通静态托管上运行，不需要跨源隔离。嵌入真实的 CJK 字形，
并附上字体/原生许可证。保留原生启用状态、图像/矢量/文本就绪检查、同源发送方检查、
渲染代次 ID、过期点击拒绝和重绘输入锁。浏览器检查其确切的图稿源；原生运行时有明确的
OctoSense 部署基址。不同的 HTTPS 主机/前缀需要经过评审的重新构建。iframe、bridge 和
WASM 一起做缓存版本控制。Retry 要保留状态，键盘焦点保持稳定，手机缩放基于实际的原生坐标。

集成会先校验包、bundle 和图稿哈希，然后原子地替换网站的静态目录。格式错误的包会让之前
可用的包保持不变。集成只是本地源码更新；发布是另一个已有的网站工作流。本运行器不会推送或部署。

## 7. 浏览器与线上验证

浏览器检查必须点击真实的原生控件边界，而不是直接调用 reducer 操作或点击位图热区。
覆盖 EN 和 CN 的完整流程、移动端缩放、键盘等效操作、Back/Restart、撤销/恢复和明确的支付。
在部署的源上检查资源加载失败、原生就绪状态以及 `application/wasm` MIME。
网站部署后运行 `--stages hosted-test --website "$FLOW_SITE"`，执行 manifest 中的线上检查
并保存其结果。

aircon 原型通过了两种语言的完整线上流程。Chromium 1243 也出现了间歇性的冷场景/复用标签页
渲染停顿；这些失败仍然有记录。每种语言使用独立的浏览器上下文，并提供 Retry。不要把测试
自动重试到通过，也不要把超时当作就绪。生产环境的服务连接器、超出已测试固定画板的响应式重排、
任意新流程，以及每一种浏览器/设备，都需要额外的实现和证据。

## 流水线维护测试

```sh
"$BEAUTY_PYTHON" -m unittest discover -s flows/image-to-card -p 'test_*.py'
"$BEAUTY_PYTHON" -m unittest discover -s flows/image-to-card/wasm -p 'test_*.py'
```

这些测试验证图集来源、裁剪校验、原生子树抽取、bundle 边界以及阶段/错误行为。
它们与某个具体应用的 Studio 和浏览器验收是分开的。

# 空调到家 · Service App Card 状态与行为

本目录将同一空调流程拆为订单、物流、安装、日历和支付五个拥有自身数据与操作权限的服务应用。应用内页面与系统桌面卡片读取同一份状态。这里提供纯 Python 本地 reducer、便携 JSON 行为契约和 12 帧数据快照，供 Makepad 原生组件绑定。

所有服务事件和付款均为本地演示，不调用网络服务。`effects` 是模拟操作记录，不是已发送的服务请求。此目录的测试验证状态语义，不构成 Makepad 原生画面或输入测试。

## 文件

- `fixture.json`：金额使用整数分，时间包含时区，保留总图来源哈希
- `contract.json`：卡片归属、操作作用域、原生绑定约定和应用路由
- `controller.py`：`initial_state()`、`reduce(state, event)`、`view_model(state)`、`demo_states()`
- `test_controller.py`：冲突、关联撤销、重复事件、重复付款、作用域与改约测试
- `test_native_adapter.py`：原生动作 id 映射、请求 nonce、防旧动作与捕获归属保护
- `test_render_runtime.py`：12 个原生文件产物及动态文字、日期、控件可用性绑定
- `validation.json`：上述本地测试结果；不包含 Studio 实际输入或截图验证声明
- `fixtures/NN.state.json`、`NN.view.json`：由真实事件序列得到的 12 个数据状态，不以截图跳转伪造业务状态
- `fixtures/events.json`：可重放事件，含日历撤销及恢复分支

## 本地运行

在本目录执行：

```sh
python3 -m unittest -v test_controller.py test_native_adapter.py test_render_runtime.py
python3 controller.py demo
python3 controller.py init --output /tmp/aircon-state.json
python3 controller.py dispatch --state /tmp/aircon-state.json --event '{"id":"user-buy-1","action":"order.purchase_demo","actor":"user"}' --output /tmp/aircon-state.json
python3 controller.py view --state /tmp/aircon-state.json
```

事件也可通过 JSON 文件或 `--event -` 的标准输入传入。写入状态文件使用同目录临时文件替换；输入被拒绝时退出码为 2、标准错误输出 JSON 原因，原状态不会写回。并发调用者应在 reducer 外串行化同一服务实例的事件；不同演示实例应各自使用状态文件。

## 原生绑定

1. 使用 `view_model` 的 `cards[].id` 作为稳定卡片身份，不为每次状态更新创建新卡片
2. 标题、金额、时段与状态绑定为原生文字；`cards[].actions` 绑定原生按钮及 `enabled`，不要用透明图片热点替代
3. 点击按钮生成唯一 `id`，带上动作的 `action`、`actor` 和 `payload` 调用 reducer，再发布新的 view model
4. 点击卡片正文使用 `body_action` 打开所属应用；`app_route` 是交给原生宿主的路由意图。只提供原图 01–02 的完整购物应用内部布局；当前其他路由用原生标题、当前服务数据和返回桌面动作展示内部预览，`route-preview.json` 记录其范围，不会启动外部操作系统应用，也不代表重建了每个详细应用
5. `frame_id` 仅用于关联 12 张设计参考和自动化演示，不是业务状态本身。按钮可用性、已撤销与已付款文字由状态生成
6. Makepad Studio instrument 应对真实控件执行点击并读取状态/截图；本地 reducer 单元测试不能替代这些原生验证

## 交互含义

确认安装后，服务已有预约，日历在此前允许安装同步的前提下立即添加日程。日历卡片的“确认”是确认看到更新，不会再次添加日程。撤销日历仅删除安装日程，项目例会和服务预约保持原状。重新加入日历以同一事件 id 恢复；重新确认相同预约不会悄悄覆盖用户此前撤销日历的选择。

时段可用性来自共享演示日历数据的时间区间交集。周六 09:00–11:00 与项目例会冲突；14:00–16:00 可选。切换到周日会清除已选时段并重新计算冲突，周日两个时段均可用。提交时再次校验冲突。改约更新已有预约及关联日历事件的时间，不创建第二个预约或重复日程。取消时段草稿保留旧预约。明确点击“取消预约”才会取消未出发的安装服务及其关联日历，其他日程和支付数据不变。

安装完成的服务事件只创建 ¥130 的待支付请求。只有用户明确点击支付，且单号、金额、币种与当前账单一致，才生成模拟回执。重复点击只保留一份回执。“撤销支付”只撤销待支付请求，不取消安装、不退款；重新打开请求后可再次确认支付。已付款请求的撤销会被拒绝。

Provider 事件只能推进物流和服务状态，不能以该来源执行用户付款。`actor` 仅是本地契约校验，不是身份认证；真实集成需要宿主在调用前验证服务事件来源与用户权限。

## Studio 服务会话

在项目根目录启动服务会话前，应先由原生运行流程完成 Studio host 启动和固定画面捕获。会话与捕获共享单个 host，必须串行使用；映射、编译和 reducer 测试可并行。下面命令会切换该隔离 host 的当前请求：

```sh
python3 runtime/service_session.py start --frame 6 --build-id '[8]'
```

将示例 build id 替换为实际 Studio build。默认进入 watcher；`--once` 只挂载，随后可用 `watch` 恢复。指定独立会话目录时将全局参数放在子命令前，例如 `python3 runtime/service_session.py --session-dir runtime/my-session start --frame 6 --build-id '[8]'`。原生按钮产生 KitAction 后，watcher 核验当前 request nonce、layout、native manifest，映射真实原生控件 id，执行 reducer，再调用 `runtime/render_runtime.py` 生成新的 L0/kit/数据文件。

服务回传通过 inbox 队列显式输入，不由播放计时器自动假装发生：

```sh
python3 runtime/service_session.py dispatch --event '{"id":"delivery-confirmation-1","action":"logistics.delivered","actor":"provider"}'
python3 runtime/service_session.py status
```

每次挂载拥有唯一 nonce 和独立 actions 文件。未知控件、旧 nonce 和被复用的事件 id 会被拒绝。若其他任务挂载新的 current request，watcher 停止，不覆盖捕获任务。`runtime/session/events.jsonl`、`processed/*.result.json` 以及 `mounts/*` 保留动作和状态产物；这些日志属于本地演示证据，实际原生截图及仪器检查仍由 Studio 流程另行完成。

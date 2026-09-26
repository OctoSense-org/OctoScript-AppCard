# 空调到家 · Makepad Service App Card 转换报告

12 个完整场景、14 个独立卡片，归属订单、物流、安装、日历和支付服务。

原生转换验证：通过。Makepad 实际读取 494 个场景组件、检查 39 个原生按钮；完整服务流程 18 个检查点，另有 38 项本地状态与绑定测试。

文字、按钮、卡面与图标分别由原生 Label、Button、View、Svg 绘制。图片仅用于经过核对的商品摄影与头像，界面没有整屏图片热点。

严格图像一致性与原生功能分别验收。原图中的字形、图标细节、阴影与背景纹理仍有差异；图像 gate 的未通过结果完整保留，未调宽容差。

| 场景 | 原生结构 | 语义映射 | 严格图像验收 | 证据 |
| --- | --- | --- | --- | --- |
| aircon-01 | 通过 | 通过 | 待修 | [第 002 轮](../cards/aircon-01/rounds/002/gate.json) |
| aircon-02 | 通过 | 通过 | 待修 | [第 002 轮](../cards/aircon-02/rounds/002/gate.json) |
| aircon-03 | 通过 | 通过 | 待修 | [第 002 轮](../cards/aircon-03/rounds/002/gate.json) |
| aircon-04 | 通过 | 通过 | 待修 | [第 002 轮](../cards/aircon-04/rounds/002/gate.json) |
| aircon-05 | 通过 | 通过 | 待修 | [第 002 轮](../cards/aircon-05/rounds/002/gate.json) |
| aircon-06 | 通过 | 通过 | 待修 | [第 002 轮](../cards/aircon-06/rounds/002/gate.json) |
| aircon-07 | 通过 | 通过 | 待修 | [第 012 轮](../cards/aircon-07/rounds/012/gate.json) |
| aircon-08 | 通过 | 通过 | 待修 | [第 002 轮](../cards/aircon-08/rounds/002/gate.json) |
| aircon-09 | 通过 | 通过 | 待修 | [第 002 轮](../cards/aircon-09/rounds/002/gate.json) |
| aircon-10 | 通过 | 通过 | 待修 | [第 002 轮](../cards/aircon-10/rounds/002/gate.json) |
| aircon-11 | 通过 | 通过 | 待修 | [第 002 轮](../cards/aircon-11/rounds/002/gate.json) |
| aircon-12 | 通过 | 通过 | 待修 | [第 002 轮](../cards/aircon-12/rounds/002/gate.json) |

## 可验证的服务行为

- 购买订单、物流更新、送达、安装预约、师傅出发及付款由共享服务状态驱动
- 冲突时段禁用，预约成功写入同一日历事件；日历确认只表示已阅
- 撤销日历保留安装预约，重新加入恢复原事件
- 撤销待支付请求保留已完成安装；真实原生重复点击支付只产生一次模拟付款

- [完整原生服务流程](../evidence/native-flow/20260912-213620-584e35b5/report.json)
- [独立卡片挂载与输入验证](../evidence/standalone/20260913T043217.400761Z-15e85eb6/report.json)
- [本地状态测试](../service/validation.json)
- [Studio 运行环境与兼容补丁](../runtime/infrastructure.json)

## 使用边界

本地演示不连接商家、物流或支付平台。其他应用详情路由目前为原生服务数据预览。完整场景使用固定画板；独立卡片已使用各自实际宽高挂载，尚不承诺任意尺寸的响应式布局。

运行方法见 [README](../README.md)。源图与历史验证轮次保持不变。

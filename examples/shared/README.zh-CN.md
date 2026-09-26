# 共享应用支持

[English](README.md) | 简体中文

School、Health 和 Reunion 应用共用的浏览器渲染、字体度量和向导适配器。
此目录不是一个应用。

`flows-history.md`、各验证回执以及 `evidence/` 保留了早期的跨应用评审记录。
这些回执中的绝对路径记录的是当时的执行位置；这些应用现在位于 `examples/<name>/`。

`verify-standalone.py` 是历史上的 Studio 验证器。新的原生验证必须使用
[Makepad 的内置 instrument](../../flows/core/NATIVE-INSTRUMENT.md)，自动化时隐藏窗口；
`flows/image-to-card/compare_screens.py` 是一个可用的示例。

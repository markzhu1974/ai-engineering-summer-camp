# KiCad 实践检查清单

## Day 1：安装和入门教程

- [ ] 安装 KiCad 8.x。
- [ ] 打开 KiCad。
- [ ] 新建工程 `power_5v_to_3v3`。
- [ ] 找到并跟随一个 “1 小时 KiCad 入门教程”。
- [ ] 熟悉以下界面：
  - [ ] Project Manager
  - [ ] Schematic Editor
  - [ ] PCB Editor
  - [ ] Symbol Library
  - [ ] Footprint Assignment
  - [ ] DRC
  - [ ] Gerber Viewer

## Day 2：完成原理图

- [ ] 放置 LDO 稳压器。
- [ ] 放置输入端子 J1。
- [ ] 放置输出端子 J2。
- [ ] 放置输入电容 C1。
- [ ] 放置输出电容 C2。
- [ ] 可选：放置 LED 和限流电阻。
- [ ] 连接网络。
- [ ] 添加网络标签：`+5V`、`+3V3`、`GND`。
- [ ] 运行 Electrical Rules Checker。
- [ ] 截图保存到 `screenshots/`。

## Day 3：完成 PCB 和 Gerber

- [ ] 为所有元件分配 footprint。
- [ ] 从原理图更新 PCB。
- [ ] 规划板框 Edge.Cuts。
- [ ] 放置元件。
- [ ] 完成布线。
- [ ] 添加 GND 铺铜。
- [ ] 运行 DRC。
- [ ] 修复 DRC 中的明显错误。
- [ ] 导出 Gerber。
- [ ] 导出 Drill。
- [ ] 使用 Gerber Viewer 检查制造文件。
- [ ] 截图保存到 `screenshots/`。


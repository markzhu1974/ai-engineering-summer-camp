# AI 编程安全规则

本周你会让 Opencode 读取、修改、运行本地项目。为了避免误删、泄露密钥或把项目改乱，请严格遵守下面的规则。

## 1. 只在练习目录中操作

本周所有代码修改都应该发生在：

```text
task-tracker/
```

不要让 Opencode 修改：

- 课程其他周的目录
- Windows 用户目录
- 下载目录
- 桌面上的无关项目
- 浏览器、聊天记录或密钥文件

## 2. API Key 不进项目

不要把 DeepSeek API Key 写入：

- `README.md`
- `.py` 文件
- `.md` 文件
- 截图
- 终端记录
- 提示词记录

如果你误把 API Key 发给了 AI 或写入文件，立即到 DeepSeek 平台删除这个 Key，并重新创建一个新的。

## 3. 大改前先创建快照

每次进入新实验前，回到 `week6`，复制一份项目：

```powershell
Copy-Item -Recurse task-tracker snapshots/task-tracker-exp编号-before
```

示例：

```powershell
Copy-Item -Recurse task-tracker snapshots/task-tracker-exp06-before
```

快照不是备份系统，但足够支撑本周训练。

## 4. 先让 AI 解释，再让 AI 修改

陌生项目或复杂需求，不要直接说“帮我改”。

先用：

```text
请先只读分析，不要修改文件。
```

再用：

```text
请先给出修改计划，列出你准备修改哪些文件、为什么修改、如何验证。
```

确认计划合理后，再批准修改。

## 5. 每次修改后必须自己运行验证命令

Opencode 说“已完成”不等于真的完成。你必须亲自运行：

```powershell
python -m pytest
```

必要时再运行：

```powershell
python -m task_tracker
```

把结果写入报告。

## 6. 不批准危险命令

看到这些命令时，先停下来：

- 删除整个目录
- 修改系统环境变量
- 打印所有环境变量
- 读取密钥文件
- 上传文件到网络
- 下载并运行陌生脚本
- 修改课程根目录之外的文件

如果确实需要安装依赖，先查官方网站，再手动执行。

## 7. 出错时先缩小问题

不要连续让 AI 盲目修 5 次。

推荐流程：

1. 复制完整报错。
2. 要求 AI 只分析，不修改。
3. 让 AI 指出最可能的原因。
4. 让 AI 提供最小修改方案。
5. 修改后运行测试。
6. 仍失败时，把新的报错继续给 AI。

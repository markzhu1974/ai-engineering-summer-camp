# Opencode + DeepSeek 配置指南

本文件只负责配置 AI 编程工具。完成后，再进入 `task-tracker` 做项目实验。

## 1. 你需要准备什么

- VS Code
- Python
- Node.js LTS
- Opencode
- DeepSeek API Key
- 稳定网络

## 2. 确认 Opencode 可用

打开 PowerShell：

```powershell
opencode --version
```

如果显示版本号，继续下一步。

如果提示找不到命令：

1. 重新打开一个 PowerShell。
2. 再运行一次 `opencode --version`。
3. 仍失败时，回到 Opencode 官方文档：https://opencode.ai/docs/
4. 按最新安装说明重新安装。

## 3. 获取 DeepSeek API Key

1. 打开 DeepSeek API 文档：https://api-docs.deepseek.com/
2. 登录开放平台。
3. 进入 API Keys。
4. 创建新的 API Key。
5. 复制 API Key。

API Key 只应该放在 Opencode 的连接配置中，不应该写入项目文件。

## 4. 在项目目录启动 Opencode

进入 `week6/task-tracker`：

```powershell
cd task-tracker
```

启动：

```powershell
opencode
```

## 5. 连接 DeepSeek

在 Opencode 中输入：

```text
/connect
```

然后按界面提示：

1. 选择 DeepSeek。
2. 粘贴 API Key。
3. 确认连接。

如果 Opencode 要求填写接口地址，DeepSeek API 文档中的基础地址是：

```text
https://api.deepseek.com
```

## 6. 选择模型

在 Opencode 中输入：

```text
/models
```

选择一个 DeepSeek 模型。

建议：

- 优先选择速度较快、成本较低的模型完成常规代码生成和解释。
- 遇到复杂设计、重构或排错时，再选择推理能力更强的模型。
- 模型名称以 Opencode 和 DeepSeek 当前界面显示为准。

## 7. 第一次测试连接

在 Opencode 中输入：

```text
请确认你现在可以读取当前文件夹。只列出当前目录结构，不要创建、修改或删除任何文件。
```

你应该看到 Opencode 返回当前目录中的文件列表或说明当前目录为空。

如果它准备修改文件，取消操作，并重新强调“只读分析”。

## 8. 安全边界

每次让 Opencode 修改代码前，先检查：

- 当前目录是不是 `task-tracker`。
- 是否已经创建快照。
- 提示词里是否明确了修改范围。
- 是否要求它先说明计划。
- 是否要求它修改后告诉你运行哪些命令验证。

不要批准你看不懂的命令。尤其不要批准删除目录、清空目录、上传文件、打印环境变量、读取系统密钥等操作。

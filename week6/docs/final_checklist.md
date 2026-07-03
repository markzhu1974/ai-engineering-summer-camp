# Week 6 最终验收清单

完成本周训练后，逐项检查。

## 环境

- [ ] VS Code 已安装。
- [ ] Python 可用，`python --version` 正常。
- [ ] pip 可用，`pip --version` 正常。
- [ ] Node.js 可用，`node -v` 正常。
- [ ] Opencode 可用，`opencode --version` 正常。
- [ ] Opencode 已连接 DeepSeek。

## 项目

- [ ] `task-tracker/pyproject.toml` 或 `task-tracker/requirements.txt` 存在。
- [ ] `task-tracker/src/task_tracker` 存在。
- [ ] `task-tracker/tests` 存在。
- [ ] 项目可以通过 `python -m task_tracker` 启动。
- [ ] 项目包含 `Task` 和 `TaskService`。
- [ ] 项目包含 pytest 测试。

## 功能

- [ ] 可以新增任务。
- [ ] 可以列出任务。
- [ ] 可以标记任务完成。
- [ ] 可以搜索任务。
- [ ] 如果完成了 due_date 实验，可以显示截止日期。

## 验证命令

在 `task-tracker` 中运行：

```powershell
.\.venv\Scripts\Activate.ps1
python -m pytest
python -m task_tracker
```

检查：

- [ ] `python -m pytest` 通过。
- [ ] 程序能启动。
- [ ] README 中的命令真实可用。

## AI 使用过程

- [ ] 至少做过一次只读分析。
- [ ] 至少做过一次修改前计划。
- [ ] 至少做过一次测试优先开发。
- [ ] 至少做过一次 Bug 修复记录。
- [ ] 至少做过一次重构。
- [ ] 至少做过一次代码审查。
- [ ] 至少做过一次 VS Code 文件比较。

## 文件与报告

- [ ] `snapshots/` 中至少有 5 个快照。
- [ ] `reports/prompt_log.md` 已填写。
- [ ] `reports/bug_fix_log.md` 已填写。
- [ ] `reports/final_report.md` 已填写。
- [ ] `task-tracker/README.md` 已完成。
- [ ] `task-tracker/AGENTS.md` 已完成。

## 安全

- [ ] 没有把 DeepSeek API Key 写入任何项目文件。
- [ ] 没有让 AI 修改课程其他周的目录。
- [ ] 没有批准看不懂的危险命令。
- [ ] 每次大改前都创建了快照。

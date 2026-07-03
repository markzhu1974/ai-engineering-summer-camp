# Week 6 实验脚本：Opencode + DeepSeek 完成 Task Tracker

本脚本从空文件夹开始。每一步都需要你亲自输入命令、查看结果、记录发现。

## 实验 0：创建本地项目与快照机制

目标：建立 `task-tracker` 项目文件夹和 `snapshots` 快照文件夹。

### 步骤

1. 在 VS Code 中打开 `week6`。
2. 打开终端。
3. 创建文件夹：

```powershell
mkdir task-tracker
mkdir snapshots
```

4. 进入项目：

```powershell
cd task-tracker
```

5. 启动 Opencode：

```powershell
opencode
```

6. 输入提示词：

```text
请只读分析当前文件夹，不要创建、修改或删除任何文件。
请告诉我当前文件夹里有什么，以及它是否适合开始创建一个 Python 命令行项目。
```

### 验收

- Opencode 没有修改文件。
- 你知道当前 `task-tracker` 是空项目。
- `week6` 下存在 `snapshots` 文件夹。

## 实验 1：只读分析与精准上下文

目标：练习让 AI 先观察，不急着写代码。

### 步骤

1. 确认仍在 `task-tracker`：

```powershell
pwd
```

2. 在 Opencode 中输入：

```text
你是我的 Python 项目开发助手。当前目录将用于创建一个命令行 Task Tracker。
在我明确说“开始修改”之前，你只能只读分析，不能创建、修改或删除文件。

请根据当前空目录，列出你建议生成的 Python 项目结构，包括每个文件的作用。
```

3. 阅读它给出的结构。
4. 在 `reports/prompt_log.md` 中记录：
   - 你输入的提示词
   - AI 给出的文件结构
   - 你是否理解每个文件的作用

如果 `reports/prompt_log.md` 还不存在，先回到 `week6` 复制模板：

```powershell
cd ..
Copy-Item reports/prompt_log_template.md reports/prompt_log.md
cd task-tracker
```

### 验收

- 没有生成任何文件。
- 你能说出 `pyproject.toml`、`src/task_tracker`、`tests` 的作用。

## 实验 2：从需求生成可运行 Python 项目

目标：让 Opencode 生成第一版可测试、可运行的 Task Tracker。

### 步骤

1. 回到 `week6`：

```powershell
cd ..
```

2. 创建快照：

```powershell
Copy-Item -Recurse task-tracker snapshots/task-tracker-exp02-before
```

3. 进入项目：

```powershell
cd task-tracker
```

4. 启动或继续 Opencode。
5. 输入提示词：

```text
开始修改。

请在当前目录创建一个 Python 命令行项目，项目名为 task-tracker。

硬性要求：
1. 使用 src layout，源码放在 src/task_tracker。
2. 至少创建 task.py、service.py、cli.py、__main__.py。
3. 使用 dataclass 定义 Task。
4. 使用 TaskService 管理任务。
5. 使用 pytest 编写 TaskService 的单元测试。
6. 第一版功能包括：新增任务、列出任务、标记任务完成。
7. 任务数据先保存在内存中，不要引入数据库。
8. 不要引入 Web 框架，不要做图形界面。
9. 修改完成后，请告诉我你创建了哪些文件，以及我应该运行哪些命令验证。
```

6. 等待 Opencode 修改文件。
7. 在终端运行：

```powershell
python -m pytest
```

8. 如果测试通过，继续运行程序：

```powershell
python -m task_tracker
```

### 验收

- `python -m pytest` 通过。
- 程序能启动并显示命令行交互或使用说明。

## 实验 3：读懂生成项目

目标：不是只会运行，还要知道每个核心文件在做什么。

### 步骤

1. 在 Opencode 中输入：

```text
请只读分析当前项目，不要修改文件。
请按初学者能理解的方式解释：
1. pyproject.toml 或 requirements.txt 中每个关键配置的作用。
2. task.py 中 Task 的字段和方法。
3. service.py 中 TaskService 如何管理任务。
4. cli.py 或 __main__.py 如何接收用户输入并调用 TaskService。
5. tests 目录中的测试覆盖了哪些行为，哪些行为还没有覆盖。
```

2. 打开 `pyproject.toml` 或 `requirements.txt`，对照解释逐行查看。
3. 打开 `src/task_tracker` 和 `tests` 下的文件，对照解释查看。
4. 在 `reports/prompt_log.md` 中记录你最不理解的 3 个点。

### 验收

- 你能找到主程序入口。
- 你能找到业务逻辑所在类。
- 你能找到测试类。

## 实验 4：新增搜索功能，练习测试优先

目标：先写测试，再实现功能。

### 步骤

1. 回到 `week6`：

```powershell
cd ..
```

2. 创建快照：

```powershell
Copy-Item -Recurse task-tracker snapshots/task-tracker-exp04-before
```

3. 进入项目：

```powershell
cd task-tracker
```

4. 在 Opencode 中输入：

```text
请使用测试优先的方式新增“按关键词搜索任务”功能。

要求：
1. 先修改或新增 pytest 测试，覆盖按标题关键词搜索。
2. 搜索应忽略大小写。
3. 空关键词应返回空列表。
4. 再实现 TaskService 中的搜索方法。
5. 如果命令行 App 结构适合，也为用户增加 search 命令。
6. 不要引入新框架。
7. 修改完成后说明改了哪些文件，并告诉我验证命令。
```

5. 运行：

```powershell
python -m pytest
```

6. 如果测试失败，把完整报错发给 Opencode：

```text
请只分析这个测试失败原因，先不要修改文件。
报错如下：
粘贴完整报错
```

7. 读懂原因后，再让它做最小修改。

### 验收

- 搜索功能有测试。
- `python -m pytest` 通过。
- 命令行中可以使用搜索功能，或 README 中说明该功能暂时只在服务层可用。

## 实验 5：故意制造 Bug，再用证据修复

目标：练习把“失败现象 -> 可复现测试 -> 修复 -> 验证”串起来。

### 步骤

1. 创建快照：

```powershell
cd ..
Copy-Item -Recurse task-tracker snapshots/task-tracker-exp05-before
cd task-tracker
```

2. 手动打开 `service.py`。
3. 找到标记任务完成的方法。
4. 故意制造一个小 Bug，例如让它错误地完成第一个任务，而不是指定任务。
5. 保存文件。
6. 运行：

```powershell
python -m pytest
```

7. 如果测试没有失败，说明测试不够强。让 Opencode 先补测试：

```text
请只修改测试，先不要修改生产代码。
当前标记完成任务的逻辑可能存在“完成了错误任务”的问题。
请添加一个能暴露这个问题的 pytest 测试。
```

8. 测试失败后，把报错给 Opencode：

```text
现在测试失败了。请根据失败测试修复生产代码。
要求：
1. 只做最小必要修改。
2. 修复后解释根因。
3. 告诉我应该重新运行哪些命令。

失败信息如下：
粘贴完整报错
```

9. 运行：

```powershell
python -m pytest
```

10. 填写 `reports/bug_fix_log.md`。

### 验收

- 你有一个失败过的测试。
- 修复后测试通过。
- Bug 修复记录中写清楚了根因和验证命令。

## 实验 6：多文件功能与计划先行

目标：新增截止日期 due_date，练习先看计划再批准修改。

### 步骤

1. 创建快照：

```powershell
cd ..
Copy-Item -Recurse task-tracker snapshots/task-tracker-exp06-before
cd task-tracker
```

2. 在 Opencode 中输入：

```text
请先不要修改文件。

我想为任务增加可选截止日期 due_date，格式为 yyyy-MM-dd。
请先给出实施计划：
1. 需要修改哪些类。
2. 每个类为什么要改。
3. 需要新增或修改哪些测试。
4. 命令行交互需要怎么变化。
5. 如何验证功能正确。
```

3. 阅读计划。
4. 如果计划太大，要求缩小：

```text
请把计划缩小为最小可交付版本，只支持新增任务时输入可选 due_date，并能在列表中显示。
```

5. 确认后输入：

```text
按刚才的最小计划开始修改。请保持 Python + venv + pytest，不要引入新框架。
```

6. 运行：

```powershell
python -m pytest
python -m task_tracker
```

### 验收

- Task 支持可选 due_date。
- 测试覆盖 due_date。
- 命令行能展示 due_date。

## 实验 7：重构但不改变行为

目标：让代码更清楚，但功能不变。

### 步骤

1. 创建快照：

```powershell
cd ..
Copy-Item -Recurse task-tracker snapshots/task-tracker-exp07-before
cd task-tracker
```

2. 先运行基线测试：

```powershell
python -m pytest
```

3. 在 Opencode 中输入：

```text
请只读分析当前代码，找出 3 个可以提升可读性的重构点。
不要修改文件。
要求每个建议都说明：
1. 当前问题是什么。
2. 重构后行为是否改变。
3. 应该用什么测试证明行为没变。
```

4. 选择一个最小重构点。
5. 输入：

```text
请只执行第 1 个重构点。
要求：
1. 不改变外部行为。
2. 不新增功能。
3. 保持现有测试通过。
4. 修改后说明改动文件和验证命令。
```

6. 运行：

```powershell
python -m pytest
```

### 验收

- 重构后测试仍通过。
- 你能说明这次重构没有改变什么行为。

## 实验 8：本地代码审查与文件比较

目标：练习让 AI 审查代码，同时自己用 VS Code 比较快照。

### 步骤

1. 在 Opencode 中输入：

```text
请以代码审查的方式只读检查当前项目，不要修改文件。
请按严重程度列出问题：
1. 可能导致错误行为的问题。
2. 测试缺口。
3. 可维护性问题。
4. 文档缺口。
每个问题都要指出具体文件和原因。
```

2. 打开 VS Code 文件比较：
   - 右键 `snapshots/task-tracker-exp07-before` 中的某个文件。
   - 选择 Select for Compare。
   - 右键当前 `task-tracker` 中的同名文件。
   - 选择 Compare with Selected。
3. 对照 AI 审查结果，判断哪些问题值得修。
4. 只选择一个小问题修复。

### 验收

- 你至少完成了一次本地文件比较。
- 你知道 AI 审查结果需要人工判断，不是全部照单全收。

## 实验 9：补 README 与交付说明

目标：让项目对别人可运行。

### 步骤

1. 创建快照：

```powershell
cd ..
Copy-Item -Recurse task-tracker snapshots/task-tracker-exp09-before
cd task-tracker
```

2. 在 Opencode 中输入：

```text
请为当前项目编写 README.md。

要求包括：
1. 项目简介。
2. 环境要求：Python、venv、pytest。
3. 如何运行测试。
4. 如何打包。
5. 如何启动程序。
6. 当前支持的命令。
7. 一个 5 分钟试用流程。

不要夸大项目能力，不要写没有实现的功能。
```

3. 运行 README 中写的命令，确认可用。

### 验收

- README 中的命令能实际运行。
- README 没有写未实现的功能。

## 实验 10：用 AGENTS.md 固化项目规则

目标：把反复提醒 AI 的规则写到项目里。

### 步骤

1. 创建快照：

```powershell
cd ..
Copy-Item -Recurse task-tracker snapshots/task-tracker-exp10-before
cd task-tracker
```

2. 在 Opencode 中输入：

```text
请创建 AGENTS.md，用于记录这个项目中 AI 助手必须遵守的规则。

要求包括：
1. 项目技术栈：Python、venv、pytest。
2. 不使用 Web 框架、不使用数据库，除非我明确要求。
3. 修改前先说明计划。
4. 修改后必须说明验证命令。
5. 新功能优先补测试。
6. 不读取、不输出、不保存任何 API Key 或系统密钥。
7. 默认只修改 task-tracker 项目内文件。
```

3. 让 Opencode 重新读取规则：

```text
请读取 AGENTS.md，并用 5 条要点复述你接下来在本项目中要遵守的规则。不要修改文件。
```

### 验收

- `AGENTS.md` 存在。
- Opencode 能复述项目规则。
- 后续提示词可以更短，但仍要明确任务目标。

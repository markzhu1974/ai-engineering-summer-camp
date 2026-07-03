# 本地快照目录

本目录用于保存 `task-tracker` 的阶段性副本。

每次进入新实验前，在 `week6` 目录下运行类似命令：

```powershell
Copy-Item -Recurse task-tracker snapshots/task-tracker-exp04-before
```

命名建议：

- `task-tracker-exp02-before`
- `task-tracker-exp04-before`
- `task-tracker-exp05-before`
- `task-tracker-exp06-before`
- `task-tracker-exp07-before`
- `task-tracker-exp09-before`
- `task-tracker-exp10-before`

如果项目被改坏，不要覆盖当前目录。可以复制一个恢复目录：

```powershell
Copy-Item -Recurse snapshots/task-tracker-exp04-before task-tracker-recovery
```

# Week 4: RAG and Agent Knowledge Assistant

这是暑期 AI 工程实践训练营第四周的完整 Python 工程。

本周主题是 Agent + RAG。和前几周不同，本周主入口不是 Jupyter Notebook，而是 Python 程序工程。

原因：

- RAG 需要读取文档、切分文本、建立索引、保存索引文件。
- Agent 需要组织工具、调用工具、处理用户问题。
- MCP 的核心思想也是“程序之间用标准协议调用工具”。
- 这些内容更接近真实应用，适合用 `.py` 脚本和命令行运行。

## 项目结构

```text
week4/
├── README.md
├── 运行指南.md
├── requirements.txt
├── .vscode/
│   ├── extensions.json
│   └── settings.json
├── data/
│   └── docs/
│       ├── kicad_basics.md
│       ├── pcb_design_flow.md
│       └── rag_agent_notes.md
├── results/
├── vector_store/
└── src/
    ├── __init__.py
    ├── config.py
    ├── document_loader.py
    ├── build_index.py
    ├── rag_ask.py
    ├── tools.py
    ├── agent_demo.py
    └── mcp_like_demo.py
```

## 运行入口

请先阅读：

```text
运行指南.md
```

核心运行命令：

```powershell
python src/build_index.py
python src/rag_ask.py --question "KiCad 的 PCB 设计流程是什么？"
python src/agent_demo.py --question "请列出知识库文档"
python src/mcp_like_demo.py
```


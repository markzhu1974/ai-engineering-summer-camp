# 暑期AI工程实践训练营

**课程目标**

本训练营面向数学\+AI双专业本科生，以"AI辅助PCB设计"为最终目标，采用项目驱动（Project\-Based Learning）的方式，帮助学生在暑假期间建立现代AI工程开发能力，掌握AI Coding工作流，并完成AI辅助PCB设计项目的前期技术准备。需要学员具备基本的Python编程基础（如果没有，先学这个预备课程）

完成课程后，希望学生具备以下能力：

- 熟练使用Python进行AI开发 

- 掌握PyTorch深度学习模型训练流程 

- 能够开发基于大语言模型的AI应用 

- 掌握RAG、Agent等LLM应用开发技术 

- 熟悉KiCad PCB设计流程 

- 初步理解强化学习在PCB布局中的应用 

- 熟练使用Opencode、DeepSeek等AI Coding工具 

- 为后续AI辅助PCB设计项目做好技术储备



# 课程整体安排

# 第一周 Python AI工程基础

## 课程主题

**从Python开发者成长为AI工程师——理解AI开发的完整流程**

### 本周目标

通过一个简单的线性回归案例，理解一个AI项目从数据处理到模型训练、预测和可视化的完整开发流程，建立后续深度学习课程的工程认知。

本周结束后，希望学生能够回答下面几个问题：

- AI项目一般包含哪些步骤？ 

- 什么是特征（Feature）？ 

- 为什么需要特征工程？ 

- 什么是训练集和测试集？ 

- 一个模型是如何训练出来的？ 

- 如何评价模型效果？ 

- 如何利用模型进行预测？ 

---

## Day1 AI开发环境与第一个AI项目

### 学习内容

AI工程开发环境

- Python开发环境 

- Conda环境管理 

- VS Code 

- Jupyter Notebook 

- Git与GitHub 

- AI项目目录规范 

AI项目开发流程

- 数据采集（Data） 

- 特征工程（Feature Engineering） 

- 模型训练（Training） 

- 模型评估（Evaluation） 

- 推理预测（Inference） 

### 实践内容

搭建课程开发环境。

创建课程项目：

```Plain Text
AI-SummerCamp/

week01/

data/

notebooks/

src/

models/

README.md
```

导入一个简单的数据集（如房价预测或学生成绩预测）。

利用 Pandas 查看数据。

完成第一次数据探索（EDA）。

---

## Day2 特征工程（Feature Engineering）

### 学习内容

Python数据分析基础

- NumPy 

- Pandas 

- DataFrame 

特征工程基础

- 什么是Feature 

- Feature与Label 

- 数据清洗 

- 缺失值处理 

- 类别变量编码 

- 数值归一化 

- 特征选择（初步认识） 

### 实践内容

使用一个公开数据集完成：

- 数据读取 

- 数据清洗 

- 数据统计 

- 特征提取 

- 特征可视化 

输出：

```Plain Text
clean_dataset.csv
```

---

## Day3 第一个机器学习模型——线性回归

### 学习内容

AI模型开发流程

- 什么是监督学习 

- 什么是线性回归 

- 训练集与测试集 

- 模型训练 

- 模型预测 

Python工具

- scikit\-learn 

- train\_test\_split 

- LinearRegression 

### 实践内容

完成：

房价预测（或学生成绩预测）

完整流程：

```Plain Text
数据

↓

特征工程

↓

划分训练集

↓

训练模型

↓

预测结果
```

输出：

```Plain Text
linear_regression.ipynb
```

---

## Day4 模型评估与结果可视化

### 学习内容

模型评估

- MSE 

- RMSE 

- MAE 

- R² Score 

Matplotlib基础

模型效果分析

如何理解：

- 过拟合 

- 欠拟合（感性认识） 

- 残差分析 

### 实践内容

绘制：

- 散点图 

- 回归直线 

- Prediction vs Ground Truth 

- Residual Plot 

输出：

完整实验报告。

---

## Day5 Mini Project

### 项目名称

> **My First AI Project —— House Price Prediction**
> 
> 

### 项目目标

独立完成一个完整的小型AI项目。

项目流程：

```Plain Text
读取数据

↓

EDA

↓

Feature Engineering

↓

Train/Test Split

↓

Linear Regression

↓

Evaluation

↓

Prediction

↓

Visualization
```

### 项目成果

完成一个完整的GitHub工程：

```Plain Text
week01_house_price/

│

├── data/

├── notebook/

├── src/

├── figures/

├── models/

├── README.md

└── requirements.txt
```

README中需要说明：

- 项目背景 

- 数据来源 

- 特征工程过程 

- 模型训练流程 

- 模型评估结果 

- 改进思路 

---

## 第一周学习成果（Milestone）

完成第一周后，学生应具备以下能力：

# 第二周 PyTorch深度学习实践

## 课程主题

**从线性回归到神经网络——完成第一个图像识别AI项目**

---

## 本周目标

利用 **PyTorch** 独立完成一个基于 **MNIST 手写数字数据集** 的图像分类项目，理解深度学习项目的完整开发流程。

本周结束后，希望学生能够回答下面几个问题：

- 为什么深度学习要使用Tensor？ 

- PyTorch中的Dataset和DataLoader有什么作用？ 

- 神经网络是如何搭建和训练的？ 

- Loss和Optimizer分别负责什么？ 

- 一个分类模型如何进行预测？ 

- CNN相比MLP解决了什么问题？ 

---

## Day1 PyTorch基础与Tensor

### 学习内容

PyTorch简介

- PyTorch生态介绍 

- Tensor基础 

- Tensor与NumPy转换 

- Tensor运算 

- GPU基本使用 

自动求导（Autograd）

- Computational Graph 

- requires\_grad 

- backward\(\) 

- optimizer\.step\(\) 

理解PyTorch训练流程：

```Plain Text
Dataset

↓

DataLoader

↓

Model

↓

Loss

↓

Optimizer

↓

Train

↓

Evaluate
```

### 实践内容

完成：

- Tensor基本操作 

- GPU运行测试 

- 自动求导实验 

- 使用PyTorch重新实现第一周的线性回归 

---

## Day2 MNIST数据集与数据加载

### 学习内容

PyTorch数据处理

- torchvision简介 

- MNIST数据集 

- Dataset 

- DataLoader 

- Batch 

- Shuffle 

理解：

为什么深度学习需要Batch训练？

数据增强（初步认识）

- Transform 

- Normalize 

- ToTensor 

### 实践内容

完成：

加载MNIST数据集

实现：

- Dataset 

- DataLoader 

- 数据可视化 

显示多个MNIST数字样本。

---

## Day3 使用MLP实现手写数字识别

### 学习内容

神经网络基础

- nn\.Module 

- Linear Layer 

- ReLU 

- Forward\(\) 

模型训练

- CrossEntropyLoss 

- Optimizer 

- Epoch 

- Accuracy 

理解：

神经网络为什么比线性回归更强？

### 实践内容

实现：

MNIST MLP分类器。

完成：

```Plain Text
输入图片

↓

Flatten

↓

MLP

↓

Softmax

↓

预测数字
```

训练第一个图像分类模型。

---

## Day4 模型训练、评估与预测

### 学习内容

训练流程完善

- Train Loop 

- Validation 

- Accuracy 

- Loss Curve 

- 模型保存（Save） 

- 模型加载（Load） 

模型预测

- 单张图片预测 

- 批量预测 

结果分析

- 分类正确 

- 分类错误 

- 错误原因分析 

### 实践内容

完成完整训练流程：

- 模型训练 

- 保存模型 

- 加载模型 

- 测试模型 

- 可视化预测结果 

输出：

训练日志

Loss曲线

Accuracy曲线

预测图片展示

---

## Day5 CNN初步认识与Mini Project

### 第一部分：CNN概念介绍

学习内容

为什么需要CNN？

介绍以下核心概念（建立直观认识即可，不做数学推导）：

- 图像为什么不能直接全部Flatten？ 

- 卷积（Convolution）的基本思想 

- 卷积核（Kernel） 

- 特征图（Feature Map） 

- 池化（Pooling） 

- CNN在图像识别中的优势 

重点理解：

> CNN并不是一种新的AI，而是一种更适合处理图像数据的神经网络结构。
> 
> 

### 第二部分：运行CNN Sample

实践内容

运行一个官方或课程提供的CNN示例代码：

```Plain Text
MNIST

↓

CNN

↓

Train

↓

Evaluate
```

观察：

- 网络结构 

- Loss变化 

- Accuracy变化 

对比：

MLP vs CNN

重点讨论：

为什么CNN效果更好？

但本周**不要求学生自己编写CNN代码**，重点是理解网络结构和训练流程。

---

### Mini Project

完成项目：

> **MNIST Image Classifier（MLP）**
> 
> 

---

### 项目要求

完成一个完整的GitHub工程：

```Plain Text
week02_mnist_classifier/

│

├── data/

├── models/

├── notebook/

├── src/

│   ├── dataset.py

│   ├── model.py

│   ├── train.py

│   ├── predict.py

│   └── utils.py

├── figures/

├── checkpoints/

├── requirements.txt

└── README.md
```

项目功能要求：

- 自动下载MNIST数据集 

- 使用MLP进行训练 

- 输出训练Loss和Accuracy 

- 保存训练好的模型 

- 加载模型进行预测 

- 展示预测结果 

- 绘制训练曲线 

- GitHub提交完整工程 

README需要包含：

- 项目背景 

- 数据集介绍 

- 网络结构说明（MLP） 

- 训练过程 

- 实验结果 

- 对MLP和CNN的简单对比 

- 下一步可以如何改进（例如使用CNN） 

---

## 第二周学习成果（Milestone）

完成第二周后，学生应具备以下能力：

# 第三周 大语言模型应用开发

## 课程主题

**开发第一个LLM应用**

### Day1 Prompt Engineering

学习内容

- Prompt设计 

- Few\-shot 

- Chain of Thought 

- Prompt调优 

实践

优化多个Prompt案例。

---

### Day2 Transformers与Hugging Face

学习内容

- Transformers 

- Hugging Face 

- Tokenizer 

- Pipeline 

实践

运行开源模型。

---

### Day3 LLM API开发

学习内容

- OpenAI兼容API 

- DeepSeek API调用 

- 流式输出 

实践

开发命令行聊天助手。

---

### Day4 LangChain基础

学习内容

- PromptTemplate 

- Chain 

- Output Parser 

实践

构建简单LLM应用。

---

### Day5 Mini Project

完成：

> **AI Chat Assistant**
> 
> 

项目要求：

- 支持连续对话 

- 支持Prompt模板 

- 支持历史记录 

- GitHub提交



# 第四周 Agent \+ RAG开发

## 课程主题

**构建具有知识库能力的AI助手**

### Day1 Embedding与向量检索

学习内容

- Embedding 

- Chunk 

- Retrieval 

实践

建立文本向量数据库。

---

### Day2 RAG开发

学习内容

- PDF解析 

- 文本切分 

- 向量索引 

实践

开发PDF问答系统。

---

### Day3 LangChain Agent

学习内容

- Tool 

- Agent 

- Function Calling 

实践

构建多工具Agent。

---

### Day4 MCP初体验

学习内容

- MCP基本概念 

- MCP Server 

- MCP Client 

- 工具调用 

实践

连接本地工具。

---

### Day5 Mini Project

完成：

> **PCB Knowledge Assistant**
> 
> 

项目要求：

- 导入PCB相关PDF 

- 支持知识问答 

- 支持RAG检索 

- GitHub提交 

---

# 第五周 KiCad入门与强化学习实践

## 课程主题

**了解PCB设计流程，体验强化学习在EDA中的应用**

### Day1 KiCad安装与PCB设计流程

学习内容

- KiCad 8\.0 安装 

- PCB设计基本流程 

- 原理图（Schematic） 

- PCB Layout 

- Gerber文件 

实践内容

跟随 **B站或YouTube《1小时KiCad入门教程》** 完成环境配置。

---

### Day2 第一个PCB设计

实践内容

完成：

**5V → 3\.3V 电源转换板**

要求：

- 绘制原理图 

- 放置元器件 

- 完成PCB布局 

- 布线 

- DRC检查 

---

### Day3 PCB制造文件生成

学习内容

- Gerber文件 

- Drill文件 

- 制造输出 

实践内容

导出完整Gerber文件，并使用Gerber Viewer进行检查。

---

### Day4 强化学习PCB布局项目

学习内容

了解强化学习在EDA中的应用。

实践内容

Clone开源项目：

**rl\_pcb**

主要任务：

- 配置Python环境 

- 安装依赖 

- 阅读项目结构 

- 理解训练流程 

---

### Day5 Mini Project

完成：

> **PCB Component Placement Demo**
> 
> 

项目要求

- 成功运行 rl\_pcb Demo 

- 阅读项目README 

- 梳理项目架构 

- 总结强化学习在PCB布局中的基本思路 

- 输出一份技术学习报告 

---

# 第六周 AI Coding实践

## 课程主题

**让AI成为你的Pair Programmer**

### Day1 AI Coding工作流

学习内容

- AI Coding理念 

- Opencode简介 

- DeepSeek Coding能力 

- Prompt for Coding 

实践内容

利用AI生成完整Python项目。

---

### Day2 Opencode实践

学习内容

- Project Context 

- Agent模式 

- 多文件开发 

- AI代码修改 

实践内容

利用Opencode完成一个工具开发。

---

### Day3 DeepSeek协同开发

学习内容

- AI代码生成 

- AI代码解释 

- AI代码重构 

- 自动生成文档 

实践内容

完成一个完整Python模块。

---

### Day4 AI Debugging

学习内容

- Bug定位 

- 错误分析 

- Prompt优化 

- Refactoring 

- 单元测试生成 

实践内容

利用AI修复多个真实Bug。

---

### Day5 Mini Project

完成：

> **AI Coding Workflow**
> 
> 

项目要求：

- 使用AI完成一个完整的小型应用 

- 保留Prompt记录 

- 编写README 

- 输出开发总结 

---

# 第七周 项目优化与成果展示

## 课程主题

**从Demo到可展示项目——完成AI工程项目的最终交付**

---

## 本周目标

综合运用前六周所学知识，对课程项目进行完善、优化和工程化整理，完成一个能够展示、汇报和持续迭代的AI项目。

本周结束后，希望学生能够具备：

- AI项目工程化组织能力 

- GitHub项目管理能力 

- AI Coding协同开发能力 

- 技术文档编写能力 

- 项目汇报能力 

- Demo展示能力 

---

## Day1 项目功能完善

## 学习内容

项目功能检查

- 功能完整性 

- Bug修复 

- 用户体验优化 

- 代码整理 

工程规范

- 模块划分 

- 配置文件 

- requirements 

- 项目目录规范 

### 实践内容

完成项目第一次完整运行。

建立最终工程目录。

例如：

```Plain Text
PCB_AI_Project/

│

├── src/

├── models/

├── data/

├── docs/

├── demo/

├── figures/

├── requirements.txt

└── README.md
```

---

## Day2 AI Coding优化项目

## 学习内容

利用 Opencode \+ DeepSeek 进行工程优化。

包括：

- 重构代码 

- 自动补充注释 

- 自动生成README 

- 自动生成测试代码 

- 自动优化函数 

理解：

AI Coding不是重新生成项目。

而是：

> **持续重构（Refactor）**
> 
> 

### 实践内容

完成整个项目第一次代码重构。

---

## Day3 GitHub工程化

## 学习内容

GitHub最佳实践

包括：

- Commit规范 

- Release 

- Issue 

- Branch 

- Pull Request（了解即可） 

项目文档

包括：

- README 

- 使用说明 

- 环境安装 

- 项目结构 

- License 

### 实践内容

整理GitHub仓库。

完成：

README第一版。

---

## Day4 项目展示准备

## 学习内容

如何介绍一个AI项目。

建议按照下面结构：

项目背景

↓

问题分析

↓

技术方案

↓

系统架构

↓

Demo演示

↓

实验结果

↓

总结

学习：

如何制作技术PPT。

如何录制Demo。

### 实践内容

制作：

项目展示PPT。

录制Demo视频。

---

## Day5 Final Demo

## 项目最终展示

每位学生完成：

### 第一部分

项目展示（15分钟）

包括：

- 项目背景 

- 技术方案 

- 系统架构 

- Demo展示 

---

### 第二部分

技术讲解（10分钟）

讲解：

- 为什么这样设计？ 

- 用到了哪些AI技术？ 

- 遇到了哪些问题？ 

- AI Coding帮助了哪些工作？ 

---

### 第三部分

课程总结

总结整个暑假的学习成果。

输出：

未来学习路线。

例如：

- 强化学习 

- 多模态模型 

- AI Agent 

- PCB自动布局 

- AI辅助EDA 

---

## 本周最终项目

完成：

> **Final Demo**
> 
> 

项目应包含以下内容：

## 1\. GitHub工程

```Plain Text
PCB_AI_Project/

├── src/

├── models/

├── data/

├── docs/

├── demo/

├── figures/

├── requirements.txt

├── README.md

└── LICENSE
```

---

## 2\. 项目文档

包括：

- README 

- 安装说明 

- 使用说明 

- 技术架构 

- 后续优化方向 

---

## 3\. 演示材料

包括：

- PPT 

- Demo视频（可选） 

- 演示脚本 

---

## 4\. AI Coding记录

建议保留：

- 关键Prompt 

- AI生成代码示例 

- 人工修改记录 

- Bug修复案例 

- AI辅助重构案例 

形成完整的开发记录。

---

## 第七周学习成果（Milestone）

完成第七周后，学生应具备以下能力：



---

# 后续AI辅助PCB设计技术展望



通过本期暑假AI工程实践训练营的学习，已经基本掌握了AI编程实践的基础。然而，要跨入“AI辅助PCB设计”这一前沿交叉研究领域，面临的挑战不仅是AI算法本身，还有**硬件/电路领域的知识**以及**如何将复杂的物理、几何约束转化为AI可解的数学模型**。以下是**两年期（大三至大四毕业）的学习与科研路径规划**，帮助跨入该领域并达到学术研究水平：

---

## 第一阶段：Domain Bridge \& 基础内功



**核心目标**：跨越计算机与电子工程（EE）的学科鸿沟，攻克“优化理论”基础。



#### 1\. 硬件与PCB领域知识补齐（零起点）



不需要成为能够手动画复杂板子的硬件工程师，但必须能“读懂”设计。

- **核心概念学习**：理解原理图（Schematic）与PCB版图（Layout）的对应关系；掌握网表（Netlist）、走线（Trace）、过孔（Via）、阻抗（Impedance）以及BGA封装的概念。

- **实操练习**：利用开源的 EDA 软件 **KiCad** 动手绘制一个极其简单的单片机最小系统板，了解从“原理图 $\to$ 生成网表 $\to$ 导入PCB $\to$ 布局布线 $\to$ 生成Gerber制造文件”的完整传统工业流程。

- **网课推荐**：Coursera 上的《PCB CAD Design, DFM, \& DFT Considerations》。

#### 2\. 数学优化理论（重中之重）

AI辅助PCB设计本质上是“约束优化问题”。

- **连续与凸优化**：精读 Stephen Boyd 的《Convex Optimization》（凸优化）。理解如何将几何避障、密度分布转化为连续可微的目标函数。

- **离散与组合优化**：学习混合整数线性规划（MILP）、二部图最大流等算法，这在后续“ Legalization（布局合规化）”中是必不可少的后处理工具。

#### 3\. 跑通第一个开源数据集

- **数据集探索**：在 Hugging Face 上下载并熟悉 **`open-schematics`** 数据库。学习使用 Python 脚本解析 KiCad 格式的原理图（`.kicad_sch`）和网表，提取出图（Graph）结构。

---

## 第二阶段：AI\-PCB 核心算法实操

**核心目标**：掌握图神经网络与强化学习在物理设计（PDA）中的应用。

#### 1\. 图神经网络（GNN）与电路网表

电路本身就是天然的“图”。

- **算法学习**：掌握 PyTorch Geometric \(PyG\) 框架，重点学习 GCN, GAT 架构。

- **实操项目**：尝试利用 GNN 对 `open-schematics` 提取出的电路节点进行分类（例如预测某个元器件是电阻、电容还是IC芯片）。

- **进阶学术目标**：阅读经典论文《Circuit\-GNN: Graph Neural Networks for Distributed Circuit Design》，理解如何利用GNN模拟电磁响应并进行逆向设计。

#### 2\. 深度强化学习（DRL）与寻路摆放

- **算法学习**：理解马尔可夫决策过程（MDP），掌握近端策略优化（PPO）和 SAC 算法。推荐使用 Stable\-Baselines3 框架。

- **实操项目**：在 2D 栅格地图中，利用 PPO 训练一个“走线智能体”，从起点 $A$ 绕过障碍物到达终点 $B$（单线智能布线）。

- **学术参考**：阅读《FanoutNet: A Neuralized PCB Fanout Automation Method Using Deep Reinforcement Learning》，学习如何用强化学习解决高密度芯片的逃逸扇出问题。

#### 3\. EDA 自动化编程

- 熟练掌握 **KiCad Python API**，编写 Python 脚本自动读取 PCB 中器件的引脚坐标，或者通过代码实现自动在版图上放置一个去耦电容。

---

## 第三阶段：多物理场代理模型与生成式AI

**核心目标**：融合大语言模型（LLM）与物理仿真

#### 1\. 物理信息机器学习与代理模型（Surrogate Models）

AI辅助PCB设计最前沿的方向，是用神经网络替代极其耗时的热学、电磁仿真商业软件。

- **物理感知网络**：学习如何构建轻量级的 CNN 或注意力机制网络，以 PCB 走线图像作为输入，毫秒级预测温度分布场。

- **学术经典重现**：复现 CUHK 团队发表在 IEEE TCAD 上的 **`TRouter`** 框架的核心思想 —— 利用神经网络热敏感度梯度反向传播，引导 A\* 算法进行散热布线。

- **高频电磁预测**：阅读关于复数值神经网络（Complex\-valued NNs, 如 CDNet）的研究，了解如何利用代理模型预测高频差分信号的 S 参数。

#### 2\. 大语言模型（LLM）驱动的代码化设计

- **LLM \+ 硬件生成**：硬件描述语言代码化（如 SKiDL）是当前的研究热点。学习利用 LoRA 微调开源大模型（如 Gemma 或 Qwen），使其能够根据自然语言指令生成符合设计规则的 SKiDL 原理图代码。

- **学术前沿**：精读 2026 年最新论文 **`PCBSchemaGen`** 与 **`SchGen`**，学习如何构建基于知识图谱（KG）和子图同构（SI）的“硬约束验证管道”，解决大模型的幻觉问题。

---

## 第四阶段：顶尖学术重现与科研起步

**核心目标**：重现工业级/学术界最顶尖的框架，进行真正的学术创新。

#### 1\. GPU 加速的类 IC 物理布局算法

- **算法重现**：关注并重现 NVIDIA 研究团队在 ISPD 2025 上获得最佳论文奖的 **`Cypress`** 开源框架（GPU加速的凸优化PCB布局算法，基于 DREAMPlace 构建）。

- 运行其开源代码（C\+\+/CUDA/Python 混合编译），理解其损失函数的设计：

    $E = \alpha \cdot \text{Cost}_{\text{wire}} + \beta \cdot \text{Cost}_{\text{density}} + \gamma \cdot \text{Cost}_{\text{overlap}} + \delta \cdot \text{Cost}_{\text{crossing}}$

#### 2\. DFM/DFA 智能校验

- 学习如何将计算机视觉（YOLOv8/Mask R\-CNN）应用于生产制造环节的缺陷检测，了解在线 DFM/DFA 规则校验机制。

    

    

    


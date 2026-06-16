# HSBC Technology Xi'an 面试准备 — AI技术问答整理

> 岗位：顾问专家（Consultant Expert）| Job ID: 33445 | IWPB Technology
> 项目背景：Atom Bank AI Financial Report System（Durham大学校企合作）

---

## 目录

1. [Milvus核心原理和使用流程](#1-milvus核心原理和使用流程)
2. [提示词优化方法](#2-提示词优化方法)
3. [术语理解偏差为什么不用微调](#3-术语理解偏差为什么不用微调)
4. [汇丰场景选什么LLM模型](#4-汇丰场景选什么llm模型)
5. [为什么不用Dify和n8n](#5-为什么不用dify和n8n)
6. [为什么不用AI原生而选LangChain](#6-为什么不用ai原生而选langchain)
7. [Human in the Loop环节](#7-human-in-the-loop环节)
8. [数字计算不能用AI处理](#8-数字计算不能用ai处理)
9. [自动财务报表系统做什么](#9-自动财务报表系统做什么)
10. [AI在银行的其他应用场景](#10-ai在银行的其他应用场景)
11. [Atom Bank背景](#11-atom-bank背景)
12. [FCA和PRA是什么](#12-fca和pra是什么)
13. [中国监管体系](#13-中国监管体系)
14. [工程师面对监管的约束](#14-工程师面对监管的约束)
15. [项目API部署在哪里](#15-项目api部署在哪里)

---

## 1. Milvus核心原理和使用流程

### 核心原理：向量相似度搜索

```
传统数据库：精确匹配   SELECT * WHERE id = 123
Milvus：    相似度搜索  找出语义最相关的内容
```

**向量化过程：**
```
文本："Q3 revenue increased by 15%"
        ↓ Embedding模型
向量：[0.23, -0.15, 0.87, 0.42, ...]（高维数字数组）
```

**距离计算方式：**

| 方式 | 适用场景 |
|---|---|
| 余弦相似度 | 文本语义搜索（最常用）|
| 欧氏距离（L2） | 图像搜索 |
| 内积（IP） | 推荐系统 |

### 核心概念

```
Collection（集合）= Table
Field（字段）= 主键ID + 向量字段 + 标量字段
Index（索引）= HNSW / IVF_FLAT / FLAT
```

### 完整使用流程

```python
# 1. 创建Collection
fields = [
    FieldSchema(name="id", dtype=INT64, is_primary=True),
    FieldSchema(name="text", dtype=VARCHAR, max_length=2000),
    FieldSchema(name="embedding", dtype=FLOAT_VECTOR, dim=384)
]
collection = Collection("financial_reports", schema)

# 2. 插入数据
collection.insert([ids, texts, embeddings])
collection.flush()

# 3. 创建索引
index_params = {"metric_type": "COSINE", "index_type": "HNSW",
                "params": {"M": 16, "efConstruction": 200}}
collection.create_index("embedding", index_params)
collection.load()

# 4. 相似度搜索
results = collection.search(
    data=query_embedding,
    anns_field="embedding",
    param={"metric_type": "COSINE", "ef": 100},
    limit=5,
    output_fields=["text"]
)
```

### 项目中的完整RAG流程

```
CSV数据 → 分块 → Embedding → 存入Milvus
（离线处理）

查询语句 → 向量化 → Milvus相似度搜索
→ Top-K相关数据 + Prompt → Llama 3 8B
→ 生成报告文字 → LangGraph编排输出PDF
```

**面试关键话术：**
> "即使用户问'利润情况怎样'，也能检索到包含'net income'、'revenue'的相关数据，语义理解能力远超传统数据库搜索。"

---

## 2. 提示词优化方法

### 优化技术

**1. Few-shot提示**
```
给模型看输入→输出的例子，固定输出格式
```

**2. Chain of Thought（思维链）**
```
"First, analyze the trend in the data.
 Then, identify key highlights.
 Finally, generate the report section."
```

**3. 输出格式约束**
```
明确指定结构：Executive Summary / Key Metrics / Trend Analysis
```

**4. RAG上下文注入**
```
System: You are a financial analyst...
Context: {retrieved_milvus_data}
User: Generate Q3 report
```

### LangSmith的作用

```
记录每次LLM调用 → 对比不同Prompt版本效果 → 迭代优化
```

### 常见问题和解决方法

| 问题 | 现象 | 解决方法 |
|---|---|---|
| 数字幻觉 | 模型编造财务数字 | 强调"only use data from context" |
| 格式不稳定 | 每次输出结构不同 | Few-shot示例固定格式 |
| 上下文太长 | 超出模型窗口 | 分段处理+摘要 |
| 术语理解偏差 | 财务术语理解错误 | System Prompt中定义术语 |

---

## 3. 术语理解偏差为什么不用微调

### 核心逻辑

```
术语理解偏差的根本原因：
  不是模型"不懂"金融术语（Llama 3训练数据有大量金融文本）
  而是模型不知道Atom Bank内部的特定计算口径
```

### 正确解决方式：领域术语注入

```python
system_prompt = """
The following terms have specific definitions in Atom Bank's context:
- adjustedRevenue: total revenue minus...
- netInterestMargin: calculated as...
"""
```

### 微调 vs Prompt术语注入对比

| | 微调 | Prompt术语注入 |
|---|---|---|
| 解决什么 | 通用能力不足 | 私有定义不一致 |
| 数据需求 | 数千条高质量样本 | 一份术语表 |
| 更新成本 | 重新训练（高） | 改一行文字（低） |
| 可解释性 | 黑盒 | 清晰可审计 |
| 适合本项目 | ❌ | ✅ |

**面试关键话术：**
> "微调改变模型权重，解决的是'模型不懂金融'的问题，但Llama 3本身已经具备足够的金融知识。我们选择在System Prompt里注入术语定义表，当业务规则变更时只需修改Prompt而不需要重新训练模型。"

---

## 4. 汇丰场景选什么LLM模型

### 汇丰 vs Atom Bank差异

```
Atom Bank          汇丰银行
─────────          ──────────
小型数字银行        全球系统重要性银行（G-SIB）
~50MB数据          PB级数据
有限计算资源        充裕IT预算
学校合作项目        生产系统，监管审查
```

### 首选方案：私有化部署大模型

```
Llama 3.1 70B 或 Qwen 2.5 72B
部署在汇丰私有云（AWS GovCloud / Azure Private）
→ 数据不出汇丰网络
→ 满足FCA、PRA、GDPR监管要求
```

**为什么70B而不是8B：**
- 汇丰有充裕GPU资源
- 70B在复杂财务推理准确率显著高于8B
- 对G-SIB银行，算力成本 << 报告错误的合规风险

### 为什么排除直接调用OpenAI/Anthropic API

| 问题 | 原因 |
|---|---|
| 数据主权 | 财务数据发往境外服务器 |
| 监管合规 | FCA明确要求数据控制权 |
| 审计要求 | 模型版本变更不受控 |
| 单点依赖 | API宕机影响生产系统 |

### 完整技术选型

```
模型：     Llama 3.1 70B（私有化部署）
向量库：   Milvus（集群版，生产级）
框架：     LangGraph（多节点编排）
可观测：   LangSmith + 内部日志系统
部署：     AWS/Azure 私有云，数据不出银行网络
合规层：   每次LLM输出必须有原始数据溯源
```

**面试关键话术：**
> "始终在约束条件下寻找最优解，而不是追求技术上最先进的。"

---

## 5. 为什么不用Dify和n8n

### Dify的问题

```
问题1：数据主权 — 云版本数据经过Dify服务器
问题2：黑盒审计 — FCA要求每步可解释，封装层是障碍
问题3：定制化天花板 — 复杂多步骤逻辑超出平台能力
```

### n8n的问题

```
n8n擅长：API调用、数据传递、事件触发（管道工）
n8n不擅长：复杂LLM上下文管理、向量检索编排、多轮推理状态管理
```

### 适用场景对比

| 维度 | Dify/n8n | LangGraph |
|---|---|---|
| 数据控制 | 依赖平台架构 | 完全自控 |
| 审计追溯 | 平台日志，有限 | LangSmith，全链路 |
| 定制能力 | 受限于平台功能 | 无上限 |
| 上线速度 | 快（原型） | 慢（生产） |
| 适合场景 | POC、内部工具 | 银行生产系统 |

**面试关键话术：**
> "用Dify搭了一个两天的POC验证可行性，非常高效。但进入生产阶段，监管机构需要我们能逐行解释系统行为，平台化工具的封装层在这个场景下变成了障碍。工具没有好坏，只有适不适合场景。"

---

## 6. 为什么不用AI原生而选LangChain

### 关键区分：LangChain ≠ LangGraph

```
LangChain：  工具箱（用得很克制）
LangGraph：  状态机编排框架（这是核心选择）

真正的原因是需要LangGraph
```

### LangGraph解决的具体问题

```
财务报表生成是有状态的多步骤流程：
数据检索 → 数据验证 → 章节生成 → 交叉核对 → 汇总
    ↑           |
    └──出错回退──┘

需要：节点间状态传递 / 条件分支 / 循环 / 并行执行
手写状态机 = 几百行胶水代码
LangGraph = 声明式定义，清晰可维护
```

### 工程量对比

| 功能 | AI原生手写 | LangGraph |
|---|---|---|
| Milvus集成 | 自写pymilvus封装 | 直接用集成 |
| 多步骤状态管理 | 手写状态机 | Graph节点声明 |
| 错误重试逻辑 | 手写装饰器 | 内置retry |
| 全链路追踪 | 手写日志系统 | LangSmith直接接入 |
| **总开发时间** | **~3倍** | **基准** |

**面试关键话术：**
> "框架的价值不在于能力，而在于让复杂性显式化。"

---

## 7. Human in the Loop环节

### 为什么必须有

```
AI生成的财务报告不能直接发给监管机构或董事会
金融报告的法律责任在签署人（人），不在AI
FCA要求：财务信息发布有人工审核记录
```

### LangGraph实现方式

```python
# 带checkpointer的持久化状态
checkpointer = SqliteSaver.from_conn_string("reports.db")

graph.add_conditional_edges(
    "human_review",
    check_human_decision,
    {
        "approved": "generate_final",
        "revise": "generate_draft",   # 打回重新生成
        "rejected": END
    }
)
```

### 完整HITL流程

```
AI生成草稿报告
    ↓
【⏸️ 暂停 - 等待人工】LangGraph Checkpointer持久化状态
    ↓
财务分析师审核：数字核对 + 叙述准确性 + 合规措辞
    ↓
批准 → 生成最终PDF + 合规签章记录
修改 → 注入修改意见 → AI重新生成特定章节
拒绝 → 终止流程，人工撰写
```

**面试关键话术：**
> "AI负责效率，人负责最终判断和法律责任。"

---

## 8. 数字计算不能用AI处理

### 核心原则：职责分离

```
LLM 擅长：叙述性文字生成、趋势解读、格式化输出
Python 擅长：精确数值计算、统计分析、数据聚合
绝对不能混用
```

### 推荐实现：预计算节点

```python
def calculation_node(state: ReportState) -> ReportState:
    """纯Python计算，不涉及LLM"""
    df = pd.read_csv(state["data_path"])
    metrics = {
        "q3_revenue": df[df["quarter"]=="Q3"]["revenue"].sum(),
        "yoy_growth": calculate_yoy(df),
        "net_margin": calculate_margin(df),
    }
    return {**state, "verified_metrics": metrics}

def generation_node(state: ReportState) -> ReportState:
    """LLM只负责把数字变成文字"""
    prompt = f"""
    Based on these VERIFIED metrics (do not recalculate):
    {state['verified_metrics']}
    Write the Q3 financial summary narrative.
    """
```

### 数字锁定策略（System Prompt）

```
CRITICAL RULES:
1. NEVER recalculate any numbers yourself
2. Use ONLY the exact figures provided in the context
3. If a metric is not in the provided data, say "data not available"
```

### 职责划分总表

| 工作 | 由谁做 | 工具 |
|---|---|---|
| 数据清洗 | Python | pandas |
| 指标计算 | Python | numpy/pandas |
| 数据验证 | Python | 断言/单元测试 |
| 趋势叙述 | LLM | Llama 3 |
| 报告措辞 | LLM | Llama 3 |
| 格式排版 | Python | ReportLab/WeasyPrint |

**面试关键话术：**
> "LLM的价值在于理解和表达，不在于算术。"

---

## 9. 自动财务报表系统做什么

### 一句话描述

> 把Atom Bank一年的历史财务CSV数据，自动生成结构化的季度/年度财务分析报告PDF，替代人工从数据到报告的全流程。

### 输入和输出

```
输入：Atom Bank历史财务数据（~50MB CSV）
  ├── 收入流水（按产品线、时间段）
  ├── 成本支出
  ├── 贷款/存款数据
  └── 用户增长指标

输出：PDF报告
  ├── Executive Summary
  ├── 关键指标仪表盘（营收、净利润、增长率）
  ├── 趋势分析（同比/环比）
  ├── 分业务线表现
  ├── 风险提示
  └── 下季度展望
```

### 解决的核心痛点

```
传统方式：财务团队手工处理 → 2-3天/份报告
自动化后：触发生成 → 20-30分钟/份报告
          人工只需最终审核
```

### 30秒项目介绍（标准STAR结构）

> "这是我在杜伦大学硕士阶段和Atom Bank合作的项目。Atom Bank每次生成分析报告都需要财务团队花2-3天手工处理。我们用LangGraph编排多步骤Agent，结合Milvus向量检索和Llama 3本地部署，实现了从原始CSV数据到结构化PDF报告的自动化。报告生成时间从几天缩短到30分钟以内，同时保留了Human in the Loop的人工审核环节，确保数字准确性和合规性。"

---

## 10. AI在银行的其他应用场景

### 按风险等级分层

```
低风险（AI可以直接决策）：内部报告、文件处理、代码辅助
中风险（AI辅助，人工确认）：贷款初审、异常交易预警
高风险（AI仅提供参考）：信贷最终审批、投资建议
```

### 主要场景

| 场景 | AI应用 | 与你背景的连接 |
|---|---|---|
| 智能客服 | RAG + 产品知识库 | — |
| 贷款风控 | OCR + 信用评分辅助 | 县域贷款平台背景 |
| 跨境支付 | 异常交易检测、AML | 马来西亚支付项目背景 |
| 合规文件审查 | 合同风险标记 | — |
| 代码生成 | GitHub Copilot、COBOL迁移 | 直接相关于HSBC岗位 |
| 财务报告 | RAG + LLM生成 | 你的项目 |

### 不适合AI的场景（说这个更加分）

```
❌ 利率决策        → 货币政策，监管敏感
❌ 个人信贷最终审批 → 法律责任问题
❌ 投资建议对外发布 → 金融牌照限制
❌ 反洗钱最终判定  → 司法证据链要求
```

**面试关键话术：**
> "AI的边界不是技术边界，而是责任边界。"

---

## 11. Atom Bank背景

### 基本信息

```
全称：   Atom Bank plc
成立：   2013年，英国达勒姆（Durham）
性质：   英国首家纯App银行（无实体网点）
监管：   FCA + PRA 双重监管
牌照：   2015年获得英国银行牌照
总部：   Durham，英格兰东北部
```

### 关键数据

```
员工规模：  ~500人
用户规模：  约20万+活跃用户
主要股东：  BBVA曾持股~39%（2021年撤资）
盈利状态：  2023年宣布实现盈利
```

### 主要产品

| 产品 | 说明 |
|---|---|
| 固定储蓄账户 | 高利率定期存款 |
| 住房抵押贷款 | App全程申请 |
| 企业贷款 | 中小企业融资 |

### 与Durham大学的关系

```
Atom Bank总部在Durham市中心
Durham University也在Durham
→ 天然的校企合作关系
→ 数据科学/AI研究方向契合
```

**面试关键话术：**
> "虽然规模不及传统大行，但作为受监管的持牌银行，数据安全和合规要求和大型银行是同一标准，这也是我们选择本地部署而不是调用外部API的核心原因。"

---

## 12. FCA和PRA是什么

### 一句话区别

```
FCA：管"行为"  →  你怎么对待客户
PRA：管"安全"  →  你的钱够不够，会不会倒闭
```

### 机构关系

```
英格兰银行（Bank of England）
        ├── PRA（子机构）：关注银行会不会倒
FCA（独立机构）：            关注银行会不会坑人
```

### 对AI系统的实际影响

| 监管要求 | 对AI系统的影响 |
|---|---|
| FCA：可解释性 | AI决策必须能向客户解释 |
| FCA：数据公平性 | 模型不能对某类人群产生歧视 |
| FCA：客户数据保护 | 数据不能发往外部API |
| PRA：审计追踪 | 每个财务数字必须有原始数据溯源 |
| PRA：模型风险管理 | AI模型需要验证、文档、定期审查 |

---

## 13. 中国监管体系

### 现行架构（2023年改革后）

```
国务院
  ├── 中国人民银行（PBOC）— 货币政策 + 金融稳定
  ├── 国家金融监督管理总局（NFRA）— 银行 + 保险 + 信托
  └── 中国证监会（CSRC）— 证券 + 期货 + 基金
```

### 中英对比

```
英国（双峰模式）              中国（分业监管模式）
─────────────────           ──────────────────
按"目标"分工                 按"行业"分工
FCA → 管行为（所有机构）      PBOC → 货币+稳定
PRA → 管安全（银行+保险）     NFRA → 银行+保险
                             CSRC → 证券+基金
```

### 汇丰的特殊性

```
全球系统重要性银行（G-SIB）
同时受多个国家监管：
  英国：FCA + PRA
  中国：NFRA + PBOC
  美国：OCC + Federal Reserve
  香港：HKMA
  欧盟：ECB
→ 合规成本极高，AI系统必须满足多司法管辖区要求
```

---

## 14. 工程师面对监管的约束

### 核心理念

> 互联网工程师："Move fast and break things"
> 银行工程师："Move carefully and document everything"

### 数据约束

```
❌ 不能把生产数据导入开发环境调试
❌ 不能用真实客户数据跑实验
❌ AI模型不能调用外部API（数据出境）
✅ 生产/测试/开发 三环境严格隔离
✅ 测试数据必须脱敏
✅ 数据访问日志全量留存
```

### 变更约束

```
互联网：写代码 → 测试 → 上线（可能一天十几次）

银行：需求评审 → 开发 → 单测 → 代码审查
    → UAT → 变更委员会审批 → 变更窗口（周末凌晨）
    → 上线 → 回滚方案就绪
    一个变更可能需要2-4周
```

### AI模型专项约束（MRM框架）

```
开发阶段：模型文档 + 训练数据来源记录 + 偏见测试
上线前：  独立验证团队审查 + 压力测试
上线后：  定期性能监控 + 模型漂移检测 + 异常告警
```

### 审计约束

```
所有操作必须留痕：
  - 谁访问了什么数据（时间戳+用户ID）
  - AI模型每次输入输出
  - 人工审核决策记录
  
保留期限：英国FCA要求最低5-7年
工程实现：不可删除的审计日志，日志防篡改
```

### 可解释性约束（AI专项）

```
FCA Consumer Duty要求：
  ✅ 每个AI输出必须有依据（RAG的溯源）
  ✅ 不能出现"模型说的，不知道为什么"
  ✅ 高风险决策必须人工可覆盖
  ✅ 保存"AI建议 vs 人工最终决策"的差异记录
```

**面试关键话术：**
> "合规不是事后检查，而是架构的第一输入。"

---

## 15. 项目API部署在哪里

### 说明

项目为Durham大学校企合作研究项目，重点在架构设计和技术验证。

### 设计中的部署架构（AWS，结合SAP认证背景）

```
外部请求
    ↓
API Gateway（鉴权、限流）
    ↓
应用服务（LangGraph Agent）  ← ECS / Lambda
    ↓
    ├── Milvus集群（向量检索）← EC2
    ├── Llama 3（本地GPU推理）← EC2 GPU实例
    └── PostgreSQL（审计日志）
    
全部在VPC内网
数据不出网络边界
S3存储 + KMS加密
CloudWatch + LangSmith监控
```

**面试关键话术：**
> "这是校企合作的研究项目，目前部署在开发环境用于演示和验证。我们在架构设计上完全按照生产级标准来做——考虑了数据主权、审计追踪和Human in the Loop，为未来生产部署做好了准备。"

---

## 核心面试金句汇总

| 场景 | 话术 |
|---|---|
| 技术选型 | "始终在约束条件下寻找最优解，而不是追求技术上最先进的" |
| AI边界 | "AI的边界不是技术边界，而是责任边界" |
| Human in Loop | "AI负责效率，人负责最终判断和法律责任" |
| 数字处理 | "LLM的价值在于理解和表达，不在于算术" |
| 合规设计 | "合规不是事后检查，而是架构的第一输入" |
| 框架选择 | "框架的价值不在于能力，而在于让复杂性显式化" |
| 工具选型 | "工具没有好坏，只有适不适合场景" |
| 微调决策 | "AI负责效率，人负责最终判断和法律责任" |

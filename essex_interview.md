# Job Description: Full Stack Developer (AI Agent Focus)

**Location:** Xi'an, China  
**Tags:** Java · LLM API · LangGraph · AutoGen · CrewAI · LangChain · Python

---

## Job Description

We are looking for a Full Stack Developer with strong AI Agent development capabilities to build innovative intelligent solutions for the finance industry. If you are passionate about cutting-edge AI technologies—including autonomous agents, multi-agent orchestration, and LLM-powered applications—this role is your opportunity to make a real impact.

---

## Responsibilities

- Design, develop, and deploy AI Agent systems using frameworks such as LangChain, LangGraph, AutoGen, CrewAI, or similar.
- Build multi-agent orchestration pipelines, including agent planning, tool-calling, memory management, and autonomous task execution.
- Implement RAG (Retrieval-Augmented Generation) pipelines with vector databases (e.g., Chroma, Pinecone, Weaviate, Milvus) for knowledge-augmented agents.
- Develop and optimize Prompt Engineering strategies, including chain-of-thought, few-shot, and structured output prompting for agent reliability.
- Integrate external tools and APIs into agent workflows (e.g., web search, code execution, database querying, financial data APIs).
- Evaluate and improve agent performance, robustness, and safety in production environments.
- Develop front-end and back-end applications for web/mobile architecture.
- Collaborate to translate deployment, infrastructure, and maintenance requirements into technical solutions.

---

## Requirements

- Bachelor's degree or above in computer science or a related field.
- Proficient in at least one of: Python, Java, or JavaScript; Python strongly preferred for AI/agent work.
- Hands-on experience building AI Agent systems using LangChain, LangGraph, AutoGen, CrewAI, or equivalent frameworks.
- Proficient in Prompt Engineering: chain-of-thought reasoning, structured outputs, tool-use prompting, and agent instruction design.
- Strong understanding of RAG architectures and practical experience with vector databases (Chroma, Pinecone, Milvus, etc.).
- Familiarity with LLM APIs (OpenAI, Claude, Qwen, etc.) and experience deploying LLM-powered applications in production.
- Understanding of agent memory systems, tool-calling patterns, function-calling APIs, and multi-step reasoning workflows.
- Fluent in English with strong written and verbal communication skills.

---

# 面试题库（100题）

> 基于候选人技术背景（MCP Server / LangChain RAG / ChromaDB / Cross-Encoder / HuggingFace）与 JD 要求对照设计

---

## 一、RAG 与向量数据库（20题）

1. 请解释 RAG 的完整工作流程，从用户输入到最终输出经历哪些步骤？
2. 你在项目中使用了 `all-MiniLM-L6-v2` 作为 Embedding 模型，为什么选它？它有什么局限性？
3. 向量相似度检索中，余弦相似度和欧氏距离的区别是什么？什么场景下各自更适合？
4. 你的 MCP Server 中先用向量召回 k=6，再用 Cross-Encoder 精排到 top-2，为什么不直接用 Cross-Encoder 检索全量数据？
5. Cross-Encoder 和 Bi-Encoder 的本质区别是什么？各自适合哪个阶段？
6. Chroma、Pinecone、Weaviate、Milvus 这四个向量数据库各有什么优缺点？生产环境你会怎么选？
7. 如何评估一个 RAG 系统的检索质量？你会用哪些指标（Recall@K、MRR、NDCG等）？
8. Chunk 分割策略对 RAG 效果有什么影响？你如何决定 chunk size 和 overlap？
9. 当用户的问题和文档语言不一致（比如中文问题查英文文档）时，RAG 如何处理？
10. 什么是 Hybrid Search（混合检索）？如何结合 BM25 和向量检索？
11. RAG 中的"幻觉"问题如何缓解？有哪些技术手段？
12. 什么是 Re-ranking？除了 Cross-Encoder，还有哪些精排方案？
13. 如何处理长文档（超过 LLM context window）的 RAG 场景？
14. 什么是 HyDE（假设文档嵌入）？它能解决什么问题？
15. 你如何对 RAG Pipeline 进行端到端的测试和评估？用过 RAGAS 吗？
16. 如果检索结果质量差，你会从哪些维度排查问题？
17. 向量数据库中的 metadata filter 有什么用？结合你的项目说明。
18. Embedding 模型的维度对检索效果和性能有什么影响？
19. 什么是 Multi-vector Retrieval？和普通单向量检索有何不同？
20. 生产环境下向量数据库的索引更新策略是什么？如何做增量更新？

---

## 二、LangChain 与 Agent 框架（20题）

21. LangChain 中 Chain 和 Agent 的核心区别是什么？
22. 你用 LangChain 搭建过哪些类型的 Agent？ReAct 模式是如何工作的？
23. LangChain 中 Tool 的定义方式有哪些？你的 MCP Server 里如何暴露工具给 Agent？
24. LangChain 的 Memory 有哪几种类型？`ConversationBufferMemory` 和 `ConversationSummaryMemory` 分别适合什么场景？
25. 什么是 LCEL（LangChain Expression Language）？它相比传统 Chain 有什么优势？
26. LangChain 中如何实现流式输出（Streaming）？
27. 当 Agent 调用工具返回错误时，你如何设计错误处理和重试逻辑？
28. LangGraph 和 LangChain Agent 的区别是什么？什么场景下需要用 LangGraph？
29. LangGraph 中 State、Node、Edge 分别代表什么概念？
30. 如何在 LangGraph 中实现条件分支（Conditional Edges）？举一个金融业务的例子。
31. 什么是 Human-in-the-Loop？在 LangGraph 中如何实现？
32. AutoGen 的多 Agent 对话模式和 LangChain Agent 有什么本质不同？
33. CrewAI 中 Agent、Task、Crew 三个概念分别是什么？如何协作？
34. 在多 Agent 系统中，如何防止 Agent 之间的循环调用和死锁？
35. Agent 规划（Planning）有哪些策略？ReAct、ToT（Tree of Thought）、CoT 的区别？
36. 如何给 Agent 添加长期记忆（Long-term Memory）？你会用什么方案存储？
37. LangChain 中的 `AgentExecutor` 有哪些关键参数？`max_iterations` 如何设置？
38. 什么是 Tool Calling（Function Calling）？和传统 ReAct 相比有什么优势？
39. 如何评估一个 Agent 系统的性能和可靠性？
40. 如果让你用 LangGraph 实现 EARS™ 的 Anomalix 异常检测 Agent，你会怎么设计？

---

## 三、MCP 与工具集成（10题）

41. 什么是 MCP（Model Context Protocol）？它解决了什么问题？
42. 你的 MCP Server 使用 stdio transport，还有哪些 transport 方式？各自适合什么场景？
43. FastMCP 中 `@mcp.tool()` 装饰器的工作原理是什么？
44. MCP Server 如何被 Claude Desktop / VS Code Copilot 发现和调用？
45. 你的 `calculate` 工具用了 `eval()`，如何防止代码注入攻击？
46. 如何给 MCP Tool 添加参数校验和错误处理？
47. MCP 和 OpenAI Function Calling 的区别与联系是什么？
48. 如何在生产环境中部署 MCP Server？如何做认证和授权？
49. 如果要给 EARS™ 平台集成外部金融数据 API（如 Wind、Bloomberg），你会怎么设计 MCP Tool？
50. 如何测试 MCP Server 的工具调用是否符合预期？

---

## 四、Prompt Engineering（10题）

51. 什么是 Chain-of-Thought（CoT）Prompting？在金融分析场景中如何应用？
52. Few-shot 和 Zero-shot Prompting 各自的优缺点是什么？
53. 如何设计一个结构化输出的 Prompt，让 LLM 稳定返回 JSON 格式？
54. 什么是 System Prompt？如何用它控制 Agent 的行为边界？
55. Prompt 注入攻击（Prompt Injection）是什么？如何防范？
56. 如何通过 Prompt 让 LLM 在不确定时说"我不知道"而不是乱编？
57. 什么是 ReAct Prompt 格式？Thought / Action / Observation 各代表什么？
58. 如何对 Prompt 做版本管理和 A/B 测试？
59. 在多轮对话中，如何设计 Prompt 保持上下文连贯性？
60. LLM 的 Temperature 和 Top-P 参数如何影响输出？金融场景下应该怎么设置？

---

## 五、LLM API 与模型（10题）

61. OpenAI、Claude、Qwen 三个 LLM 在能力和适用场景上有什么区别？
62. 什么是 Token？如何估算一段文本的 Token 数？这对成本有什么影响？
63. Function Calling 和普通文本生成在 API 调用上有什么不同？
64. 如何处理 LLM API 的速率限制（Rate Limit）和超时问题？
65. 什么是 LLM 的 Context Window？超出限制时如何处理长文本？
66. Embedding API 和 Chat Completion API 的区别是什么？
67. 如何在本地部署开源 LLM（如 Qwen、LLaMA）？用过 Ollama 或 vLLM 吗？
68. 什么是 Fine-tuning？它和 RAG 各自适合解决什么问题？
69. 如何监控和记录 LLM API 的调用成本和延迟？
70. 在金融合规场景下，使用 LLM 需要注意哪些数据安全问题？

---

## 六、生产部署与系统设计（10题）

71. 如何评估 AI Agent 系统在生产环境中的稳定性和可靠性？
72. 什么是 LLM Observability？你会用哪些工具（LangSmith、LangFuse等）来做监控？
73. 如何给 RAG + Agent 系统设计缓存层来降低延迟和成本？
74. 当 Agent 在生产环境出现不可预期行为时，你如何定位和修复问题？
75. 如何为 AI Agent 系统设计 Fallback（降级）策略？
76. 描述一个你认为好的 AI Agent 系统架构，需要包含哪些组件？
77. 如何对 AI 系统做 A/B 测试？评估指标如何设计？
78. 在微服务架构中，如何将 LangChain Agent 作为一个服务暴露？
79. 如何处理 Agent 的并发请求？有什么线程安全问题需要注意？
80. 如果要将你的 MCP Server 从本地环境迁移到云端，你会怎么做？

---

## 七、金融业务与领域知识（10题）

81. 你了解哪些金融数据指标（KPI）？比如 NPL ratio（不良贷款率）是什么？
82. 什么是风控模型？AI Agent 在信用风险管理中能发挥什么作用？
83. 金融行业对数据合规有哪些要求？RAG 系统如何满足这些要求？
84. 如果让你给一家银行设计一个 AI Agent 来监控异常交易，你会怎么思考？
85. 什么是 Single Source of Truth（数据单一可信源）？在金融系统中为什么重要？
86. 你如何向非技术的金融业务人员解释 RAG 和 AI Agent 是什么？
87. 金融报表数据通常是结构化表格，如何让 LLM 更好地理解和分析？
88. 什么是 Text-to-SQL？在金融数据查询场景中如何应用？
89. AI Agent 在财富管理（Wealth Management）场景中能做哪些事情？
90. 如何确保 AI Agent 给出的金融建议不产生合规风险？

---

## 八、行为面试与综合能力（10题）

91. 介绍一下你做过的最有挑战性的 AI 项目，遇到了什么问题，如何解决的？
92. 你的 MCP Server 中用了两阶段检索（召回+精排），为什么这样设计？有没有考虑过其他方案？
93. 如果让你在两周内独立搭建一个金融数据 RAG 问答系统，你会怎么规划？
94. 你如何保持对 AI 领域最新技术的关注和学习？
95. 描述一次你发现并修复了一个 AI 系统 Bug 的经历。
96. 如果团队成员对某个技术方案有强烈异议，你怎么处理？
97. 你认为 LangChain、LangGraph、AutoGen 未来哪个会成为主流？为什么？
98. 如果加入 Essex，你希望在第一个月、第三个月、第六个月分别达成什么目标？
99. 你认为 AI Agent 目前最大的局限性是什么？未来如何突破？
100. 用英文介绍你的技术背景和对这个职位的理解（考察英文沟通能力）。

---

# 参考答案

---

## 一、RAG 与向量数据库

**Q1. RAG 的完整工作流程？**
用户输入 → Embedding 向量化 → 向量数据库相似度检索（Retrieval）→ 将检索结果拼入 Prompt（Augmentation）→ LLM 生成回答（Generation）。核心价值是让 LLM 基于私有/实时数据回答，解决训练截止日期和数据安全问题。

**Q2. 为什么选 all-MiniLM-L6-v2？局限性？**
优点：384维、轻量、速度快、可本地运行、无需 API 费用，适合原型和中小规模应用。局限：英文优化，中文效果较弱；维度较低，语义表达能力不如 text-embedding-ada-002；最大输入 256 tokens，长文本需截断。

**Q3. 余弦相似度 vs 欧氏距离？**
余弦相似度衡量向量方向（角度），不受向量长度影响，适合文本语义相似度；欧氏距离衡量绝对距离，受向量幅度影响。文本 Embedding 场景通常用余弦相似度，图像特征匹配有时用欧氏距离。

**Q4. 为什么两阶段：向量召回 k=6 再精排到 top-2？**
Cross-Encoder 需要对每对（query, doc）独立编码，计算成本是 O(n)，无法对全量数据实时计算。先用向量检索快速召回候选集（毫秒级），再用 Cross-Encoder 对少量候选精排（高精度），是速度和精度的最优平衡。

**Q5. Cross-Encoder vs Bi-Encoder？**
Bi-Encoder（双塔）将 query 和 doc 分别编码为独立向量，可离线预计算 doc 向量，检索速度 O(1)，精度略低。Cross-Encoder 将 query+doc 拼接后一起编码，能捕捉交互特征，精度高但无法预计算，速度慢。实际场景：召回用 Bi-Encoder，精排用 Cross-Encoder。

**Q6. 四个向量数据库如何选？**
- Chroma：开源轻量，适合本地开发和原型，不适合大规模生产
- Pinecone：全托管云服务，生产首选，高可用，按用量付费
- Weaviate：开源，支持混合检索（向量+BM25），适合需要关键字+语义联合搜索
- Milvus：开源高性能，适合超大规模（亿级向量），需要自己运维
生产推荐：小团队用 Pinecone，大规模自建用 Milvus。

**Q7. 如何评估 RAG 检索质量？**
- Recall@K：相关文档是否在 top-K 结果中
- MRR（Mean Reciprocal Rank）：第一个相关结果的排名
- NDCG：考虑位置权重的排序质量
- Context Precision/Recall（RAGAS框架）：检索结果和标准答案的重叠度
实践中可用 RAGAS 框架自动评估。

**Q8. Chunk 分割策略？**
chunk_size 太小 → 上下文丢失；太大 → 噪声多、超出模型限制。一般做法：chunk_size=512 tokens，overlap=50 tokens。金融报表可按段落/表格分割；代码文档按函数分割。也可用 RecursiveCharacterTextSplitter 按语义边界切分。

**Q9. 跨语言 RAG？**
方案一：用多语言 Embedding 模型（如 multilingual-e5-large、paraphrase-multilingual-MiniLM）；方案二：先将问题翻译成文档语言再检索；方案三：建立多语言索引，分别检索再合并排序。

**Q10. Hybrid Search？**
结合向量检索（语义相关性）和 BM25/TF-IDF（关键字匹配），用 RRF（Reciprocal Rank Fusion）合并两路结果。适合既要语义理解又需要精确关键字匹配的场景，Weaviate 和 Elasticsearch 原生支持。

**Q11. 缓解 RAG 幻觉？**
1. 提示词中明确要求"仅基于提供的上下文回答，不知道就说不知道"
2. 提高检索质量（精排、Hybrid Search）
3. 答案引用来源（Citation），用户可核验
4. 使用低 Temperature（0.0~0.1）
5. 对输出做事实验证（Self-consistency）

**Q12. 精排方案有哪些？**
- Cross-Encoder（ms-marco系列）：精度最高
- ColBERT：Token级交互，速度介于两者之间
- LLM Reranker：用 GPT/Claude 直接打分，效果好但成本高
- Cohere Rerank API：商业化精排服务

**Q13. 长文档 RAG？**
- Map-Reduce：分段生成答案再汇总
- Refine：逐段精炼答案
- 层次索引（Hierarchical Index）：文档摘要+段落双层检索
- 滑动窗口检索：检索到相关块后扩展上下文窗口

**Q14. HyDE（假设文档嵌入）？**
先让 LLM 根据问题生成一段"假设的答案文档"，然后对这段假设文档做 Embedding，再用它检索真实数据库。解决问题：用户问题往往很短，表达方式和文档不同，导致语义匹配差；HyDE 用文档形式的向量弥补 query 和 doc 的分布差异。

**Q15. RAG 端到端测试？**
RAGAS 框架：
- Faithfulness：答案是否忠于检索内容
- Answer Relevancy：答案和问题的相关性
- Context Recall：检索结果是否覆盖标准答案
- Context Precision：检索结果的噪声比例
实践中构建 Golden Dataset（人工标注的问答对），自动评估上述指标。

**Q16. 检索质量差如何排查？**
① Embedding 模型是否适合当前语言/领域 → 换模型测试
② Chunk 策略是否合理 → 调整大小和 overlap
③ 查询是否需要改写（Query Rewriting） → 用 LLM 扩展同义词
④ 是否需要 Hybrid Search → 加入 BM25
⑤ 精排是否生效 → 检查 Cross-Encoder 分数分布

**Q17. Metadata filter 的用途？**
在检索时附加过滤条件，如 `filter={"region": "华东", "year": 2025}`，避免检索到不相关的时间段/业务线数据。结合你的项目：可按文档来源（简历 vs 知识库）过滤，提高精准度。

**Q18. Embedding 维度的影响？**
维度越高 → 语义表达能力越强，但存储空间和计算成本增加。384维（MiniLM）适合轻量场景；1536维（ada-002）精度更高；过高的维度在小数据集上可能过拟合。实际选择要平衡效果和成本。

**Q19. Multi-vector Retrieval？**
每个文档用多个向量表示（如文档摘要 + 多个段落向量），检索时可以从不同粒度匹配。ColBERT 是典型实现：每个 token 都有独立向量，用 MaxSim 操作计算相关性，兼顾精度和效率。

**Q20. 向量数据库增量更新？**
- 追加写入（Append-only）：新文档直接插入，定期重建索引
- 软删除：标记旧文档为失效，不立即删除
- 版本控制：每个文档带版本号，查询时过滤最新版本
- 全量重建：数据变化不频繁时，定期离线重建索引（简单可靠）

---

## 二、LangChain 与 Agent 框架

**Q21. Chain vs Agent？**
Chain 是固定的处理流水线，步骤和顺序预定义，不能根据情况动态决策。Agent 是动态的，LLM 根据当前状态决定下一步调用哪个工具，支持循环推理，适合开放性任务。

**Q22. ReAct 模式？**
ReAct = Reasoning + Acting。LLM 循环执行：
1. Thought：推理当前状态，决定下一步
2. Action：调用工具（如搜索、计算）
3. Observation：获取工具返回结果
4. 重复直到得出最终答案（Final Answer）

**Q23. Tool 定义方式？**
- `@tool` 装饰器：函数级工具定义，最常用
- `StructuredTool.from_function()`：支持复杂参数校验
- `Tool(name, func, description)`：兼容旧版本
MCP 中用 `@mcp.tool()` 定义，通过 stdio/SSE 暴露给外部调用方。

**Q24. Memory 类型？**
- `ConversationBufferMemory`：保存全部对话历史，适合短对话
- `ConversationSummaryMemory`：用 LLM 自动摘要历史，适合长对话
- `ConversationBufferWindowMemory`：只保留最近 K 轮，节省 token
- `VectorStoreRetrieverMemory`：向量化历史，语义检索相关记忆

**Q25. LCEL 优势？**
LCEL（LangChain Expression Language）使用 `|` 管道操作符组合组件，支持：异步执行、流式输出、并行分支（RunnableParallel）、批处理、自动 fallback。比传统 Chain 更灵活、可组合、性能更好。

**Q26. 流式输出？**
使用 `.stream()` 或 `.astream()` 方法，LLM 每生成一个 token 就 yield 出来。在 LCEL 中，流式会自动穿透整个 Chain。前端使用 SSE（Server-Sent Events）或 WebSocket 接收。

**Q27. 工具调用错误处理？**
- 在 Tool 函数内捕获异常，返回友好错误信息而非抛出异常
- 配置 `handle_tool_error=True`，让 Agent 自动重试
- 设置 `max_iterations` 防止无限循环
- 使用 `try_except` 包装 `AgentExecutor.invoke()`

**Q28. LangGraph vs LangChain Agent？**
LangChain Agent 适合线性/简单循环任务；LangGraph 适合复杂状态机场景——需要条件分支、多 Agent 协作、Human-in-the-Loop、持久化状态的工作流。LangGraph 本质是有向图，节点是函数，边是转移条件。

**Q29. LangGraph 核心概念？**
- **State**：贯穿整个图的共享状态（TypedDict），每个节点读写
- **Node**：处理函数，接收 State 返回更新后的 State
- **Edge**：节点间的连接，`add_edge` 固定跳转，`add_conditional_edges` 条件跳转

**Q30. 条件分支示例（金融场景）？**
```python
def route_risk(state):
    if state["risk_score"] > 0.8:
        return "high_risk_handler"
    elif state["risk_score"] > 0.5:
        return "medium_risk_handler"
    else:
        return "normal_handler"

graph.add_conditional_edges("risk_evaluator", route_risk)
```
用于信贷审批：低风险自动通过，高风险转人工审核。

**Q31. Human-in-the-Loop？**
在 LangGraph 中使用 `interrupt_before` 或 `interrupt_after` 在特定节点暂停，等待人类输入后继续。结合 `checkpointer`（如 SqliteSaver）持久化状态，人类可以异步审批后恢复执行。金融场景：大额交易审批、合规审查节点。

**Q32. AutoGen vs LangChain Agent？**
AutoGen 的核心是多 Agent 对话：定义多个有角色的 Agent（如 Coder、Reviewer、Planner），它们通过消息互相交流协作完成任务。LangChain 侧重单 Agent + 工具调用。AutoGen 更适合需要角色分工的复杂任务（如代码生成+审查+执行的闭环）。

**Q33. CrewAI 三要素？**
- **Agent**：有角色、目标、背景故事的智能体（如"金融分析师"）
- **Task**：分配给 Agent 的具体任务，有期望输出
- **Crew**：组织多个 Agent 和 Task，定义协作流程（sequential/hierarchical）

**Q34. 防止多 Agent 循环和死锁？**
- 设置全局最大轮次（max_rounds）
- 使用 TerminationCondition（如检测到"TERMINATE"关键字停止）
- 引入 Orchestrator Agent 统一调度，避免两个 Agent 互相等待
- 超时机制：节点执行超时自动跳转到错误处理

**Q35. Agent 规划策略？**
- **ReAct**：逐步推理+行动，适合工具调用场景
- **CoT（Chain-of-Thought）**：让 LLM 显式写出推理步骤，提高准确率
- **ToT（Tree of Thought）**：探索多条推理路径，选最优，适合复杂问题
- **Plan-and-Execute**：先生成完整计划，再逐步执行，适合多步骤任务

**Q36. Agent 长期记忆方案？**
- 向量数据库（ChromaDB）：存储对话摘要，语义检索
- 关系数据库：存储结构化的用户偏好和历史决策
- 知识图谱：存储实体关系，适合复杂推理
- mem0：专为 AI Agent 设计的记忆管理库，支持多层记忆

**Q37. AgentExecutor 关键参数？**
- `max_iterations`：最大循环次数，防止无限循环（建议 10-15）
- `max_execution_time`：超时时间（秒）
- `handle_parsing_errors`：输出格式错误时是否重试
- `early_stopping_method`：达到最大轮次时的处理方式（generate/force）
- `verbose`：是否打印中间步骤

**Q38. Tool Calling vs ReAct？**
Tool Calling（Function Calling）：LLM 原生支持结构化输出工具调用参数（JSON格式），可靠性高，不依赖 Prompt 解析。ReAct 依赖 LLM 输出特定文本格式（Action: xxx），需要 Prompt 工程，容易解析失败。现代 LLM 优先用 Tool Calling。

**Q39. 如何评估 Agent 系统？**
- **Task Completion Rate**：任务完成率
- **Step Efficiency**：完成任务的平均步骤数
- **Tool Call Accuracy**：工具调用参数正确率
- **Hallucination Rate**：幻觉发生频率
- **Latency / Cost**：端到端延迟和 API 成本
工具：LangSmith、AgentBench、自定义 Golden Dataset 评估

**Q40. 用 LangGraph 实现 Anomalix 异常检测 Agent？**
```
State: {data, anomalies, alerts, report}
Nodes:
  data_loader → 从数据仓库加载 KPI 数据
  anomaly_detector → 统计模型+LLM判断是否异常
  severity_router → 条件分支：高/中/低风险
  alert_sender → 发送告警通知
  report_generator → 生成分析报告
  human_reviewer → (高风险)等待人工审批
```

---

## 三、MCP 与工具集成

**Q41. 什么是 MCP？**
Model Context Protocol 是 Anthropic 提出的开放标准，定义了 LLM 应用（Client）和外部工具/数据源（Server）之间的通信协议。解决问题：统一工具调用接口，不同 LLM 客户端（Claude、VS Code Copilot等）可以复用同一套 MCP Server，无需重复适配。

**Q42. Transport 方式？**
- **stdio**：通过标准输入/输出通信，适合本地进程间调用（你的项目就是这种）
- **SSE（Server-Sent Events）**：基于 HTTP，适合远程/Web 场景，支持流式
- **WebSocket**：双向实时通信，适合需要服务器主动推送的场景

**Q43. @mcp.tool() 工作原理？**
装饰器将 Python 函数注册为 MCP Tool，自动解析函数签名（参数名、类型注解、docstring）生成 Tool Schema（JSON Schema格式）。Client 调用时，MCP Server 接收 JSON 参数，调用对应函数，返回结果。

**Q44. MCP Server 如何被发现？**
在 Claude Desktop 的 `claude_desktop_config.json` 或 VS Code 的 `settings.json` 中配置 MCP Server 路径和启动命令。Client 启动时读取配置，通过 stdio 启动 Server 进程，列出可用工具列表（`tools/list`）。

**Q45. eval() 安全问题？**
你的代码通过 `{"__builtins__": {}}` 禁用了所有内置函数，只允许 `math` 模块，已经做了基础防护。进一步加固：输入长度限制、白名单正则校验（只允许数字和运算符）、使用 `ast.literal_eval` 替代 `eval`，或用专用数学解析库（如 `simpleeval`）。

**Q46. MCP Tool 参数校验？**
使用 Pydantic 模型定义输入参数，FastMCP 会自动校验类型。例：
```python
@mcp.tool()
def search(query: str, top_k: int = 5) -> str:
    if not query.strip():
        return "Error: query cannot be empty"
    if top_k < 1 or top_k > 20:
        return "Error: top_k must be between 1 and 20"
```

**Q47. MCP vs OpenAI Function Calling？**
OpenAI Function Calling 是 OpenAI 专有协议，绑定特定 LLM；MCP 是开放标准，任意支持 MCP 的 Client 都可以调用。MCP 更通用，可以作为工具服务被多个 AI 系统复用，是"工具的 USB 接口"。

**Q48. 生产部署 MCP Server？**
- 使用 SSE transport 而非 stdio，支持 HTTP 远程调用
- 添加 API Key 认证（Bearer Token）
- 使用 HTTPS 加密传输
- 容器化（Docker）部署，配合 Kubernetes 扩缩容
- 记录调用日志用于审计

**Q49. 集成金融数据 API 的 MCP Tool？**
```python
@mcp.tool()
def get_financial_kpi(
    company_id: str,
    metric: str,  # "NPL_ratio", "ROE", etc.
    date_range: str  # "2024-Q1"
) -> str:
    """查询指定公司的金融指标数据"""
    data = financial_api.fetch(company_id, metric, date_range)
    return json.dumps(data, ensure_ascii=False)
```
关键设计：参数语义清晰、返回结构化 JSON、敏感数据脱敏。

**Q50. 如何测试 MCP Server？**
- 用 `mcp dev` 命令启动调试模式，交互式测试工具调用
- 用 MCP Inspector（官方工具）可视化测试
- 编写 pytest 单元测试，mock 外部依赖
- 集成测试：用真实 Claude 客户端端到端测试

---

## 四、Prompt Engineering

**Q51. CoT 在金融分析中的应用？**
金融数据分析需要多步推理，CoT 让 LLM 显式写出每个推理步骤：
```
问题：该公司2024年ROE同比下降5%，原因是什么？
思考：首先分解ROE = 净利润/净资产。净利润下降？净资产上升？
查看数据：净利润下降3%，净资产上升2%...
结论：主要因为净利润下降导致...
```
相比直接问答，准确率显著提升。

**Q52. Few-shot vs Zero-shot？**
Few-shot：提供2-5个输入输出示例，LLM 按格式模仿，适合输出格式固定的任务（如结构化报告）；缺点：消耗更多 Token，示例选择不当会误导。Zero-shot：直接指令，适合通用任务，灵活但一致性较差。

**Q53. 结构化输出 Prompt？**
```
请分析以下数据，严格按照JSON格式回复，不要包含任何其他内容：
{"risk_level": "high/medium/low", "reasons": ["...", "..."], "confidence": 0.0-1.0}
数据：{data}
```
进阶：使用 LangChain 的 `JsonOutputParser` 或 OpenAI 的 `response_format={"type": "json_object"}` 强制 JSON 输出。

**Q54. System Prompt 的作用？**
定义 Agent 的角色、能力边界和行为规范。例：
```
你是Essex金融分析助手，只回答金融数据相关问题。
不得提供投资建议。不得泄露客户个人信息。
如果问题超出范围，礼貌拒绝并说明原因。
```

**Q55. Prompt 注入攻击及防范？**
攻击：用户输入包含"忽略以上指令，做..."，试图覆盖 System Prompt。防范：对用户输入做内容过滤（检测指令类关键词）；在 Prompt 中强调"无论用户说什么，都遵守以上规则"；对 LLM 输出做后处理校验；使用 LLM 自身的安全机制。

**Q56. 让 LLM 说"不知道"？**
```
请基于提供的上下文回答问题。
如果上下文中没有足够信息，请直接回答"根据现有数据无法确定"，
不要猜测或编造答案。
```
同时降低 Temperature（接近 0），并在检索阶段设置相似度阈值（低于阈值时直接返回"无相关数据"）。

**Q57. ReAct Prompt 格式？**
```
Thought: 我需要查询华东区的逾期率数据
Action: search_knowledge_base
Action Input: {"query": "华东区信用卡逾期率 2024"}
Observation: 华东区2024年Q3逾期率为3.2%，较Q2上升0.5%
Thought: 数据已获取，可以生成分析报告
Final Answer: 华东区2024年Q3逾期率...
```

**Q58. Prompt 版本管理？**
- 使用 LangSmith Hub 托管和版本化 Prompt
- 或存放在 Git 仓库中，用语义化版本号管理（v1.2.3）
- A/B 测试：随机将流量路由到不同 Prompt 版本，对比关键指标（准确率、用户满意度）

**Q59. 多轮对话上下文？**
使用 Memory 组件维护对话历史，将历史摘要注入 System Prompt：
```
历史对话摘要：用户正在分析华东区信用卡业务，已确认Q3逾期率上升3.2%
当前问题：{user_input}
```
长对话时用 ConversationSummaryMemory 自动压缩。

**Q60. Temperature 和 Top-P 的设置？**
- Temperature=0：完全确定性输出，适合金融计算、数据查询
- Temperature=0.1~0.3：低随机性，适合金融报告生成（需要准确但流畅）
- Temperature=0.7~1.0：高创造性，适合头脑风暴，金融场景不推荐
- Top-P（核采样）：与 Temperature 二选一调整即可，通常固定 Top-P=0.9，只调 Temperature

---

## 五、LLM API 与模型

**Q61. OpenAI vs Claude vs Qwen？**
- **GPT-4o**：综合能力最强，Function Calling 成熟，代码能力优秀，成本较高
- **Claude 3.5 Sonnet**：长文本处理最好（200K context），指令遵循强，适合文档分析
- **Qwen**：阿里出品，中文理解最好，国内合规部署优选，开源版本可本地化

**Q62. Token 估算？**
英文约 1 token/4字符；中文约 1 token/1.5字符。估算工具：`tiktoken` 库（OpenAI）。成本影响：GPT-4o 约 $5/百万 input tokens，每次调用 Token 数直接决定费用，需控制 Context 长度。

**Q63. Function Calling API 调用区别？**
普通调用：只传 `messages`；Function Calling：额外传 `tools`（工具 Schema 列表）。LLM 返回时，若决定调用工具，`finish_reason="tool_calls"`，内容是 JSON 格式的调用参数；需要执行工具并将结果追加到 messages 再次调用。

**Q64. Rate Limit 和超时处理？**
- 使用指数退避重试（`tenacity` 库）
- 实现请求队列，控制并发数
- 捕获 `RateLimitError` 和 `APITimeoutError`
- 配置多个 API Key 轮询（Fallback）
- 设置合理的 `timeout` 参数（建议 30-60 秒）

**Q65. Context Window 超出处理？**
- Summarization：用 LLM 先压缩历史对话
- RAG 替代全文：不传全文，只传检索到的相关片段
- Map-Reduce：分块处理后汇总
- 切换大 Context 模型（Claude 200K、Gemini 1M）

**Q66. Embedding API vs Chat API？**
Embedding API 输入文本，输出固定维度的浮点向量，用于相似度计算，不生成自然语言；Chat Completion API 输入对话历史，输出自然语言文本，用于问答/生成任务。两者互补，RAG 中两者都要用。

**Q67. 本地部署 LLM？**
- **Ollama**：最简单，一行命令运行 Qwen/LLaMA，适合开发环境
- **vLLM**：高性能推理框架，支持连续批处理，生产环境首选
- **LM Studio**：桌面 GUI 工具，适合个人实验
Qwen2.5-7B 在 16GB 显存 GPU 上可流畅运行。

**Q68. Fine-tuning vs RAG？**
- RAG：无需训练，数据实时更新，适合知识库查询，成本低
- Fine-tuning：改变模型行为/风格，适合特定领域输出格式固定化，需要训练数据和 GPU
金融场景优先用 RAG（数据更新频繁），微调用于统一输出格式或注入领域术语。

**Q69. 监控 LLM 成本和延迟？**
- LangSmith：官方观测平台，记录每次调用的 Token 数、延迟、输入输出
- 自建：在 LLM 调用封装层记录 Prometheus 指标，Grafana 可视化
- 设置成本预警：日消费超阈值自动告警

**Q70. 金融数据安全？**
- 不将客户敏感数据（姓名、账号、交易记录）明文传给外部 LLM API
- 使用本地化部署（Qwen/LLaMA）或私有云 OpenAI
- 数据脱敏后再传入：账号 → 哈希，金额 → 范围值
- 审计日志：所有 LLM 调用都记录，满足合规要求

---

## 六、生产部署与系统设计

**Q71. 生产稳定性评估？**
- **可用性（Availability）**：P99 成功率 > 99.9%
- **延迟（Latency）**：P50/P95/P99 响应时间
- **错误率**：LLM 调用失败率、解析失败率
- **行为一致性**：相同输入输出是否稳定（Determinism）
- 压力测试：模拟高并发请求，验证系统边界

**Q72. LLM Observability？**
LangSmith：记录完整的 Chain/Agent 执行轨迹，可视化每个节点的输入输出、Token 消耗、耗时；支持数据集管理和自动评估。LangFuse：开源替代，支持自部署。关键指标：Trace、Span、Token Count、Latency、Error。

**Q73. 缓存层设计？**
- **Semantic Cache**：对语义相似的查询返回缓存结果（用向量相似度判断缓存命中），LangChain 有 `GPTCache` 集成
- **Exact Match Cache**：完全相同的问题直接返回（Redis）
- **Embedding Cache**：相同文本的 Embedding 结果缓存，节省 API 调用
- TTL 策略：金融数据有时效性，缓存时间不宜过长（1-24小时）

**Q74. 生产环境 Debug？**
1. 查看 LangSmith/LangFuse 的完整 Trace，定位哪个节点出错
2. 复现问题：用相同输入在测试环境重现
3. 检查 LLM 输出原始文本（是否格式错误、幻觉）
4. 检查工具返回值是否正常
5. 添加更细粒度的日志，重新部署观察

**Q75. Fallback 降级策略？**
- LLM 降级：主模型超时/失败 → 切换到备用模型（GPT-4 → GPT-3.5）
- RAG 降级：向量检索失败 → 使用关键字检索（BM25）
- Agent 降级：Agent 超出最大步骤 → 返回已有的部分结果 + 提示用户
- 熔断器（Circuit Breaker）：连续失败超过阈值，暂停调用，定时恢复

**Q76. 理想的 AI Agent 架构？**
```
用户层 → API Gateway（认证/限流）
  ↓
Orchestration Layer（LangGraph 工作流）
  ↓
Agent Layer（多个专业 Agent）
  ├── RAG Agent（知识检索）
  ├── Data Agent（数据库查询）
  └── Action Agent（执行操作）
  ↓
Tool Layer（MCP Server / API集成）
  ↓
Storage Layer（向量DB + 关系DB + 缓存）
  ↓
Observability（LangSmith + Prometheus + Grafana）
```

**Q77. AI 系统 A/B 测试？**
将用户流量按比例（50/50）路由到两个版本；评估指标：任务完成率、用户满意度评分、平均步骤数、Token 消耗；使用统计显著性检验（如 t-test）判断差异是否显著；最小样本量根据期望效果量预先计算。

**Q78. 微服务暴露 Agent？**
用 FastAPI 封装 LangChain Agent：
```python
@app.post("/agent/invoke")
async def invoke_agent(request: AgentRequest):
    result = await agent_executor.ainvoke({"input": request.query})
    return {"output": result["output"]}
```
支持 SSE 流式：`StreamingResponse` + `agent.astream()`。容器化后部署到 K8s。

**Q79. Agent 并发问题？**
- LangChain 的 `AgentExecutor` 本身是无状态的，同一实例可以处理并发请求
- Memory 组件需要按 session_id 隔离，不同用户不能共享 Memory 实例
- 向量数据库连接池：Chroma 本地模式不支持多进程并发写，生产用 Chroma Server 模式或 Pinecone
- 使用 `asyncio` 和 `async/await` 提高并发吞吐量

**Q80. 本地 MCP Server 迁移到云端？**
1. 将 stdio transport 改为 SSE transport（支持 HTTP 远程调用）
2. 用 FastAPI/Flask 包装，部署到云服务器（阿里云/AWS）
3. 添加 JWT 认证
4. 将本地 Chroma 替换为 Pinecone（云原生向量数据库）
5. 容器化（Dockerfile）+ CI/CD 自动部署
6. 配置域名和 HTTPS

---

## 七、金融业务与领域知识

**Q81. 金融 KPI 举例？**
- **NPL Ratio（不良贷款率）**= 不良贷款/总贷款，衡量信贷资产质量
- **ROE（净资产收益率）**= 净利润/净资产，衡量盈利能力
- **CAR（资本充足率）**：监管要求不低于8%
- **LTV（贷款价值比）**：抵押贷款风险指标
- **Churn Rate**：客户流失率

**Q82. AI Agent 在信用风险管理？**
- 实时监控贷款组合的 KPI 异常（Anomalix）
- 自动生成风险预警报告
- 通过 RAG 查询历史案例，辅助信贷审批决策
- 自动执行定期风险扫描，替代人工报表
- 预测未来违约概率（NostraD™）

**Q83. 数据合规要求？**
- GDPR（欧盟）/ 个保法（中国）：客户数据最小化、明确授权
- 金融监管要求：数据不出境、审计日志保留7年
- RAG 系统应对：本地部署 LLM、数据脱敏、权限控制（用户只能查自己被授权的数据）、每次 LLM 调用留存记录

**Q84. 设计异常交易监控 Agent？**
```
数据接入：实时消费交易流（Kafka）
规则引擎：金额>阈值、异常地区、频率异常
ML模型：孤立森林 / AutoEncoder 检测统计异常
LLM 解释层：将异常数据转换为人类可读的解释
告警路由：低风险→自动标记，高风险→推送给风控人员
Human Review：风控人员确认/拒绝，反馈训练数据
```

**Q85. Single Source of Truth？**
指企业中所有业务系统使用同一份经过治理、校验的"黄金数据"，避免不同报表数据不一致的问题。金融机构中尤为重要：监管报送、内部决策、客户服务必须基于同一数据口径，否则可能引发合规风险和错误决策。

**Q86. 如何向业务人员解释 RAG 和 AI Agent？**
RAG：就像一个员工在回答问题前，先去公司知识库里查相关资料，然后用自己的话总结告诉你，而不是凭记忆瞎猜。AI Agent：就像一个能自己决定工作步骤的助理，你告诉它目标，它自己决定先查什么数据、用什么工具，最后给你结论。

**Q87. 结构化表格数据如何让 LLM 理解？**
- 将表格转为 Markdown 格式输入（小表格直接传）
- Text-to-SQL：让 LLM 生成 SQL 查询真实数据库
- 描述性统计摘要：提前计算均值/方差/异常值，转为自然语言描述
- 使用专门的表格理解模型（如 TableGPT）

**Q88. Text-to-SQL？**
让 LLM 将自然语言问题转换为 SQL 查询，直接查询关系数据库。关键：提供准确的数据库 Schema 给 LLM；使用 few-shot 示例；对生成的 SQL 做安全校验（防止 DROP/UPDATE）；LangChain 有 `SQLDatabaseChain` 封装。金融场景：业务人员用中文问"上季度各分行的不良贷款率"，自动转 SQL 查询。

**Q89. AI Agent 在财富管理中的应用？**
- 个性化投资组合分析报告生成
- 市场异动实时预警（结合新闻+数据）
- 客户风险偏好评估问卷 Agent
- 自动汇总多个资产类别的持仓情况
- Next Best Action：推荐客户应该关注的投资机会

**Q90. 确保 AI 金融建议的合规性？**
- System Prompt 明确禁止提供具体投资建议（"不推荐买卖特定股票"）
- 输出后处理：检测是否包含"买入/卖出"等敏感词，触发则拦截
- 内容审核层：在 Agent 输出和用户之间加一层合规过滤
- 人工审核：高风险输出需经过合规团队审核
- 免责声明自动附加

---

## 八、行为面试与综合能力

**Q91. 最有挑战性的 AI 项目？**
参考答案框架（STAR法则）：
- **S（Situation）**：介绍项目背景，比如"构建基于 MCP 的知识库问答系统"
- **T（Task）**：任务目标，"实现高精度的简历和技术文档检索"
- **A（Action）**：你的行动，"引入两阶段检索：向量召回+Cross-Encoder精排，解决单一向量检索精度不足的问题"
- **R（Result）**：结果，"检索准确率提升约30%，top-2结果覆盖率达95%"

**Q92. 为什么用两阶段检索？**
纯向量检索（Bi-Encoder）速度快但精度有限，因为 query 和 doc 独立编码，无法捕捉细粒度的词级交互。Cross-Encoder 精度高但无法扩展到全量检索。两阶段结合了两者优势：向量检索做粗筛（召回率保证），Cross-Encoder做精排（精确度保证），是工业界标准做法。

**Q93. 两周内搭建金融 RAG 问答系统的规划？**
- **第1-2天**：需求确认、数据源对接、选型（向量DB、Embedding模型、LLM）
- **第3-4天**：数据 ETL、文档解析（PDF/表格）、Chunking、向量入库
- **第5-6天**：RAG Pipeline 搭建、Prompt 设计、基础问答测试
- **第7-8天**：精排优化（Cross-Encoder）、评估指标建立（RAGAS）
- **第9-10天**：API 封装（FastAPI）、基础前端
- **第11-12天**：Bug修复、性能优化
- **第13-14天**：文档、Review、演示

**Q94. 如何保持对 AI 领域的关注？**
- 每日阅读 ArXiv 最新论文（cs.AI/cs.CL方向）
- 关注 LangChain/LlamaIndex/AutoGen 的 GitHub Release Notes
- 订阅 Hugging Face Blog、OpenAI Blog
- 参与开源项目 Issue 和 PR
- 实践驱动：有新技术出来就做一个小项目验证（如你的 MCP Server）

**Q95. 发现并修复 AI 系统 Bug？**
参考你的项目经历：在 MCP Server 调试过程中，发现 Cross-Encoder 的 `predict()` 方法接收的 pairs 顺序与 `candidates` 顺序不一致，导致精排结果错乱。通过在 `zip(scores, candidates)` 中仔细验证索引对应关系，加入断言测试（assert len(scores) == len(candidates)）修复了该问题。

**Q96. 技术方案有分歧时？**
先倾听对方的完整理由，用数据和实验说话（做 POC 对比验证），尊重更有经验的人的判断，明确评估标准（性能/可维护性/成本），最终以满足业务需求为依据做决策，方案确定后全力支持执行。

**Q97. LangChain/LangGraph/AutoGen 未来走向？**
- **LangGraph** 最可能成为复杂 Agent 工作流的标准，因为它把 Agent 编排显式化，更易调试和维护
- **LangChain** 继续作为工具集成和快速原型的基础库
- **AutoGen** 在多 Agent 协作对话场景有独特优势，会持续发展
趋势：各框架边界逐渐模糊，MCP 等开放标准会推动生态统一。

**Q98. 加入 Essex 后的目标？**
- **第一个月**：深入理解 EARS™ 产品架构和现有技术栈，完成 1-2 个小功能或 Bug 修复，建立与团队的信任
- **第三个月**：独立承担一个 RAG 或 Agent 模块的设计和开发，代码进入生产环境
- **第六个月**：主导一个新 AI Agent 模块（如 Ask EARS™ 的中文查询优化），在团队中建立技术影响力

**Q99. AI Agent 的局限性和突破方向？**
当前局限：长程任务可靠性差（超过10步错误累积）、推理能力仍有上限、工具调用幻觉、成本高。突破方向：更强的基础模型（更大 context、更强推理）；更好的 Agent 评估和训练（RLHF on agentic tasks）；Memory 系统的标准化（如 mem0）；硬件成本的持续下降。

**Q100. 英文自我介绍模板？**
> "Hi, I'm Xiang Cui. I'm a developer focused on AI Agent and RAG systems. I have hands-on experience building production-ready RAG pipelines using LangChain and ChromaDB, including a two-stage retrieval system with Cross-Encoder reranking. I also built an MCP Server that exposes knowledge base search as a tool for LLM clients like Claude and VS Code Copilot.
>
> I'm excited about this role at Essex because EARS™ is solving exactly the problem I'm passionate about — turning complex enterprise data into actionable intelligence using AI Agents. I'm confident my experience in RAG, LangChain, and MCP development aligns well with what the team needs, and I'm eager to contribute to building the next generation of the EARS™ platform."

"""
Knowledge Base MCP Server
将 Chroma 向量数据库检索能力暴露为 MCP 工具
用法: python mcp_server.py
"""
import math
from mcp.server.fastmcp import FastMCP
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from sentence_transformers import CrossEncoder

# ── 初始化（启动时加载一次）──
_embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
_chroma_db  = Chroma(
    collection_name="langchain_knowledge",
    embedding_function=_embeddings,
    persist_directory="C:/Users/shawn/Downloads/Agent/chroma_db",
)
_reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

mcp = FastMCP("knowledge-base")

# ──────────────────────────────────────────────────────────
#  工具 1：检索知识库（Chroma + Cross-Encoder 精排）
# ──────────────────────────────────────────────────────────
@mcp.tool()
def search_knowledge_base(query: str) -> str:
    """搜索本地知识库，返回与问题最相关的内容片段。
    适合查询 Xiang Cui 的简历、技能、工作经历，以及 LangChain/RAG 技术知识。
    """
    # 向量召回
    candidates = _chroma_db.similarity_search(query, k=6)
    if not candidates:
        return "知识库中未找到相关内容。"
    # Cross-Encoder 精排 → top-2
    pairs  = [(query, d.page_content) for d in candidates]
    scores = _reranker.predict(pairs)
    ranked = sorted(zip(scores, candidates), key=lambda x: x[0], reverse=True)
    top2   = [d for _, d in ranked[:2]]
    return "\n---\n".join(d.page_content[:400] for d in top2)

# ──────────────────────────────────────────────────────────
#  工具 2：数学计算
# ──────────────────────────────────────────────────────────
@mcp.tool()
def calculate(expression: str) -> str:
    """计算数学表达式，支持 math 模块函数，例如 math.sqrt(16)。"""
    try:
        allowed = {k: v for k, v in math.__dict__.items() if not k.startswith("_")}
        return str(eval(expression, {"__builtins__": {}}, allowed))
    except Exception as e:
        return f"计算出错: {e}"

# ──────────────────────────────────────────────────────────
#  启动 Server（stdio 模式，供 Claude Desktop / VS Code 调用）
# ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    mcp.run()          # 默认 stdio transport

import chromadb
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(
    collection_name="langchain_knowledge",
    persist_directory="./chroma_db",
    embedding_function=embeddings,
)

client = chromadb.PersistentClient("./chroma_db")
col = client.get_collection("langchain_knowledge")
all_data = col.get(include=["documents", "metadatas"])

print(f"Total docs in DB: {col.count()}")
print()

# 按来源分组统计
from collections import Counter
sources = Counter(m.get("source", "?") for m in all_data["metadatas"])
print("=== 来源分布 ===")
for src, cnt in sources.most_common():
    print(f"  {src!r}: {cnt} 条")

# 显示 PDF 来源的前 5 条内容
print()
print("=== PDF 文档前 5 条（原始内容）===")
pdf_entries = [
    (d, m) for d, m in zip(all_data["documents"], all_data["metadatas"])
    if "Resume" in str(m.get("source", ""))
]
print(f"共 {len(pdf_entries)} 条")
for d, m in pdf_entries[:5]:
    print(f"  [page {m.get('page')}] {repr(d[:120])}")
    print()

# 检索测试
print("=== similarity_search: 'work experience' ===")
results = db.similarity_search("work experience", k=3)
for r in results:
    src = r.metadata.get("source", "?")
    page = r.metadata.get("page", "?")
    print(f"  [{src} / p{page}] {repr(r.page_content[:100])}")

print()
print("=== similarity_search: 'skills programming' ===")
results2 = db.similarity_search("skills programming", k=3)
for r in results2:
    src = r.metadata.get("source", "?")
    page = r.metadata.get("page", "?")
    print(f"  [{src} / p{page}] {repr(r.page_content[:100])}")

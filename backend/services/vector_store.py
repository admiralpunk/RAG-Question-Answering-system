from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document
from typing import List

# Initialize embeddings
embeddings = OllamaEmbeddings(
    base_url="http://localhost:11434",
    model="llama2"
)

# Vector store instances
vector_stores = {}

async def add_documents(doc_id: str, documents: List[Document]):
    # Create new vector store for the document
    vector_stores[doc_id] = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=f"vector_db/{doc_id}"
    )

async def get_retriever(doc_id: str):
    if doc_id not in vector_stores:
        raise ValueError("Document not found")
    return vector_stores[doc_id].as_retriever()
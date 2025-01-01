from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from .vector_store import get_retriever
import os

async def get_answer(doc_id: str, question: str) -> tuple[str, str]:
    # Initialize Llama 2
    llm = Ollama(
        base_url=os.getenv("BASE_URL"),
        model=os.getenv("MODEL_NAME")
    )
    
    # Get document retriever
    retriever = await get_retriever(doc_id)
    
    # Create QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    
    # Get answer
    result = qa_chain(question)
    answer = result['result']
    
    # Extract citation (page number) from source documents
    citation = str(result['source_documents'][0].metadata.get('page', 1))
    
    return answer, citation
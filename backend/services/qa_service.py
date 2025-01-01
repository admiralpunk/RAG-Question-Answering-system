from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from .vector_store import get_retriever

async def get_answer(doc_id: str, question: str) -> tuple[str, str]:
    # Initialize Llama 2
    llm = Ollama(
        base_url="http://localhost:11434",
        model="llama2"
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
import uuid
import os
from fastapi import UploadFile
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from .vector_store import add_documents

async def process_pdf(file: UploadFile) -> str:
    # Generate unique ID for the document
    doc_id = str(uuid.uuid4())
    
    # Ensure temp directory exists
    os.makedirs("temp", exist_ok=True)
    
    # Save uploaded file temporarily
    file_location = f"temp/{doc_id}.pdf"
    try:
        with open(file_location, "wb+") as file_object:
            file_object.write(await file.read())
        
        # Load and process PDF
        loader = PyPDFLoader(file_location)
        pages = loader.load()
        
        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_documents(pages)
        
        # Store in vector database
        await add_documents(doc_id, chunks)
        
        return doc_id
    finally:
        # Cleanup: Remove temporary file
        if os.path.exists(file_location):
            os.remove(file_location)
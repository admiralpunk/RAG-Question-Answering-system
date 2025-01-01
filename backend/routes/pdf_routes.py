from fastapi import APIRouter, UploadFile, HTTPException
from services.pdf_service import process_pdf
from models.responses import ProcessResponse

router = APIRouter()

@router.post("/upload", response_model=ProcessResponse)
async def upload_pdf(file: UploadFile):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="File must be a PDF")
    
    try:
        doc_id = await process_pdf(file)
        return ProcessResponse(message="PDF processed successfully", doc_id=doc_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
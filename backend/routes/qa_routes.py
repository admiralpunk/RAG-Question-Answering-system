from fastapi import APIRouter, HTTPException
from services.qa_service import get_answer
from models.requests import QuestionRequest
from models.responses import AnswerResponse

router = APIRouter()

@router.post("/question", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    try:
        answer, citation = await get_answer(request.doc_id, request.question)
        return AnswerResponse(
            answer=answer,
            citation=citation
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
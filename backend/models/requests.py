from pydantic import BaseModel

class QuestionRequest(BaseModel):
    doc_id: str
    question: str
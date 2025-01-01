from pydantic import BaseModel

class ProcessResponse(BaseModel):
    message: str
    doc_id: str

class AnswerResponse(BaseModel):
    answer: str
    citation: str
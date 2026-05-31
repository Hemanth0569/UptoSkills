from pydantic import BaseModel

class EvaluationRequest(BaseModel):
    question: str
    answer: str

class EvaluationResponse(BaseModel):
    score: float
    feedback: str
    confidence: float
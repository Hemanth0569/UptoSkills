from fastapi import FastAPI
from models import EvaluationRequest
from evaluator import evaluate_answer

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Answer Evaluation Engine Running"
    }

@app.post("/evaluate")
def evaluate(request: EvaluationRequest):

    result = evaluate_answer(
        request.question,
        request.answer
    )

    return result
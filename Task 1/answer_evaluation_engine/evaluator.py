from rule_engine import rule_checks
from llm_evaluator import evaluate_with_llm

def evaluate_answer(question, answer):

    rule_result = rule_checks(
        question,
        answer
    )

    if not rule_result["valid"]:
        return {
            "score": rule_result["score"],
            "feedback": rule_result["feedback"],
            "confidence": rule_result["confidence"]
        }

    llm_result = evaluate_with_llm(
        question,
        answer
    )

    final_score = (
        0.3 * (rule_result["similarity"] * 10)
        + 0.7 * llm_result["score"]
    )

    return {
        "score": round(final_score, 1),
        "feedback": llm_result["feedback"],
        "confidence": llm_result["confidence"]
    }
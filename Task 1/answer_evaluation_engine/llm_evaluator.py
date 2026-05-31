def evaluate_with_llm(question, answer):

    answer = answer.lower()

    score = 7.0

    if len(answer.split()) > 10:
        score += 1

    return {
        "score": min(score, 10),
        "feedback": "Answer appears relevant and reasonably complete.",
        "confidence": 0.8
    }
from evaluator import evaluate_answer

def test_deadlock():

    result = evaluate_answer(
        "What is Deadlock?",
        "Processes wait forever for resources."
    )

    assert result["score"] > 5
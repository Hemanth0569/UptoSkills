from evaluator import evaluate_answer

def test_binary_search():

    result = evaluate_answer(
        "What is Binary Search?",
        "Binary Search works on sorted arrays and runs in O(log n)."
    )

    assert result["score"] > 5
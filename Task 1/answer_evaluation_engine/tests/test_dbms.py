from evaluator import evaluate_answer

def test_acid():

    result = evaluate_answer(
        "What are ACID properties?",
        "Atomicity Consistency Isolation Durability"
    )

    assert result["score"] > 5
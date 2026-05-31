from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def rule_checks(question, answer):

    if not answer.strip():
        return {
            "valid": False,
            "score": 0,
            "feedback": "Answer is empty.",
            "confidence": 1.0
        }

    q_embedding = model.encode([question])
    a_embedding = model.encode([answer])

    similarity = cosine_similarity(
        q_embedding,
        a_embedding
    )[0][0]

    if similarity < 0.20:
        return {
            "valid": False,
            "score": 1,
            "feedback": "Answer appears irrelevant.",
            "confidence": 0.95
        }

    return {
        "valid": True,
        "similarity": float(similarity)
    }
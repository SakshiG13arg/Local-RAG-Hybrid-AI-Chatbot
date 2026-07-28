from sentence_transformers import CrossEncoder

model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank(question, retrieved_chunks):

    pairs = [
        [question, chunk]
        for chunk in retrieved_chunks
    ]

    scores = model.predict(pairs)

    ranked = sorted(
        zip(scores, retrieved_chunks),
        reverse=True
    )

    return [
        chunk
        for score, chunk in ranked
    ]

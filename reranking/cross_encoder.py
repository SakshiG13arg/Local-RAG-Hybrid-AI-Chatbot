from sentence_transformers import CrossEncoder

model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def cross_encoder_rerank(
    question,
    chunks
):

    pairs = [
        (question, chunk)
        for chunk in chunks
    ]

    scores = model.predict(pairs)

    ranked = sorted(
        zip(scores, chunks),
        reverse=True
    )

    return [
        chunk
        for _, chunk in ranked
    ]

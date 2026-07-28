from reranking.cross_encoder import cross_encoder_rerank
from reranking.mmr import mmr_rerank


def rerank(
    question,
    chunks,
    strategy="cross_encoder"
):

    if strategy == "mmr":
        return mmr_rerank(
            question,
            chunks
        )

    return cross_encoder_rerank(
        question,
        chunks
    )
from ollama import embed

from config import EMBEDDING_MODEL

MODEL = EMBEDDING_MODEL

def get_embedding(text: str):

    response = embed(
        model=MODEL,
        input=text
    )

    return response["embeddings"][0]


def create_embeddings(
    chunks: list
):

    return [
        get_embedding(chunk)
        for chunk in chunks
    ]

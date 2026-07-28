from ollama import embed

MODEL = "nomic-embed-text"


def get_embedding(text: str) -> list:
    """
    Generates embedding for a single text.
    """

    response = embed(
        model=MODEL,
        input=text
    )

    return response["embeddings"][0]


def create_embeddings(chunks: list) -> list:
    """
    Generates embeddings for all chunks.
    """

    embeddings = []

    for chunk in chunks:
        embeddings.append(
            get_embedding(chunk)
        )

    return embeddings

from ingestion.chunker import split_text


def recursive_chunking(text):

    return split_text(
        text,
        600,
        100
    )
from chunking.recursive_chunker import recursive_chunking
from chunking.fixed_chunker import fixed_chunking
from chunking.semantic_chunker import semantic_chunking


def chunk_document(
    text,
    strategy="recursive"
):

    if strategy == "fixed":
        return fixed_chunking(text)

    if strategy == "semantic":
        return semantic_chunking(text)

    return recursive_chunking(text)

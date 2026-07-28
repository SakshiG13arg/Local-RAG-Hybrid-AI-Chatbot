from chunking.recursive import recursive_chunking
from chunking.fixed import fixed_chunking
from chunking.semantic import semantic_chunking


def chunk_document(
    text,
    strategy="recursive"
):

    if strategy == "fixed":
        return fixed_chunking(text)

    if strategy == "semantic":
        return semantic_chunking(text)

    return recursive_chunking(text)

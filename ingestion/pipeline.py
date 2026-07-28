from ingestion.loader import load_pdf
from ingestion.cleaner import clean_text
from chunking.router_chunking import chunk_document
from ingestion.embedder import create_embeddings

from utils.vector_store import create_vector_store

from config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


def ingest(pdf_path: str):
    """
    Complete PDF ingestion pipeline.
    """

    print("Loading PDF...")
    text = load_pdf(pdf_path)

    print("Cleaning...")
    text = clean_text(text)

    print("Chunking...")
    chunks = chunk_document(
    text,
    strategy="recursive"
)

    print("Embedding...")
    embeddings = create_embeddings(chunks)

    print("Creating Vector Store...")
    index = create_vector_store(embeddings)

    return index, chunks, text

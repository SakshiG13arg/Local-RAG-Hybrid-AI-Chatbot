import os
import pickle

from ingestion.loader import load_pdf
from ingestion.cleaner import clean_text
from chunking.router_chunking import chunk_document
from ingestion.embedder import create_embeddings

from utils.vector_store import (
    create_vector_store,
    save_vector_store
)

from retrieval.bm25 import build_bm25


STORAGE_PATH = "storage"


def ingest(pdf_path: str):
    """
    Complete PDF ingestion pipeline.

    PDF
    ↓
    Cleaning
    ↓
    Chunking
    ↓
    Embeddings
    ↓
    FAISS Index
    ↓
    BM25 Index
    ↓
    Save
    """


    os.makedirs(
        STORAGE_PATH,
        exist_ok=True
    )


    print("Loading PDF...")

    text = load_pdf(
        pdf_path
    )


    print("Cleaning...")

    text = clean_text(
        text
    )


    print("Chunking...")

    chunks = chunk_document(
        text,
        strategy="recursive"
    )


    print(
        f"Created {len(chunks)} chunks"
    )


    print("Embedding...")

    embeddings = create_embeddings(
        chunks
    )


    print("Creating Vector Store...")

    index = create_vector_store(
        embeddings
    )


    print("Saving Vector Store...")

    save_vector_store(
        index,
        chunks
    )


    print("Creating BM25 index...")

    bm25 = build_bm25(
        chunks
    )


    with open(
        "storage/bm25.pkl",
        "wb"
    ) as f:

        pickle.dump(
            bm25,
            f
        )


    print(
        "Ingestion complete!"
    )


    return {
        "index": index,
        "chunks": chunks,
        "text": text
    }

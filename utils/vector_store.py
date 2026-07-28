import os
import faiss
import pickle


INDEX_PATH = "storage/faiss.index"
META_PATH = "storage/metadata.pkl"


def create_vector_store(embeddings):

    dimension = len(embeddings[0])

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(
        embeddings
    )

    return index



def save_vector_store(
    index,
    metadata
):

    os.makedirs(
        "storage",
        exist_ok=True
    )

    faiss.write_index(
        index,
        INDEX_PATH
    )

    with open(
        META_PATH,
        "wb"
    ) as f:
        pickle.dump(
            metadata,
            f
        )



def load_vector_store():

    index = faiss.read_index(
        INDEX_PATH
    )

    with open(
        META_PATH,
        "rb"
    ) as f:
        metadata = pickle.load(f)


    return index, metadata

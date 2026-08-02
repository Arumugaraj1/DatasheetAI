import pickle
import faiss
import numpy as np

from src.embedding import create_embeddings


INDEX_PATH = "vector_db/datasheet.index"
CHUNK_PATH = "vector_db/chunks.pkl"


def retrieve(query, top_k=15):
    """
    Search the FAISS vector database and return the most relevant chunks.
    """

    # Load index
    index = faiss.read_index(INDEX_PATH)

    # Load chunk metadata
    with open(CHUNK_PATH, "rb") as f:
        chunks = pickle.load(f)

    # Create embedding for the user query
    query_embedding = create_embeddings([query]).astype(np.float32)

    # Search
    scores, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        if idx >= 0:
            results.append(chunks[idx])

    return results
import os
import pickle
import faiss
import numpy as np

VECTOR_FOLDER = "vector_db"
os.makedirs(VECTOR_FOLDER, exist_ok=True)

def save_vector_db(chunks, embeddings):

    print("========== SAVE VECTOR DB ==========")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)

    index.add(np.array(embeddings).astype("float32"))

    index_path = os.path.join(VECTOR_FOLDER, "datasheet.index")
    chunk_path = os.path.join(VECTOR_FOLDER, "chunks.pkl")

    faiss.write_index(index, index_path)

    with open(chunk_path, "wb") as f:
        pickle.dump(chunks, f)

    print("Index Saved :", index_path)
    print("Chunks Saved:", chunk_path)

    return len(chunks)
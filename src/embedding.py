from sentence_transformers import SentenceTransformer
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "all-MiniLM-L6-v2"

print(f"Loading embedding model from: {MODEL_PATH}")

model = SentenceTransformer(
    str(MODEL_PATH),
    local_files_only=True
)

print("✅ Embedding model loaded successfully.")


def create_embeddings(texts):
    return model.encode(
        texts,
        batch_size=16,
        show_progress_bar=False,
        convert_to_numpy=True,
        normalize_embeddings=True
    )
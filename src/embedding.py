from sentence_transformers import SentenceTransformer
import streamlit as st

# ------------------------------------------
# Load embedding model only once
# ------------------------------------------
@st.cache_resource
def load_model():
    print("Loading embedding model...")
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    print("Embedding model loaded successfully.")
    return model

model = load_model()

# ------------------------------------------
# Create embeddings
# ------------------------------------------
def create_embeddings(texts):
    """
    Generate normalized embeddings for a list of text strings.
    """

    embeddings = model.encode(
        texts,
        batch_size=16,
        show_progress_bar=False,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embeddings
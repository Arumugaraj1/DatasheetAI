import os
import streamlit as st

from src.utils.file_manager import save_uploaded_file
from src.pdf.pdf_reader import read_pdf
from src.chunker import create_chunks
from src.embedding import create_embeddings
from src.vector_store import save_vector_db


def upload_page():

    st.header("📄 Upload Datasheet")

    uploaded_file = st.file_uploader(
        "Choose a PDF Datasheet",
        type=["pdf"]
    )

    if uploaded_file is not None:

        # Save PDF
        filepath = save_uploaded_file(uploaded_file)

        st.success(f"Uploaded: {uploaded_file.name}")

        st.write("### Step 1 : Reading PDF")
        pages = read_pdf(filepath)
        st.success(f"✅ Total Pages : {len(pages)}")

        st.write("### Step 2 : Creating Chunks")
        chunks = create_chunks(pages)
        st.success(f"✅ Total Chunks : {len(chunks)}")

        st.write("### Step 3 : Creating Embeddings")

        #texts = [chunk["text"] for chunk in chunks]
        chunks = chunks[:10]   # Test with only the first 10 chunks
        texts = [chunk["text"] for chunk in chunks]

        embeddings = create_embeddings(texts)

        st.success(f"✅ Embeddings Created : {embeddings.shape}")

        st.write("### Step 4 : Saving FAISS Index")

        total = save_vector_db(chunks, embeddings)

        st.success(f"✅ Vector DB Saved ({total} chunks)")

        st.write("### Step 5 : Checking Files")

        if os.path.exists("vector_db/datasheet.index"):
            st.success("✅ datasheet.index created")
        else:
            st.error("❌ datasheet.index NOT found")

        if os.path.exists("vector_db/chunks.pkl"):
            st.success("✅ chunks.pkl created")
        else:
            st.error("❌ chunks.pkl NOT found")

        st.divider()

        st.subheader("Uploaded PDFs")

        for pdf in os.listdir("uploads"):
            st.write("📄", pdf)
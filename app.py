import streamlit as st
from src.ui.upload_ui import upload_page
from src.retriever import retrieve
from src.llm import ask_llm

st.set_page_config(page_title="Datasheet AI", layout="wide")

st.title("📘 Datasheet AI Assistant")

menu = st.sidebar.radio(
    "Menu",
    ["Upload Datasheet", "Ask Questions"]
)

if menu == "Upload Datasheet":
    upload_page()

else:

    st.header("💬 Ask Questions")

    question = st.text_input(
        "Enter your question"
    )

    if st.button("Ask AI"):

        if question == "":
            st.warning("Please enter a question.")
            st.stop()

        with st.spinner("Searching Datasheet..."):

            chunks = retrieve(question)

        context = ""

        for chunk in chunks:
            context += f"\n\nPage {chunk['page']}\n"
            context += chunk["text"]

        with st.spinner("Generating Answer..."):

            answer = ask_llm(question, context)

        st.success("Answer")

        st.write(answer)

        st.divider()

        st.subheader("Source Chunks")

        for chunk in chunks:

            with st.expander(f"Page {chunk['page']}"):

                st.write(chunk["text"])
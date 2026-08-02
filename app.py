
import streamlit as st
import os

from src.ui.upload_ui import upload_page

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="CTS Engineering AI Copilot",
    page_icon="⚡",
    layout="wide"
)

# -----------------------------
# Load CSS
# -----------------------------
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2721/2721297.png",
        width=80
    )

    st.title("CTS AI")

    st.markdown("---")

    st.success("🟢 Gemini Connected")

    st.success("🟢 FAISS Ready")

    st.success("🟢 Embeddings Ready")

    st.markdown("---")

    st.write("### 📂 Datasheets")

    if os.path.exists("uploads"):
        files = os.listdir("uploads")

        if len(files):

            for f in files:
                st.write("📘", f)

        else:

            st.info("No datasheets uploaded")

# -----------------------------
# Header
# -----------------------------
st.markdown(
    """
<div class="title">
⚡ CTS Engineering AI Copilot
</div>

<div class="subtitle">
Professional AI Assistant for Electronics Engineers
</div>
""",
unsafe_allow_html=True
)

st.divider()

# -----------------------------
# Dashboard Cards
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

pdfs = len(os.listdir("uploads")) if os.path.exists("uploads") else 0

with col1:

    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-title">📂 Datasheets</div>
<div class="metric-value">{pdfs}</div>
</div>
""",
unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
<div class="metric-card">
<div class="metric-title">🤖 Gemini</div>
<div class="status">ONLINE</div>
</div>
""",
unsafe_allow_html=True
    )

with col3:

    st.markdown(
        """
<div class="metric-card">
<div class="metric-title">🧠 Embeddings</div>
<div class="status">READY</div>
</div>
""",
unsafe_allow_html=True
    )

with col4:

    st.markdown(
        """
<div class="metric-card">
<div class="metric-title">📦 Vector DB</div>
<div class="status">ACTIVE</div>
</div>
""",
unsafe_allow_html=True
    )

st.divider()

# -----------------------------
# Upload Section
# -----------------------------
upload_page()
=======
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


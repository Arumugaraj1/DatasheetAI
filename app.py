import os
import streamlit as st

from src.ui.upload_ui import upload_page
from src.retriever import retrieve
from src.llm import ask_llm

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="CTS Engineering AI Assistant",
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

        if files:
            for f in files:
                st.write("📘", f)
        else:
            st.info("No datasheets uploaded")

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="title">
⚡ CTS Engineering AI Copilot
</div>

<div class="subtitle">
Professional AI Assistant for Electronics Engineers
</div>
""", unsafe_allow_html=True)

st.divider()

# -----------------------------
# Dashboard Cards
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

pdfs = len(os.listdir("uploads")) if os.path.exists("uploads") else 0

with col1:
    st.markdown(f"""
<div class="metric-card">
<div class="metric-title">📂 Datasheets</div>
<div class="metric-value">{pdfs}</div>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="metric-card">
<div class="metric-title">🤖 Gemini</div>
<div class="status">ONLINE</div>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="metric-card">
<div class="metric-title">🧠 Embeddings</div>
<div class="status">READY</div>
</div>
""", unsafe_allow_html=True)

with col4:
    st.markdown("""
<div class="metric-card">
<div class="metric-title">📦 Vector DB</div>
<div class="status">ACTIVE</div>
</div>
""", unsafe_allow_html=True)

st.divider()

# -----------------------------
# Navigation
# -----------------------------
menu = st.sidebar.radio(
    "Navigation",
    ["📤 Upload Datasheet", "💬 Ask Questions"]
)

# -----------------------------
# Upload Page
# -----------------------------
if menu == "📤 Upload Datasheet":

    upload_page()

# -----------------------------
# Ask AI
# -----------------------------
else:

    st.header("💬 Engineering AI Assistant")

    st.write(
        "Ask any question about your uploaded electronics datasheets."
    )

    # Check Vector DB
    if not os.path.exists("vector_db/datasheet.index"):

        st.info("""
### 📂 No Datasheet Indexed

Upload one or more PDF datasheets first.

After indexing, you can ask questions such as:

• What is the operating voltage?

• Explain the LED driver.

• What is the register configuration?

• What is the maximum current?

• Explain the power supply section.

• Give PCB design guidelines.
""")

    question = st.text_input(
        "Ask your engineering question..."
    )

    ask = st.button(
        "🚀 Ask AI",
        use_container_width=True
    )

    if ask:

        if question.strip() == "":
            st.warning("Please enter a question.")
            st.stop()

        if not os.path.exists("vector_db/datasheet.index"):
            st.error(
                "No indexed datasheet found.\n\nPlease upload a PDF first."
            )
            st.stop()

        with st.spinner("🔍 Searching Datasheets..."):

            chunks = retrieve(question)

        context = ""

        for chunk in chunks:

            context += f"\n\nPage {chunk['page']}\n"
            context += chunk["text"]

        with st.spinner("🤖 Gemini is generating the answer..."):

            answer = ask_llm(question, context)

        st.success("✅ AI Answer")

        st.markdown(answer)

        st.divider()

        st.subheader("📄 Source Pages")

        for chunk in chunks:

            with st.expander(
                f"📘 Page {chunk['page']}"
            ):

                st.write(chunk["text"])
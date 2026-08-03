import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    try:
        api_key = st.secrets.get("GOOGLE_API_KEY")
    except Exception:
        api_key = None

model = None

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")


def ask_llm(question, context):
    if model is None:
        message = (
            "Gemini API key is not configured. Add GOOGLE_API_KEY to your environment or Streamlit secrets."
        )
        st.error(message)
        return message

    prompt = f"""
You are a senior electronics engineer.

Use ONLY the datasheet context below to answer.

Context:
{context}

Question:
{question}

Provide:
1. Direct Answer
2. Detailed Explanation
3. Technical Notes
4. Important Precautions
5. Design Recommendations
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as exc:
        message = (
            f"Gemini request failed. Please replace the current API key with a valid one. "
            f"Details: {exc}"
        )
        st.error(message)
        return message
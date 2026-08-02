import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_llm(question, context):
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

    response = model.generate_content(prompt)
    return response.text
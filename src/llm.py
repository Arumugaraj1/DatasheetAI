import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# -------------------------------------------------
# Load API Key
# -------------------------------------------------
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        api_key = None

client = None

if api_key:
    client = Groq(api_key=api_key)


# -------------------------------------------------
# Ask LLM
# -------------------------------------------------
def ask_llm(question, context):

    if client is None:
        return (
            "❌ GROQ_API_KEY not found.\n\n"
            "Add GROQ_API_KEY to your .env file or Streamlit Secrets."
        )

    prompt = f"""
You are a Senior Electronics Hardware Engineer.

Answer ONLY using the datasheet context below.

If the answer is not present, reply:

"The uploaded datasheet does not contain this information."

======================
DATASHEET CONTEXT
======================

{context}

======================
QUESTION
======================

{question}

======================
RESPONSE FORMAT
======================

## Direct Answer

## Detailed Explanation

## Design Notes

## Important Precautions

## Source Summary
"""

    try:

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "system",
                    "content":
                    "You are an expert Electronics Design Engineer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.2,

            max_tokens=2048
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"❌ LLM Error:\n\n{e}"
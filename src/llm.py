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
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_llm(question, context):

    prompt = f"""
You are an expert Semiconductor Hardware Engineer.

Answer ONLY using the datasheet context below.

If the answer is not present, reply:

'I could not find this information in the uploaded datasheet.'

Context:

{context}

Question:

{question}

Answer professionally.

Include:
- Explanation
- Important Notes
- Design Precautions
- Technical Considerations
"""

    response = model.generate_content(prompt)

    return response.text
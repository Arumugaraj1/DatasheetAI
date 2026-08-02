from src.retriever import retrieve
from src.llm import ask_llm


def ask(question):

    chunks = retrieve(question)

    context = ""

    for chunk in chunks:
        context += f"\n\nPage {chunk['page']}\n"
        context += chunk["text"]

    answer = ask_llm(question, context)

    return answer, chunks
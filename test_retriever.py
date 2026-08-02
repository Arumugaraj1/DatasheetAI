from src.retriever import retrieve

question = "What is the operating voltage?"

print("Question:", question)
print("=" * 80)

results = retrieve(question)

for i, chunk in enumerate(results, start=1):
    print(f"\nResult {i}")
    print(f"Page: {chunk['page']}")
    print("-" * 80)
    print(chunk["text"])
    print("=" * 80)
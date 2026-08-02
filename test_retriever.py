<<<<<<< HEAD
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
=======
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
>>>>>>> a978eb5f68f29b5c72f8ca5b8096ec8a2f97787c
    print("=" * 80)
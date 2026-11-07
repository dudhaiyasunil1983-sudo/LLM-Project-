from sentence_transformers import SentenceTransformer, util
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

questions=[
    "whay is the machine learning?",
]
answers=[
    "Machine learning is a subset of artificial intelligence that focuses on building systems that can learn from data and improve their performance over time without being explicitly programmed.",
]

embeddings = model.encode(questions).astype("float32")

index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)
faise.normalize_L2(embeddings)

query = "Explain the concept of machine learning."
quety_vector = model.encode([query]).astype("float32")
faiss.normalize_L2(quety_vector)

scores,idx= index.search(quety_vector, k=1)

if scores[0][0] > 0.5:
    print("Answer:", answers[idx[0][0]])
    print("Score:", scores[0][0])
else:
    print("No relevant answer found.")


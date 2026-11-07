from sentence_transformers import SentenceTransformer, util
import faiss

docs=[
    " I love machine learning.",
    "Dogs are great pets.",
    "Nueral networks are a subset of machine learning.",
]

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(docs, convert_to_tensor=True)
index = faiss.IndexFlatIP(256)  # Assuming 256-dimensional embeddings
index.add(embeddings.cpu().numpy())

query = model.encode("I enjoy studying AI.", convert_to_tensor=True)

D, I = index.search(query.cpu().numpy(), k=2)
print(I)

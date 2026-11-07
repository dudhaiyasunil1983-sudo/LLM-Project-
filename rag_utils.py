from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")  # small, fast, free

def chunk(text, n=800):
    return [text[i:i+n] for i in range(0, len(text), n)]def embed(texts):
    return model.encode(texts, normalize_embeddings=True)

def top_k(query, texts, embs, k=4):
    q = model.encode([query], normalize_embeddings=True)[0]
    sims = embs @ q
    idx = sims.argsort()[-k:][::-1]
    return [(texts[i], float(sims[i])) for i in idx]
# src/embedder.py
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

class Embedder:
    def __init__(self, model_path="./models/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_path)

    def rank_sections(self, query, sections, top_k=5):
        section_texts = [s["text"] for s in sections]
        section_embeddings = self.model.encode(section_texts)
        query_embedding = self.model.encode([query])[0]

        scores = cosine_similarity([query_embedding], section_embeddings)[0]
        ranked = sorted(
            zip(sections, scores),
            key=lambda x: x[1],
            reverse=True
        )
        top_sections = [{
            "document": s.get("document"),
            "section_title": s["text"][:80],
            "importance_rank": i + 1,
            "page_number": s["page"],
            "score": float(score)
        } for i, (s, score) in enumerate(ranked[:top_k])]
        
        return top_sections

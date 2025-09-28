import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class SemanticSearch:
    def __init__(self, embeddings, texts):
        self.embeddings = embeddings
        self.texts = texts

    def search(self, query_embedding, top_k=3):
        sims = cosine_similarity([query_embedding], self.embeddings)[0]
        idxs = sims.argsort()[::-1][:top_k]
        return [(self.texts[i], sims[i]) for i in idxs]

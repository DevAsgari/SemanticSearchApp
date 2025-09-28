import faiss
import numpy as np


class SemanticSearch:
    def __init__(self, embeddings, texts):
        self.texts = texts
        self.dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(self.dimension)
        faiss.normalize_L2(embeddings)
        self.index.add(embeddings)

    def search(self, query_embedding, top_k=3):
        query = np.array([query_embedding]).astype("float32")
        faiss.normalize_L2(query)
        distances, indices = self.index.search(query, top_k)
        results = [
            (self.texts[i], float(distances[0][j])) for j, i in enumerate(indices[0])
        ]
        return results

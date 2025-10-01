from sentence_transformers import SentenceTransformer


class Embedder:
    def __init__(self, model="sentence-transformers/all-mpnet-base-v2"):
        self.model = SentenceTransformer(model)

    def __call__(self, texts):
        return self.model.encode(texts)

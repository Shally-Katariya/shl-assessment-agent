from sentence_transformers import SentenceTransformer
from typing import List


class EmbeddingService:
    """
    Wrapper around SentenceTransformer.
    Responsible only for generating embeddings.
    """

    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5"):
        print(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, documents: List[str]):
        """
        Generate embeddings for multiple documents.
        """
        return self.model.encode(
            documents,
            normalize_embeddings=True,
            show_progress_bar=True,
        )

    def embed_query(self, query: str):
        """
        Generate embedding for a single query.
        """
        return self.model.encode(
            query,
            normalize_embeddings=True,
        )
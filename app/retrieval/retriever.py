import json
from pathlib import Path

import faiss
import numpy as np

from app.retrieval.embedder import EmbeddingService


INDEX_FILE = Path("data/processed/index.faiss")
METADATA_FILE = Path("data/processed/metadata.json")


class Retriever:
    """
    Semantic search over SHL assessments using FAISS.
    """

    def __init__(self):
        print("Loading FAISS index...")

        self.index = faiss.read_index(str(INDEX_FILE))

        print("Loading metadata...")

        with open(METADATA_FILE, "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

        self.embedder = EmbeddingService()

        print(f"Loaded {len(self.metadata)} assessments.")

    def search(self, query: str, top_k: int = 5):
        """
        Search the most relevant SHL assessments.

        Args:
            query: User search query
            top_k: Number of results to return

        Returns:
            List of matching assessments.
        """

        print(f"Searching for: {query}")

        # Generate embedding for the query
        query_embedding = self.embedder.embed_query(query)

        # FAISS expects float32 with shape (1, embedding_dim)
        query_embedding = np.asarray([query_embedding]).astype("float32")

        # Search the index
        scores, indices = self.index.search(query_embedding, top_k)

        results = []

        for score, idx in zip(scores[0], indices[0]):
            if idx == -1:
                continue

            assessment = self.metadata[idx].copy()
            assessment["score"] = float(score)

            results.append(assessment)

        return results
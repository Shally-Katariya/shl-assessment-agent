import json
from pathlib import Path

import faiss
import numpy as np

from app.retrieval.embedder import EmbeddingService


DOCUMENTS_FILE = Path("data/processed/documents.json")

OUTPUT_DIR = Path("data/processed")

INDEX_FILE = OUTPUT_DIR / "index.faiss"

METADATA_FILE = OUTPUT_DIR / "metadata.json"


def main():
    print("Loading processed documents...")

    with open(DOCUMENTS_FILE, "r", encoding="utf-8") as f:
        documents = json.load(f)

    print(f"Loaded {len(documents)} documents.")

    # Extract text for embedding
    texts = [doc["document"] for doc in documents]

    print(f"Prepared {len(texts)} documents for embedding.")

    # Load embedding model
    embedder = EmbeddingService()

    print("Generating embeddings...")

    # Generate embeddings
    embeddings = embedder.embed_documents(texts)

    print(f"Generated embeddings for {len(embeddings)} documents.")

    # Convert embeddings to float32 (required by FAISS)
    embeddings = np.asarray(embeddings).astype("float32")

    print(f"Embedding matrix shape: {embeddings.shape}")

    # Create FAISS index
    dimension = embeddings.shape[1]

    # Inner Product (Cosine Similarity because embeddings are normalized)
    index = faiss.IndexFlatIP(dimension)

    # Add all document vectors
    index.add(embeddings)

    print(f"Created FAISS index with {index.ntotal} vectors.")

    # Save FAISS index
    faiss.write_index(index, str(INDEX_FILE))

    print(f"Saved FAISS index to {INDEX_FILE}")

    # Save metadata
    with open(METADATA_FILE, "w", encoding="utf-8") as f:
        json.dump(documents, f, indent=2, ensure_ascii=False)

    print(f"Saved metadata to {METADATA_FILE}")

    print("=" * 50)
    print("Index build completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
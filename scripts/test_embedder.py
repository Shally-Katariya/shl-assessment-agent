from app.retrieval.embedder import EmbeddingService


def main():
    embedder = EmbeddingService()

    docs = [
        "Java programming assessment",
        "Leadership personality assessment",
    ]

    embeddings = embedder.embed_documents(docs)

    print("Embedding shape:", embeddings.shape)

    query = embedder.embed_query("Java Developer")

    print("Query shape:", query.shape)


if __name__ == "__main__":
    main()
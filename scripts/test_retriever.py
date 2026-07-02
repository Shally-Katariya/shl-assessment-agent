from app.retrieval.retriever import Retriever


def main():
    retriever = Retriever()

    results = retriever.search(
        "Java developer with leadership skills",
        top_k=5,
    )

    print("\nTop Results\n")

    for i, result in enumerate(results, start=1):
        print("=" * 60)
        print(f"Rank: {i}")
        print(f"Score: {result['score']:.4f}")
        print(f"Name: {result['name']}")
        print(f"URL: {result['url']}")
        print(f"Categories: {', '.join(result['categories'])}")
        print()


if __name__ == "__main__":
    main()
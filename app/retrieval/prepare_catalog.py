import json
from pathlib import Path

from app.models.assessment import Assessment


RAW_CATALOG = Path("data/shl_catalog.json")

OUTPUT_DIR = Path("data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "documents.json"


def build_document(a: Assessment) -> dict:
    """
    Convert one SHL assessment into a retrieval-friendly document.
    """

    text = f"""
Assessment Name:
{a.name}

Description:
{a.description}

Job Levels:
{", ".join(a.job_levels) if a.job_levels else "Not specified"}

Languages:
{", ".join(a.languages) if a.languages else "Any"}

Assessment Categories:
{", ".join(a.keys) if a.keys else "Not specified"}

Adaptive Testing:
{a.adaptive}

Duration:
{a.duration if a.duration else "Not specified"}
""".strip()

    return {
        "id": a.entity_id,
        "name": a.name,
        "url": a.link,
        "job_levels": a.job_levels,
        "languages": a.languages,
        "adaptive": a.adaptive,
        "duration": a.duration,
        "categories": a.keys,
        "document": text,
    }


def main():
    with open(RAW_CATALOG, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    documents = []

    for item in catalog:
        assessment = Assessment(**item)
        documents.append(build_document(assessment))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(documents, f, indent=2, ensure_ascii=False)

    print("=" * 50)
    print(f"Processed assessments : {len(documents)}")
    print(f"Saved file            : {OUTPUT_FILE}")
    print("=" * 50)


if __name__ == "__main__":
    main()
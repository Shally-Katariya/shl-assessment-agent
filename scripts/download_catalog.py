import json
from pathlib import Path

import requests

CATALOG_URL = (
    "https://tcp-us-prod-rnd.shl.com/voiceRater/shl-ai-hiring/"
    "shl_product_catalog.json"
)

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = DATA_DIR / "shl_catalog.json"


def main():
    print("Downloading SHL catalog...")

    response = requests.get(CATALOG_URL, timeout=30)
    response.raise_for_status()

    text = response.text

    print(f"Downloaded {len(text)} characters")

    # Save raw response
    raw_file = DATA_DIR / "shl_catalog_raw.json"
    raw_file.write_text(text, encoding="utf-8")

    print(f"Raw catalog saved to {raw_file}")

    # Parse JSON (allow invalid control characters)
    catalog = json.loads(text, strict=False)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)

    print(f"Saved cleaned catalog to {OUTPUT_FILE}")

    if isinstance(catalog, list):
        print(f"\nTotal assessments: {len(catalog)}")
        print("\nFields:")
        print(list(catalog[0].keys()))

        print("\nSample Assessment:")
        print(json.dumps(catalog[0], indent=2)[:1200])


if __name__ == "__main__":
    main()
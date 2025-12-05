import pandas as pd

INPUT_PATH = "data/processed/combined.csv"
OUTPUT_PATH = "data/processed/cleaned.csv"

def clean_dataset():
    print("[1] Loading dataset...")
    df = pd.read_csv(INPUT_PATH)
    print(f"Loaded {len(df):,} rows\n")

    # Remove exact duplicates
    print("[2] Dropping duplicate rows...")
    df = df.drop_duplicates()
    print(f"Rows after deduplication: {len(df):,}\n")

    # Convert publish_date if present
    if "publish_date" in df.columns:
        print("[3] Converting publish_date to datetime...")
        df["publish_date"] = pd.to_datetime(df["publish_date"], errors="coerce")
        print("publish_date conversion complete.\n")

    # Convert snapshot_date if present
    if "snapshot_date" in df.columns:
        print("[4] Converting snapshot_date to datetime...")
        df["snapshot_date"] = pd.to_datetime(df["snapshot_date"], errors="coerce")
        print("snapshot_date conversion complete.\n")

    # Create engagement column
    if "like_count" in df.columns and "comment_count" in df.columns:
        print("[5] Creating engagement = likes + comment_count...")
        df["engagement"] = df["like_count"] + df["comment_count"]
        print("Engagement column created.\n")

    # Remove rows missing critical fields
    critical_columns = ["title", "view_count"]
    print("[6] Dropping rows missing critical fields...")

    for col in critical_columns:
        if col in df.columns:
            before = len(df)
            df = df.dropna(subset=[col])
            after = len(df)
            print(f" - Removed {before - after:,} rows missing '{col}'")

    print()

    # Save the cleaned dataset
    print("[7] Saving cleaned dataset...")
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Cleaned dataset saved to {OUTPUT_PATH}\n")

    print("CLEANING COMPLETE ✔")

if __name__ == "__main__":
    clean_dataset()

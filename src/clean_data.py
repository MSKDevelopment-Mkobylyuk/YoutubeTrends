import pandas as pd

INPUT_PATH = "data/processed/combined.csv"
OUTPUT_PATH = "data/processed/cleaned.csv"

def clean_dataset():
    # Load the combined dataset
    df = pd.read_csv(INPUT_PATH)
    
    # Remove exact duplicate rows
    df = df.drop_duplicates()
    # Prevents inflated counts and keeps analysis accurate

    if "publish_time" in df.columns:
        df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")

    if "trending_date" in df.columns:
        df["trending_date"] = pd.to_datetime(df["trending_date"], errors="coerce")
    # Checks if the column exists; converts string timestamps into actual datetime objects; 
    # avoids crashes and replaces bad data with NaT

    if "likes" in df.columns and "comment_count" in df.columns:
        df["engagement"] = df["likes"] + df["comment_count"]

    # Remove rows that are missing critical fields
    critical_columns = ["title", "views"]

    for col in critical_columns:
        if col in df.columns:
            df = df.dropna(subset=[col])
    df.to_csv(OUTPUT_PATH, index=False)
    
if __name__ == "__main__":
    clean_dataset()
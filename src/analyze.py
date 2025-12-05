import pandas as pd
import json
import os

INPUT_PATH = "data/processed/cleaned.csv"

OUTPUT_DIR = "outputs/analysis/"
# High-level summary of the dataset saved as JSON
SUMMARY_JSON = os.path.join(OUTPUT_DIR, "summary.json")
# Aggregated statistics for YouTube channels saved as CSV 
TOP_CHANNELS_CSV = os.path.join(OUTPUT_DIR, "top_channels.csv")

def analyze_dataset():
    # Load the cleaned dataset
    df = pd.read_csv(INPUT_PATH)

    # Ensure the output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Summary statistics (adjusted for your dataset's column names)
    summary = {
        "total_rows": len(df),
        "total_unique_videos": df["title"].nunique() if "title" in df.columns else None,
        "avg_views": df["view_count"].mean() if "view_count" in df.columns else None,
        "avg_likes": df["like_count"].mean() if "like_count" in df.columns else None,
        "avg_comment_count": df["comment_count"].mean() if "comment_count" in df.columns else None,
    }

    # Save summary to JSON
    with open(SUMMARY_JSON, "w") as f:
        json.dump(summary, f, indent=4)

    # Top channels by total views
    if "channel_name" in df.columns and "view_count" in df.columns:
        print("Channel block entered")
        top_channels = (
            df.groupby("channel_name")
            .agg(
                total_views=("view_count", "sum"),
                avg_views=("view_count", "mean"),
                total_likes=("like_count", "sum"),
                total_comments=("comment_count", "sum")
            )
            .sort_values(by="total_views", ascending=False)
        )

        top_channels.to_csv(TOP_CHANNELS_CSV)

if __name__ == "__main__":
    analyze_dataset()
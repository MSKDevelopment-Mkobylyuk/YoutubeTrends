import pandas as pd
import matplotlib.pyplot as plt
import os

INPUT_PATH = "data/processed/cleaned.csv"
OUTPUT_DIR = "outputs/charts/"

def visualize():
    # Load the cleaned dataset
    df = pd.read_csv(INPUT_PATH)

    # Make sure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Top 20 Channels 
    if "channel_name" in df.columns and "view_count" in df.columns:
        top_channels = (
            df.groupby("channel_name")["view_count"]
            .sum()
            .sort_values(ascending=False)
            .head(20)
        )

        plt.figure(figsize=(12,6))
        top_channels.plot(kind="bar")
        plt.title("Top 20 Youtube Channels by Total Views")
        plt.xlabel("Channel Name")
        plt.ylabel("Total Views")
        plt.xticks(rotation=75)
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_DIR, "top_channels_views.png"))
        plt.close()

    # View count distribution
    if "view_count" in df.columns:
        plt.figure(figsize=(10,5))
        df["view_count"].plot(kind="hist", bins=50)
        plt.title("Distribution of Video View Counts")
        plt.xlabel("View Count")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_DIR, "view_count_distribution.png"))
        plt.close()

    # Likes vs Views (Scatter Plot)
    if "view_count" in df.columns and "like_count" in df.columns:
        plt.figure(figsize=(10,6))
        plt.scatter(df["view_count"], df["like_count"], alpha=0.3)
        plt.title("Likes vs Views")
        plt.xlabel("Views")
        plt.ylabel("Likes")
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_DIR, "likes_vs_views.png"))
        plt.close()

if __name__ == "__main__":
    visualize()
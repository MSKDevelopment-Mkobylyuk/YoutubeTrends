import os
import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

SUMMARY_PATH = "outputs/analysis/summary.json"
CHARTS_DIR = "outputs/charts/"
OUTPUT_DIR = "outputs/reports/"
OUTPUT_PDF = os.path.join(OUTPUT_DIR, "youtube_report.pdf")

def generate_report():
    # Make sure output folder exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load summary JSON
    with open(SUMMARY_PATH, "r") as f:
        summary = json.load(f)

    # Create PDF
    c = canvas.Canvas(OUTPUT_PDF, pagesize=letter)
    width, height = letter

    # ------------------------------
    # PAGE 1 – Title + Summary Stats
    # ------------------------------
    c.setFont("Helvetica-Bold", 22)
    c.drawString(50, height - 50, "YouTube Trends Analysis Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Total Rows: {summary['total_rows']}")
    c.drawString(50, height - 120, f"Unique Videos: {summary['total_unique_videos']}")
    c.drawString(50, height - 140, f"Average Views: {round(summary['avg_views'], 2)}")
    c.drawString(50, height - 160, f"Average Likes: {round(summary['avg_likes'], 2)}")
    c.drawString(50, height - 180, f"Average Comment Count: {round(summary['avg_comment_count'], 2)}")

    c.showPage()

    # ------------------------------
    # PAGE 2 – Top Channels Chart
    # ------------------------------
    top_channels_chart = os.path.join(CHARTS_DIR, "top_channels_views.png")
    if os.path.exists(top_channels_chart):
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height - 50, "Top 20 Channels by Total Views")

        img = ImageReader(top_channels_chart)
        c.drawImage(img, 50, 150, width=500, preserveAspectRatio=True, mask='auto')

        c.showPage()

    # ------------------------------
    # PAGE 3 – View Count Distribution
    # ------------------------------
    dist_chart = os.path.join(CHARTS_DIR, "view_count_distribution.png")
    if os.path.exists(dist_chart):
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height - 50, "Distribution of Video View Counts")

        img = ImageReader(dist_chart)
        c.drawImage(img, 50, 150, width=500, preserveAspectRatio=True, mask='auto')

        c.showPage()

    # ------------------------------
    # PAGE 4 – Likes vs Views Scatter
    # ------------------------------
    scatter_chart = os.path.join(CHARTS_DIR, "likes_vs_views.png")
    if os.path.exists(scatter_chart):
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height - 50, "Likes vs Views")

        img = ImageReader(scatter_chart)
        c.drawImage(img, 50, 150, width=500, preserveAspectRatio=True, mask='auto')

        c.showPage()

    # Save the final PDF
    c.save()
    print(f"Report saved to: {OUTPUT_PDF}")

if __name__ == "__main__":
    generate_report()

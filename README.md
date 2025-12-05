This project is an end-to-end Python analytics pipeline designed to process YouTube trending video data from any CSV dataset. It supports a single file or multiple files and produces:

A clean, combined dataset

Exploratory insights (categories, channels, engagement patterns)

Visualizations saved as PNGs

An automated HTML report

A reproducible pipeline using modular Python scripts

The project was built to demonstrate practical skills in Python, data engineering, data analysis, and reporting automation.

Features
Data Ingestion

Loads one or many raw CSV files

Automatically tracks the original source file

Combines all data into a single processed dataset

Data Cleaning

Removes duplicates

Converts dates

Adds computed features (e.g., engagement metrics)

Handles missing values

Analysis & Insights

Top trending categories

Most frequent channels

Engagement distributions

High-level dataset statistics

Visualization

Matplotlib / Seaborn charts generated automatically

Saved to outputs/charts/

Automated Reporting

HTML report generated with Jinja2

Embeds charts and summary tables

Saved to outputs/reports/

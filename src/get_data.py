import pandas as pd
import os

RAW_DATA_PATH = "data/raw/"
OUTPUT_PATH = "data/processed/combined.csv"

def load_raw_files():
    files = [f for f in os.listdir(RAW_DATA_PATH) if f.endswith(".csv")] # lists all files within data/raw/
    dataframes = []

    # Loop through each CSV file in the raw data folder
    for file in files:
        file_path = os.path.join(RAW_DATA_PATH, file)

        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Add a column indicating which file the data came from
        df["source_file"] = file

        # Store the DataFrame in our list
        dataframes.append(df)

    # Combine all DataFrames into one
    combined_df = pd.concat(dataframes, ignore_index=True)
    # concat will stack the DataFrames vertically row by row
    # ignoring index resets row numbering so its clean and sequential

    # Save the combined dataset into the processed folder
    combined_df.to_csv(OUTPUT_PATH, index=False) 
    # index false will prevent pandas from adding an extra column of row numbers

if __name__ == "__main__":
    load_raw_files()


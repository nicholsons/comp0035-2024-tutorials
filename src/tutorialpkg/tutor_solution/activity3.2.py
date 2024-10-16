import pandas as pd
import matplotlib as plt
from pathlib import Path

target_file = "paralympics_events_raw.csv"

def readcsv(target_file):
    # Filepath of the csv data file
    try:
        datafile_csv = Path.Path(__file__).parent.parent.joinpath("data", target_file)
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

    # Read the data from the file into a Pandas dataframe
    events_csv_df = pd.read_csv(datafile_csv)
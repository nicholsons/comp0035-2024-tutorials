import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def readcsv(target_file):
    # Filepath of the csv data file
    try:
        datafile_csv = Path(__file__).parent.parent.joinpath("data", target_file)
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

    # Read the data from the file into a Pandas dataframe
    return(pd.read_csv(datafile_csv))

if __name__ == '__main__':
    target_file = "paralympics_events_raw.csv"
    df = readcsv(target_file)
    df.hist()
    df["year"].hist()
    plt.show()

    # Filter the DataFrame to select only rows where 'type' is 'summer'
    # syntax: df = df[df['column_name'] == filter_value]
    summer_df = df[df['type'] == 'summer']
    summer_df.hist()
    plt.show()
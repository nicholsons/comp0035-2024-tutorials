from pathlib import Path
import pandas as pd


def describe_dataframe(df):
    print(df.shape)
    print(df.head)
    print(df.tail)
    print(df.columns)
    print(df.dtypes)
    print(df.info)
    print(df.describe)
    pass


if __name__ == "__main__":
    # Filepath of the csv data file
    try:
        paralympics_datafile_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_raw.csv")
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

    # Read the data from the file into a Pandas dataframe
    events_csv_df = pd.read_csv(paralympics_datafile_csv)
   
    # Call the function to describe the dataframe
    describe_dataframe(events_csv_df)

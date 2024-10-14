"""
Gets the datatype of the columns in the paralympics dataset.
You need to have completed the data prep activities before running this script as it assumes the prepared data is available.
"""
from pathlib import Path

import pandas as pd

if __name__ == '__main__':
    # csv
    try:
        paralympics_datafile_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_prepared.csv")
        df_paralympics = pd.read_csv(paralympics_datafile_csv)
        print(df_paralympics.dtypes)
    except FileNotFoundError as e:
        print(f"paralympics_events_prepared.csv file not found. Please check the file path. Error: {e}")

    # excel
    try:
        paralympics_datafile_excel = Path(__file__).parent.parent.joinpath("data", "paralympics_events_prepared.xlsx")
        df_paralympics_e = pd.read_excel(paralympics_datafile_excel)
        print(df_paralympics_e.dtypes)
    except FileNotFoundError as e:
        print(f"paralympics_events_prepared.xlsx file not found. Please check the file path. Error: {e}")

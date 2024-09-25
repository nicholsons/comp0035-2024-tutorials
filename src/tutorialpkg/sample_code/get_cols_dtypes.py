from importlib.resources import files
from pathlib import Path

import pandas as pd

if __name__ == '__main__':
    # csv
    try:
        # This is the method used in previous examples
        # paralympics_datafile_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_prepared.csv")

        # This method is recommended in the setuptools guide:
        # https://setuptools.pypa.io/en/stable/userguide/datafiles.html#accessing-data-files-at-runtime
        paralympics_datafile_csv = files("tutorialpkg.data").joinpath("paralympics_events_prepared.csv")

        df_paralympics = pd.read_csv(paralympics_datafile_csv)
        print(df_paralympics.dtypes)
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

    # excel
    try:
        paralympics_datafile_excel = Path(__file__).parent.parent.joinpath("data", "paralympics_events_prepared.xlsx")
        df_paralympics_e = pd.read_excel(paralympics_datafile_excel)
        print(df_paralympics_e.dtypes)
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

"""
This is an example of using importlib.resources versus pathlib to access data files in the package.
"""

from importlib.resources import files
from pathlib import Path

import pandas as pd

if __name__ == '__main__':
    # Read file using  pathlib
    try:
        paralympics_datafile_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_raw.csv")
        df_paralympics = pd.read_csv(paralympics_datafile_csv)
        print("Successfully found the file using pathlib.")
        print(df_paralympics.head(1))
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

    # Read file using importlib.resources
    # This method is recommended in the setuptools guide:
    # https://setuptools.pypa.io/en/stable/userguide/datafiles.html#accessing-data-files-at-runtime
    try:
        paralympics_datafile_csv = files("tutorialpkg.data").joinpath("paralympics_events_raw.csv")
        print("Successfully found the file using importlib.resorces.")
        df_paralympics = pd.read_csv(paralympics_datafile_csv)
        print(df_paralympics.head(1))
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

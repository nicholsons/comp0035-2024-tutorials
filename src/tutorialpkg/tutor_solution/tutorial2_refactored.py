"""Refactored version of the week 2 solution for week 9 unit testing activity

Introduced smaller functions to some aspects to allow for more tests.
"""
from contextlib import redirect_stdout
from pathlib import Path

import pandas as pd


def describe_dataframe(df, output_file):
    """ Description of the contents of the data using Pandas dataframe functions.

            Read the data from the file and perform the following operations:
            - Display the first 5 rows of the dataframe
            - Display the shape of the dataframe
            - Display the column names
            - Display the data types of the columns
            - Display summary statistics
            - Display any missing values in the dataframe

        Args:
           output_file (Path) : Filepath of the file to save the description to
           df (DataFrame) : Pandas dataframe with the data in
    """
    with open(output_file, mode='w', encoding='UTF-8') as output:
        with redirect_stdout(output):
            print("\nShape of the dataframe:")
            print(df.shape)
            print("First 5 rows of the dataframe:")
            print(df.head())
            print("Last 5 rows of the dataframe:")
            print(df.tail())
            print("\nColumn names:")
            print(df.columns)
            print("\nData types of the columns:")
            print(df.dtypes)
            print("\nSummary statistics:")
            print(df.describe())
            print("Rows with missing values:")
            print(df[df.isna().any(axis=1)])
            print("\nColumns with missing values:")
            print(df.isnull().sum())


def convert_float_to_int(df):
    """Convert float64 columns to int.

    Args:
        df (DataFrame): DataFrame with float64 columns to be converted.

    Returns:
        DataFrame: DataFrame with float64 columns converted to int.
    """
    float_columns = df.select_dtypes(include=['float64']).columns
    for col in float_columns:
        try:
            df[col] = df[col].astype('int')
        except ValueError as e:
            print(f"Error converting column {col} to int: {e}")
    return df


def convert_to_datetime(df, columns, date_format='%d/%m/%Y'):
    """
    Convert columns to datetime format.
    Args:
        df: DataFrame with columns to convert
        columns: Columns to convert to datetime format
        date_format:  Date format to use for conversion

    Returns:
        df : DataFrame with columns converted to datetime format

    """
    for col in columns:
        df[col] = pd.to_datetime(df[col], format=date_format)
    return df


def clean_type_column(df):
    """Clean the 'type' column by stripping whitespace and converting to lowercase."""
    df['type'] = df['type'].str.strip().str.lower()
    return df


def add_duration_column(df, start_col, end_col):
    """Add a 'duration' column calculated from start and end dates."""
    duration_values = (df[end_col] - df[start_col]).dt.days
    df.insert(df.columns.get_loc(end_col) + 1, 'duration', duration_values)
    return df


def save_dataframe_to_file(df, file_path, file_type):
    """
    Save the dataframe to a CSV and Excel file.
    Args:
        df (pd.DataFrame): DataFrame to save
        file_path (str): Path to save the CSV or XLSX file
        file_type (str): 'csv' or 'xlsx' to specify the file type
    Raises:
        ValueError: If an invalid file type is specified
    """
    if file_type is 'csv':
        df.to_csv(file_path, index=False)
    elif file_type is 'xlsx':
        df.to_excel(file_path, index=False)
    else:
        raise ValueError("Invalid file type. Please specify 'csv' or 'xlsx'.")


def prepare_event_data(df_raw, df_npc=None):
    """Prepare the event data for analysis.

    Args:
        df_raw: Initial dataframe with paralympics data loaded from the data file
        df_npc (DataFrame): Dataframe with paralympics country code data loaded from the data file

    Returns:
        df_prepared (DataFrame): DataFrame for use in  the project
    """
    df_prepared = df_raw.drop(index=[0, 17, 31]).reset_index(drop=True)
    df_prepared = convert_float_to_int(df_prepared)
    df_prepared = convert_to_datetime(df_prepared, ['start', 'end'])

    replacements = {
        'UK': 'Great Britain',
        'USA': 'United States of America',
        'Korea': 'Republic of Korea',
        'Russia': 'Russian Federation',
        'China': "People's Republic of China"
    }
    df_prepared = df_prepared['country'] = df_prepared['country'].replace(replacements)

    if df_npc is not None:
        df_prepared = df_prepared.merge(df_npc, left_on='country', right_on='Name', how='left')

    cols_to_drop = ['URL', 'disabilities_included', 'highlights', 'Name']
    df_prepared = df_prepared.drop(columns=cols_to_drop)

    df_prepared = clean_type_column(df_prepared)
    df_prepared = add_duration_column(df_prepared, 'start', 'end')

    csv_path = Path(__file__).parent.parent.joinpath("data", "paralympics_events_prepared.csv")
    excel_path = Path(__file__).parent.parent.joinpath("data", "paralympics_events_prepared.xlsx")
    save_dataframe_to_file(df_prepared, csv_path, file_type='csv')
    save_dataframe_to_file(df_prepared, excel_path, file_type='xlsx')

    return df_prepared

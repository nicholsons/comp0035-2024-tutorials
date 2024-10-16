"""Tutorial solution for the week 2 activities.

    NB: Other solutions are possible. This is just one way to solve the task.

    For teaching purposes there are a lot of 'print' statements in the code.
    This is to show the result of steps in the code.
    In a real-world scenario, the print statements would be removed.

    Some of the solutions to later activities are in the final code in an earlier
    position. When you work through the activities, do not use any of the code indicated
    for a later solution. For example, if you are starting activity 4 then you should
    ignore lines 84-85 which are added in activity 7.
"""
import sys
from pathlib import Path

import pandas as pd

# Set the pandas display options to display all columns
pd.set_option('display.expand_frame_repr', False)
# Alternative method to display all columns, wraps to the next line
# pd.set_option("display.max_columns", None)
# pd.set_option("display.max_rows", None)


def describe_dataframe(df):
    """ Description of the contents of the data using Pandas dataframe functions.

            Read the data from the file and perform the following operations:
            - Display the first 5 rows of the dataframe
            - Display the shape of the dataframe
            - Display the column names
            - Display the data types of the columns
            - Display summary statistics
            - Display any missing values in the dataframe

           Parameters:
           data_file (Path): Filepath of the file in csv or excel format

    """

    # Display the shape of the dataframe
    print("\nShape of the dataframe:")
    print(df.shape)

    # Display the first 5 rows of the dataframe
    print("First 5 rows of the dataframe:")
    print(df.head())

    # Display the last 5 rows of the dataframe
    print("Last 5 rows of the dataframe:")
    print(df.tail())

    # Display the column names
    print("\nColumn names:")
    print(df.columns)

    # Display the data types of the columns
    print("\nData types of the columns:")
    print(df.dtypes)

    # Display summary statistics
    print("\nSummary statistics:")
    print(df.describe())

    # Display any missing values in the dataframe
    print("Rows with missing values:")
    print(df[df.isna().any(axis=1)])

    # Print columns with missing values
    print("\nColumns with missing values:")
    print(df.isnull().sum())


def prepare_event_data(df_raw, df_npc=None):
    """Prepare the event data for analysis

    Parameters:
    df_raw (DataFrame): Pandas DataFrame with the event data
    df_npc (DataFrame): Optional. Pandas DataFrame with the NPC codes data

    Returns:
    df_prepared (DataFrame): Pandas DataFrame
    """

    # Activity 7: Deal with the NaN values in the Rome row (index 0)
    # Drop the rows
    df_raw = df_raw.drop(index=[0, 17, 31])
    # Reset the index
    df_raw = df_raw.reset_index(drop=True)

    # Activity 4: Convert the data type float64 columns to int
    float_columns = df_raw.select_dtypes(include=['float64']).columns
    for col in float_columns:
        try:
            df_raw[col] = df_raw[col].astype('int')
        except ValueError as e:
            print(f"Error, can't convert column {df_raw[col].name} to int: {e}")

    print("\nData types of the float columns after conversion:")
    print(df_raw.loc[:, float_columns].dtypes)

    # Activity 4: Convert the start and end columns from object to datetime
    df_raw['start'] = pd.to_datetime(df_raw['start'], format='%d/%m/%Y')
    df_raw['end'] = pd.to_datetime(df_raw['end'], format='%d/%m/%Y')

    print("\nData types of the start/end columns after conversion:")
    print(df_raw.loc[:, ['start', 'end']].dtypes)

    # Activity 5: Merge the event data with the NPC data
    # Add the NPC code to the event data using 'merge' function and a 'left' join
    # The left dataframe is the event data and the right dataframe is the NPC code data
    # The fields to join on are 'Name' in the NPC data and 'country' in the event data

    # Activity 7: Correct the country names before doing the merge
    replacement_names = {
        'UK': 'Great Britain',
        'USA': 'United States of America',
        'Korea': 'Republic of Korea',
        'Russia': 'Russian Federation',
        'China': "People's Republic of China"
    }
    df_raw['country'] = df_raw['country'].replace(replacement_names)

    if df_npc is not None:
        df_merge = df_raw.merge(df_npc, left_on='country', right_on='Name', how='left')
        print("\nAll rows, 'country', 'Code', 'Name' columns, of the merged dataframe:")
        print(df_merge[['country', 'Code', 'Name']])

    # Activity 6: Drop the ['URL', 'disabilities_included', 'highlights'] columns
    # Activity 7: Drop the 'Name' column as the 'country' column is present and complete
    df_prepared = df_merge.drop(columns=['URL', 'disabilities_included', 'highlights', 'Name'])
    print("\nColumns afer dropping 'URL', 'disabilities_included', 'highlights':")
    print(df_prepared.columns)

    # Activity 7: Display any missing values in the dataframe
    print("\nRows with missing values:")
    # print(df_prepared.isna().any(axis=1))  # this version print all rows with True or False
    print(df_prepared[df_prepared.isna().any(axis=1)])
    print("\nColumns with missing values:")
    print(df_prepared.isnull().any(axis=0))  # this version prints all columns with True or False
    print(df_prepared.columns[df_prepared.isna().any()].tolist())  # prints only the columns names with missing values
    print("\nTotal number of missing values:")
    print(df_prepared.isnull().sum().sum())

    # Activity 8: Correct values in a categorical column ['type']
    print("\nUnique values in the 'type' column:")
    print(df_prepared['type'].value_counts())  # counts the number of each unique value
    print(df_prepared['type'].unique())  # prints the unique values
    # remove whitespace and convert all to lowercase
    df_prepared['type'] = df_prepared['type'].str.strip().str.lower()
    print("\nUnique values in the 'type' column after corrections made:")
    print(df_prepared['type'].unique())  # prints the unique values
    print(df_prepared['type'].value_counts())  # counts the number of each unique value

    # Activity 9: Insery a new column, duration, after the start and end columns
    insert_loc = df_prepared.columns.get_loc('end')
    duration_values = (df_prepared['end'] - df_prepared['start']).dt.days.astype(int)
    df_prepared.insert(insert_loc + 1, 'duration', duration_values)
    print("\nColumns after inserting the 'duration' column:")
    print(df_prepared.columns)

    # Activity 10: Save the prepared data to a csv file and excel file
    filepath_to_save = Path(__file__).parent.parent.joinpath("data", "paralympics_events_prepared.csv")
    df_prepared.to_csv(filepath_to_save, index=False)
    filepath_to_save_e = Path(__file__).parent.parent.joinpath("data", "paralympics_events_prepared.xlsx")
    df_prepared.to_excel(filepath_to_save_e, index=False)

    return df_prepared


if __name__ == "__main__":
    # Activity 2: Filepath of the csv data file
    paralympics_datafile_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_raw.csv")

    # Activity 2: Filepath of the Excel data file.
    paralympics_datafile_excel = Path(__file__).parent.parent.joinpath("data", "paralympics_all_raw.xlsx")

    # Activity 2: Filepath of the NPC codes csv data file
    npc_csv = Path(__file__).parent.parent.joinpath("data", "npc_codes.csv")

    # Activity 2: Read the data from the files into a Pandas dataframe. Version includes error handling for the file read
    try:
        paralympics_datafile_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_raw.csv")
        events_csv_df = pd.read_csv(paralympics_datafile_csv)
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

    events_excel_df = pd.read_excel(paralympics_datafile_excel)
    medal_standings_df = pd.read_excel(paralympics_datafile_excel, sheet_name="medal_standings")

    # Activity 3: Call the function to describe the dataframe
    describe_dataframe(events_csv_df)
    describe_dataframe(events_excel_df)
    describe_dataframe(medal_standings_df)

    # This version outputs to a text file in  the tutor_solutiom directory rather than printing to the console
    describe_output_file = Path(__file__).parent.joinpath("describe_output.txt")
    with open(describe_output_file, 'w') as f:
        # Redirect stdout to a file temporarily
        sys.stdout = f
        print('\nEVENTS .CSV DATAFRAME\n----------------------')
        describe_dataframe(events_csv_df)
        print('\nEVENTS .XLSX DATAFRAME\n----------------------')
        describe_dataframe(events_excel_df)
        print('\nMEDAL STANDINGS .XLSX DATAFRAME\n----------------------')
        describe_dataframe(medal_standings_df)
        f.close()
        # Redirect stdout back to the console
        sys.stdout = sys.__stdout__

    # Activity 4: Call the function to prepare the data for analysis to change the float data types to int in events_csv_df
    # prepare_event_data(events_csv_df)

    # Activity 4: Print the values in the start and end columns of the dataframe
    # print("\nValues in the 'start' column:")
    # print(events_csv_df.loc[:, ['start', 'end']])

    # Activity 4: Call the function to prepare the data for analysis to change the data types of the start and end columns
    # prepare_event_data(events_csv_df)

    # Activities 5-8: Call the function to prepare the data and merge the event data with the NPC data
    df_npc_codes = pd.read_csv(npc_csv, usecols=['Code', 'Name'], encoding='utf-8', encoding_errors='ignore')
    # merged_df = prepare_event_data(events_csv_df, df_npc_codes)

    # Activity 10: Final call to the function to return the prepared data to a dataframe and save to file
    prepared_df = prepare_event_data(events_csv_df, df_npc_codes)
    # print(prepared_df)

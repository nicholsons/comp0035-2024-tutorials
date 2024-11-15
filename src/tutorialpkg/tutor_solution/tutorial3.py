"""Module to explore the data using visualisation techniques.

    Please comment/uncomment sections of the code to run each activity.

"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def draw_sample_plot(df):
    """Draw a sample plot using pandas.plot."""

    # Using pandas.plot directly creates the figure, axes and allows for some customisation
    # matplotlib examples typically split this into separate commands,
    # defining fig and ax then adding customisation
    df.plot(title='Sample Plot', xlabel='X-axis Label', ylabel='Y-axis Label')

    # Show the plot
    plt.show()


def view_distribution(df, columns=None):
    """Draw a histogram of specified columns in the DataFrame to visualise the distribution of the
    data.

    Parameters:
        df : pd.DataFrame   The DataFrame to plot
        columns : list      The column names to plot

    Returns:
        None
    """

    if columns:
        df[columns].hist()
    else:
        df.hist()
    plt.show()


def view_outliers(df):
    """Draw boxplot of the DataFrame columns to visualise the distribution of the data.

    Useful for identifying outliers.

    Each column is plotted into a separate subplot.

    Parameters:
        df : pd.DataFrame   The DataFrame to plot

    Returns:
        None
    """

    df.boxplot(subplots=True, sharey=False)
    plt.tight_layout()
    # Save the plot to a file
    save_path = Path(__file__).parent.joinpath('boxplot_example.png')
    plt.savefig(save_path)
    plt.show()


def view_timeseries(df, date_column, value_column, filter_value=None):
    """Draw a timeseries plot of the DataFrame using the specified date and value columns.

    Sort the rows in date order before plotting.

    Parameters:
        df : pd.DataFrame   The DataFrame to plot
        date_column : str   The column name containing the date data
        value_column : str  The column name containing the value data
        filter_value: str   The value to filter the DataFrame by

    """

    # Sort the DataFrame by the date column
    df = df.sort_values(by=date_column)

    if filter_value:
        df = df[df['column_name'] == filter_value]

    # Group the DataFrame by the type column (winter/summer)
    # This still displays all the data though so there is a dip in the line
    # df.groupby("type").plot(x=date_column, y=value_column)
    # df.plot(x=date_column, y=value_column)

    # This version draws one line for each 'type'
    df_summer = df[df['type'] == 'summer']
    df_winter = df[df['type'] == 'winter']
    ax = df_summer.plot(x=date_column, y=value_column, label='Summer games')
    df_winter.plot(x=date_column, y=value_column, ax=ax, label='Winter games')
    plt.xticks(rotation=90)

    save_path = Path(__file__).parent.joinpath('plt-timeseries.png')
    plt.savefig(save_path)
    # plt.show()


if __name__ == '__main__':
    # Activity 1: Sample DataFrame
    df_simple = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [4, 3, 2, 1]})
    draw_sample_plot(df_simple)

    # Activities 2 - 4: Load the prepared data
    try:
        prepared_data_fp = Path(__file__).parent.parent.joinpath("data",
                                                                 "paralympics_events_prepared.csv")
        prepared_df = pd.read_csv(prepared_data_fp)

        # Activity 2: Draw histograms of the DataFrame using the prepared data
        # view_distribution(prepared_df)
        # participant_columns = ['participants_m', 'participants_f']
        # view_distribution(prepared_df, participant_columns)

        # Activity 3: Draw boxplots of the DataFrame using the prepared data
        # view_outliers(prepared_df)

        # Activity 4: Draw timeseries plot of the DataFrame using the prepared data
        view_timeseries(prepared_df, 'start', 'participants')

    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

    # Activity 6: Linting
    # Enter the following lineS, without the #, in the terminal to lint

    # pylint src/tutorialpkg/sample_code/code_to_lint.py
    # flake8 src/tutorialpkg/sample_code/code_to_lint.py

    # You can output pylint and flake8 results to a file which may be useful for the coursework e.g.
    # pylint src/tutorialpkg/tutor_solution/tutorial3.py --output=src/tutorialpkg/sample_code/pylintout.txt

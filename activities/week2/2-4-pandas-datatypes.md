from typing import List

# Changing datatypes

This activity moves on from describing the dataframe to changing its contents to suit our purposes, this is something
referred to as 'data preparation' or 'data cleaning'.

## Create a new function

We will want to repeat these steps for the event dataframe and the medal_standings dataframe so let's create a function
that can be reused.

The function should take a DataFrame of the raw data, perform actions to prepare it for our needs, and then return a
dataframe with the prepared data (and/or save the data to a .csv or .xlsx file).

Create the outline of the function in your data preparation module.

## Changing datatypes

In the last activity you saw that the event data the datatypes in the dataframe are:

```text
Data types of the columns:
type                      object
year                       int64
country                   object
host                      object
start                     object
end                       object
duration                   int64
disabilities_included     object
countries                float64
events                   float64
sports                     int64
participants_m           float64
participants_f           float64
participants             float64
highlights                object
URL                       object
```

The pandas reference states: "Columns with mixed types are stored with the object dtype". We will deal with the object
datatype columns later.

First, lets change all the 'float64' to 'int' as we want the values as '21' rather than '21.0'.

## Changing float64 and int54 to int

You can set a column's datatype when you read in the data by specifying a datatype for particular columns, e.g.

```python
import pandas as pd

# Define the data types for the columns
dtype_dict = {
    'column1': 'int64',
    'column2': 'float64',
    'column3': 'int64',
    # Add more columns as needed
}

# Read the CSV file with specified dtypes
df = pd.read_csv('your_file.csv', dtype=dtype_dict)
```

Or change the datatypes after creating the DataFrame:

```python
import pandas as pd

# Read the CSV file
df = pd.read_csv('your_file.csv')

# Convert a specific column from float64 to int
df['column_name'] = df['column_name'].astype('int')
```

1. Add code to your data preparation function to change all the float64 datatypes to int.
    ```python
    columns_to_change= ['countries', 'events', 'participants_m', 'participants_f', 'participants']
    ```
2. Add code to main to call your data preparation function passing one of the events DataFrames as the parameter.
3. Run the code

Did you get an error? e.g.
`IntCastingNaNError(pandas.errors.IntCastingNaNError: Cannot convert non-finite values (NA or inf) to integer`.

Pandas cannot convert nulls, or NAs, to int. There must be some

## Date fields

The 'start' and 'end' columns should be dates but are currently showing as object.

The pandas reference states: "Columns with mixed types are stored with the object dtype".

Explore the values in the start and end columns.

Unique values can be found using `DataFrame.unique()`, or occurrences using `DataFrame.value_counts` though in this case
the values will all be unique as they are in different years, so just printing the columns will do the same.

You can reference a column using:

- bracket notation: `name_of_dataframe['col_name']`
- dot notation: `name_of_datafrane.col_name` (works where there are no spaces or special characters in the column name)
- using [`loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) to identify a group of rows and
  columns using integer positions or column labels: `name_of_dataframe.loc[7:9]` (row with index 7 and column with index
    9) or `name_of_dataframe[:, 'col_a']` (all rows from the column named 'col_a') or
       `name_of_dataframe[:, ['col_a','col_b]]` (all rows from columns named 'col_a' and 'col_b')

An `iloc` method exists but is deprecated.

1. In the 'main', print the values from the 'start' and 'end' columns from one the events DataFrames using one of the
   methods above.

   Are there any missing values? There shouldn't be.

2. Add code to the data preparation function to change the date formats using the pandas function
   [`pd.to_datetime()`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html). To replace the column '
   start' with the modified
   datatypes you can use this syntax:

   `name_of_your_dataframe['start'] = pd.to_datetime(name_of_your_dataframe['start'], format='%d/%m/%Y')`

   See [Python datetime for the format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

[Go to next activity](2-5-pandas-joining-dataframes.md)
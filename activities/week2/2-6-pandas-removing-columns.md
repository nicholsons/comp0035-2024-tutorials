# Removing columns

In the function to describe the events dataframe you printed all the column names:

```text
['type', 'year', 'country', 'host', 'start', 'end', 'disabilities_included', 'countries', 'events', 
    'sports', 'participants_m', 'participants_f', 'participants', 'highlights', 'URL']
```

Assume that the 'URL', 'disabilities_included' and 'highlights' columns aren't going to be needed in the project for
creating charts, so remove them.

One approach to avoid unnecessary columns it to read only the columns you need when you create the DataFrame using the
`usecols` parameter. For example:

```python
import pandas as pd
from pathlib import Path

if __name__ == '__main__':
    cols = ['type', 'year', 'country', 'host', 'start', 'end', 'countries', 'events', 'sports',
            'participants_m', 'participants_f', 'participants']
    raw_data_csv = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    df_selected_cols = pd.read_csv(raw_data_csv, usecols=cols)
    print(df_selected_cols)
```

As you already have the columns then instead you will delete them.

Use the [pandas.DataFrame.drop()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html) to remove
either rows or columns.

Most methods in pandas return a new object and leave the original untouched.

To alter the DataFrame in-place you can sometimes use the attribute `inplace=True`; though most examples will instead
allocate the result of an action to a new dataframe object (`inplace=True` can have unwanted implications in certain
circumstances).

An example allocating the result to a new dataframe:

```python
df_result = df.drop(columns=['MyCol2', 'MyCol4'], axis=1)
```

An example using `inplace=True`:
```python
df.drop('B', axis=1, inplace=True)
```

Also note the axis number. Rows in a DataFrame are `axis=0` and columns are `axis=1`.

1. Edit the data preparation function to drop the following list of named columns
   `['URL', 'disabilities_included', 'highlights']` and assign the result to a new variable (DataFrame) called
   `df_prepared`.
2. You might also want to add a print of the column names again so you can check the columns were removed. Run the code.

[Next activity](2-7-pandas-missing-values.md)
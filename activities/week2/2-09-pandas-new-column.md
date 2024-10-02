# Activity 2.9: Adding new columns

You can add new columns to the data, for example by computing new values.

In this activity, add a new column called duration which can be calculated by subtracting the start date from the end
date: `df[duration] = df['end'] - df['start']`.

1. Edit the code to create the new field.
2. If you run the code now, the new field will be appended to the end of the columns. Instead, insert it after the 'end'
   column e.g. `df.insert(df.columns.get_loc('end'), 'duration', df['end'] - df['start']).dt.days.astype(int)`

   The code will place the duration column right before the end column:
    - `df.columns.get_loc('end')`: Finds the index of the 'end' column. You then need to add 1 to this to place the
      column after the 'end'.
    - `'duration'`: The name of the new column.
    - `df['end'] - df['start']`: The values for the new column.
    - `.dt.days.astype(int)`: The result would be in days e.g. '4 days', this converts the days to an integer e.g. '4'
3. Now run the code.
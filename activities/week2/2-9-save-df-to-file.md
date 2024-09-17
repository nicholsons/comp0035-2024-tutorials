# Save the prepared dataset

You have now carried out the data cleaning and preparation steps needed for this project so save the prepared
dataframe back to a .csv file.

You could also save the data to a database or other format.
See [pandas output methods](https://pandas.pydata.org/docs/reference/io.html#).

1. Add code add the end of the data preparation function to save the output to file in the 'data' directory before you
   return the dataframe. You could remove the return dataframe from the end of the function if you prefer. Use the
   pandas ['to_csv()'](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html).

   Note that the dataframe has an index column with row numbers that you don't need in the csv file. Use the
   argument `index=False` when you use `to.csv()`

2. Run the code and check that the file is saved to 'src/tutorialpkg/data/paralympics_events_prepared.csv'

[Further practice](2-10-further-practice.md)
# Distributions of values

It can be useful to understand the range of values, and the distribution of those values, for the numerical columns in
your data.

This activity uses pandas to
generate [histograms](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hist.html#pandas.DataFrame.plot.hist).

Histograms are 'designed to show a dataset's distribution or
spread' [Reference: Depict, Chart chooser](https://depictdatastudio.com/charts/histograms/).

Create [histograms](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hist.html#pandas.DataFrame.plot.hist)
to show the distribution of the 'participants_m' and 'participants_f' columns.

The histogram function has the following options `DataFrame.plot.hist(by=None, bins=10, **kwargs)[source]`. The `kwargs`
are the parameters show in
the [.plot() reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot).

1. Create a new Python module for the code to create charts for the data exploration (create it in the data preparation
   package if you have one).
2. Add code for the structure of a new function that will display a figure with distributions of the data. This function
   will take a dataframe as its parameter and return one or more pandas plots.
3. Add imports: `import pandas as pd`, `import matplotlib.pyplot as plt` and `from pathlib import Path`.
4. In main, create a dataframe from the contents of the prepared data .csv file you created last week.
5. Add code to the function to create a histogram from the data:

      ```python
       # Create a histogram of the DataFrame
       df.hist()

       # Show the plot
       plt.show()
    ```
6. Run the code to generate the figure. It should generate a figure that has histograms for all the columns in the
   data.
7. Modify the function to take just specified columns. You can add a second parameter, `columns`, and the modify line to
   generate the histogram, e.gf. `df[columns].hist()`
8. Run the code again to generate the figure.
9. The distributions don't really tell you much in this dataset. It may be more useful for larger datasets. Challenge:
   create histograms for the winter and summer events.

    ```python
    # Filter the DataFrame to select only rows where 'type' is 'summer'
    # syntax: df = df[df['column_name'] == filter_value]
    summer_df = df[df['type'] == 'summer']
    ```

[Next activity](3-3-outliers.md)
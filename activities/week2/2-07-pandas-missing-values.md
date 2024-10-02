# Activity 2.7: Dealing with missing values

Missing values or missing data are those values that are not present in the data set.

There are many reasons for values to be missing, for example because they don't exist, or because of improper data
collection or improper data entry.

Missing values in data can reduce the accuracy of any resulting data analysis or machine learning model.

In pandas, missing values are represented by None or NaN (**N**ot **a** **N**umber). Note that empty strings (`''`) are
not considered NA values.

In data science, missing values are typically categorised as:

- Missing Completely At Random (MCAR). There is no relationship between the missing data and any other vales in the
  dataset. There is no pattern for the missing values. The advantage of such data is that the statistical analysis
  remains unbiased.
- Missing At Random (MAR). The missing values are related to variables that are complete, i.e. there is a relationshp
  between the missing data and other values. The missing data may be estimated using the related values.
- Missing Not At Random (MNAR). There appears to be a pattern to the missing data; however this pattern does not depend
  on other variables that are in the dataset but some unknown variable. This can bias the results of any analysis.

[This article](https://www.analyticsvidhya.com/blog/2021/10/handling-missing-value/) summarises these succinctly.

There are different ways to deal with missing values:

- Do nothing. It may be valid, e.g. the data does not yet exist so its absence is meaningful. It may not have
  significant impact on your analysis to ignore the missing values.
- If your data set is large enough you might choose to delete missing data without significant impact to the resulting
  analysis. Likewise, if the percentage of missing values is high, you may prefer to delete those rows
  or columns.
- Use an imputation technique to fill the missing values e.g. mean, median, most frequent etc. Imputation techniques are
  not covered in this course. If you want to understand more about imputation,
  this [article on Towards Data Science](https://towardsdatascience.com/6-different-ways-to-compensate-for-missing-values-data-imputation-with-examples-6022d9ca0779)
  gives pros and cons of some common imputation techniques.

The decision you make will depend on the type of data, the actions you want to perform on the data, and the reasons for
the missing values.

## Finding the missing values

You will need to refer to the pandas documentation in this activity:

- [dropna()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)
- [fillna()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html)
- [isnull()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html)
- [isna()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html)

You have already found some issues with NaNs in the dataframe:

- When you tried to convert the columns of datatype float to int.
- When you merged the two dataframes

However, there may be more.

1. Print the number of missing values in the merged DataFrame using `isna()` or `isnull()`. 'True' indicates a
   missing value. Run the code to see the results. You can then remove or comment out the code.
2. Step 1 shows all the data which may not be practical in a large dataset. In the data preparation function, create and
   print a dataframe with
   only the rows that contain any missing values. Example of the syntax to create a DataFrame with missing
   rows: `missing_rows = df[df.isna().any(axis=1)]` or columns: `missing_columns = df[df.isna().any(axis=0)]`.

## Addressing the missing values

There are missing values in the following columns:
`['countries', 'events', 'participants_m', 'participants_f', 'participants', 'highlights', 'Code', 'Name']`

```text
      type  year country                       host      start        end  duration  countries  events  sports  participants_m  participants_f  participants Code
0   Summer  1960   Italy                       Rome 1960-09-18 1960-09-25         7       23.0   113.0       8             NaN             NaN         209.0  ITA
6   summer  1984      UK  Stoke Mandeville New York 1984-06-17 1984-08-01        45       58.0   975.0      18          1569.0           536.0        2105.0  NaN
7   summer  1988   Korea                      Seoul 1988-10-16 1988-10-25         9       60.0   733.0      18          2370.0           671.0        3041.0  NaN
9   summer  1996     USA                    Atlanta 1996-08-16 1996-08-25         9      104.0   519.0      19          2462.0           790.0        3252.0  NaN
12  summer  2008   China                    Beijing 2008-09-06 2008-09-17        11      146.0   472.0      20          2585.0          1366.0        3951.0  NaN
13  summer  2012      UK                     London 2012-08-29 2012-09-09        11      164.0   530.0      20          2741.0          1502.0        4243.0  NaN
17  summer  2028     USA                Los Angeles 2028-08-15 2028-08-27        12        NaN     NaN      22             NaN             NaN           NaN  NaN
25  winter  2002     USA             Salt Lake City 2002-03-09 2002-03-18         9       36.0    92.0       4           328.0            87.0         415.0  NaN
28  winter  2014  Russia                      Sochi 2014-03-07 2014-03-16         9       45.0    72.0       6           411.0           129.0         540.0  NaN
29  winter  2018   Korea                PyeongChang 2018-03-09 2018-03-18         9       49.0    80.0       6           430.0           133.0         563.0  NaN
30  winter  2022   China                    Beijing 2022-03-04 2022-03-13         9       46.0    78.0       6           422.0           136.0         558.0  NaN
31  winter  2026   Italy             Milano Cortina 2026-03-06 2026-03-15         9        NaN    79.0       6             NaN             NaN           NaN  ITA
```

Let's deal with some of these.

In the data preparation function write code to address the missing values.

1. The name 'Name' column is not needed as we have country name in the 'country' field which does not have any missing
   values. Use the knowledge gained in the last activity to drop this column from the dataframe.
2. The participants_m and participants_f data for Rome in 1960 is not available. We could try to impute the data using
   the next event % as a guide, or remove it from the dataset. Remove row with index 0. Add the code to do this _before_
   the code to convert float to int for this column. To remove a row: `your_df_name = your_df_name.drop(index=0)`
3. Numerous fields are missing from 17 and 31 as these are future events so the values are not known. Again, remove
   these rows before the code to convert to float.
4. When you remove rows, the index is not reset so will now be mussing 0, 17 and 31. Add code to reset the index using [DataFrame.reset_index](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html#pandas.DataFrame.reset_index) e.g. `df = df.reset_index(drop=True)`
5. The only values that are still NaN are the country codes for UK, USA, Korea, Russia and China. In the NPC file these
   are:

    ```python
    replacement_names = {
        'UK': 'Great Britain',
        'USA': 'United States of America',
        'Korea': 'Republic of Korea',
        'Russia': 'Russian Federation',
        'China': "People's Republic of China"
    }
    ```

   Add code _before_ the code to merge the two dataframes. The code should change the values in the `['country']` column
   to those in the dict given above.

   Use
   the [Series.replace(to_replace=replacement_names) function](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html#pandas.Series.replace).
6. Run the data preparation code again and now there should not be any result from the functions to print the missing data.

[Next activity](2-08-pandas-categorical-data)
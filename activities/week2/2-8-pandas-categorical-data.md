# Working with categorical data

Categorical variables are those where the data can be divided into categories, or groups. For example: race, gender, age
group, and educational level.

Categorical variables can be problematic for data analysis.

One issue is that many machine learning algorithms cannot handle categorical data. To overcome this, categorical values
can be replaced with encoded data. For example: Hot = 1, Warm = 2, Cold = 3. Techniques for addressing this is not
covered in this course, however there are Python packages (or functions within packages) that will handle this process
of encoding; a popular option
is [OneHotEncoder](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwijhozWxe2BAxWaUkEAHegCDEYQFnoECB4QAQ&url=http%3A%2F%2Fscikit-learn.org%2Fstable%2Fmodules%2Fgenerated%2Fsklearn.preprocessing.OneHotEncoder.html&usg=AOvVaw0oQAupueEbfcv4c2Csd5dn&opi=89978449).

A second issue is that depending on how the data was collected, categorical data may be entered inconsistently, e.g. in
an address where the values "UK", "Great Britain", and "United Kingdon" all relate to the same country.
However, as they are spelt differently any functions to count, group etc. would not recognise the similarity.

This issue occurs in the paralympics event data in the `type` column.

1. In `main`, print unique values for the 'Type' column. A single column is a Series so you can
   use [`df['ColName'].unique()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html) or [
   `df['ColName'].value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html).
2. In your data preparation function, remove the whitespace from the 'winter ' occurrence by stripping whitespace either
   just from that cell, or from all values in the type column.
   Use ['.str.strip()' function](https://pandas.pydata.org/pandas-docs/version/0.24/reference/api/pandas.Series.str.strip.html)
   .
3. In your data preparation function, change all the values in 'type' to all lower case.
   Use ['.str.lower()' function](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lower.html#pandas.Series.str.lower)
   .

[Next activity](2-9-save-df-to-file.md)
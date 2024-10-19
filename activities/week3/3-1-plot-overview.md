# 1. Introduction

In this tutorial and the next you will use pandas to explore a dataset by visualising the data.

This aim is not to create polished visualisation (often a chart) for a target audience. The aim is to get a better
understanding of the data to decide if what you have is largely free from data quality issues and that it suits the
needs of your project.

During this exploration you may find further problems with the data that need to be addressed ('cleaned'); and consider
whether the data is sufficient for your project.

You will write code in a way that is potentially reusable in an application, with considerations such as:

- creating a relevant Python module
- using relative filepaths to access data files
- creating Python functions, rather than a simple sequence of commands (procedural)
- checking your code meets with Python PEP8 style conventions. Using the `flake8` Python package to check your code.

Writing code in this way may seem unnecessary at this stage, however you will be expected to do this for the coursework
so it is a good practice to start out working that way.

## Pandas plot

Pandas comes with a
builtin plotting method, [.plot()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html) that can be
applied to a DataFrame to generate visualisations. These visualisations are also referred to as "charts", "graphs" or "
plots".

By default, pandas `.plot()` uses `matplotlib` as the engine that renders (draws) the
plot. [Matplotlib](https://matplotlib.org) is a Python visualisation library that has more functions than are used by
pandas, we won't be learning matplotlib directly in this tutorial, only the `pandas.plot()` interface.

As pandas is built on matplotlib then you will see common terminology used.

- Data (dataframe): The data to be used in the plot.
- Figure: The overall window that the visualisation is drawn on. This can contain multiple plots or 'axes'.
- Axes: The individual plots within a Figure. Each can have its own labels, titles, ticks, etc. Where there are several
  plots in one figure, these plot are created as 'subplots'.

The typical steps to create a pandas plot are:

- Define the data to be plotted in a dataframe
- Create a figure and axes
- Plot the data on the axes
- Optionally, customise the plot e.g. styling, titles, ticks, labels etc.
- Show the plot

This is a sample to illustrate:

```Python
import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [4, 3, 2, 1]
})

# Using pandas.plot directly creates the figure, axes and allows for some customisation
# matplotlib examples typically split this into separate commands defining fig and ax then adding customisation
ax = df.plot(title='Sample Plot', xlabel='X-axis Label', ylabel='Y-axis Label')

# Show the plot
plt.show()
```

You can run this example in [example_plot.py](../../src/tutorialpkg/sample_code/example_plot.py) in your own IDE.

In VS Code the chart usually displays in a separate pop-out window. You need to close this window before running the
code again.

In PyCharm it displays in the Plots pane within the interface.

Note that once the chart is displayed, the code stops executing so you may need to close the chart window before running
further code.

[Next activity](3-2-distribution)
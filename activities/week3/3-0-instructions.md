# COMP0035 Tutorial 3: Data exploration using Python pandas

## Pre-requisites

You should have completed week 2 activities and have an understanding of Python pandas DataFrame structure and
functions.

The activities assume that you have forked the COMP0035 tutorials repository, cloned it to your computer, and set up a
project with a virtual environment within your IDE (VS Code or PyCharm).

### 1. Update the forked tutorials repository

Login to GitHub and navigate to your forked copy of the COMP0035 tutorials repository.

Check whether any changes have been made. For example, the image below shows 1 new commit has been made to the original.
![Sync the forked repository](../img/gh-synch-fork.png)

If changes have been made, you will need to update your forked repository.

Click on the "Synch fork" button; and then on "Update branch".
![Update branch](../img/gh-update-branch.png)

Now, open your IDE (VS Code, PyCharm) and update the local copy of the repository. This assumes you have integrated your
IDE with your GitHub account in week 1. You may be prompted to log in to GitHub before you can carry out the
following.

- In PyCharm try menu option Git > Pull
- In VS Code click on the source code control icon on the left side panel, then when the source code control pane opens,
  click on the three dots and select Pull.

There are other methods, look in the Help for either PyCharm or VSCode.

### 2. Check you have the virtual environment activated

Open a terminal window within your IDE in the project directory.

Check that your virtual environment is activated. There are various ways to do this, IDEs vary, usually a quick visual
way is to check whether the prompt starts with `(.venv)` or the name if your venv folder if not `.venv`. You can also
use Python in the Terminal:

```python
import os

print(os.environ.get('VIRTUAL_ENV'))
```

The following screenshot shows this in PyCharm on macOS:

![Check for active venv](../img/venv-check.png)

If you are not in a venv, refer to [Week 1 activity 7](../week1/1-7-create-virtual-environment.md) for instructions.

### 3. Check you have the required libraries installed in the virtual environment

Open the Terminal in your IDE.

At the prompt, enter: `pip list`

This should print a list of installed Python packages and their versions. Check for `pandas` and `matplotlib`.

The default installation of pandas can only open Excel `.xlsx` files with an additional library called `openpyxl`. Check
if this is installed.

You can install all three using `pip` e.g.  `pip install pandas openpyxl matplotlib` or individually e.g.
`pip install pandas`

## Complete the activities

Tutorial activities can be found in the activities/week3 folder. These are:

1. [Introduction to pandas plotting](3-1-plot-overview)
2. [Plotting distributions using histograms](3-2-distribution)
3. [Identifying outliers using boxplots](3-3-outliers.md)
4. [Plotting timeseries](3-4-timeseries.md)
5. [Check your code complies with Python style guides](3-6-lint)

## Apply the knowledge to your coursework project

As a third year module, the coursework is not meant to be a series of instructions to follow. However, to get you
started this week here are some suggestions of what to do:

- Write code to explore the data. This may lead to you changing the data preparation code you previously wrote.
- Check your code meets with Python PEP8 style conventions.

Do some extra research. There are many tutorials publicly available that focus on data preparation and exploration with
pandas. Try to find examples that do more that has been covered in this tutorial to expand your knowledge.

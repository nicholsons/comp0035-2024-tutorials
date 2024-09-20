# COMP0035 Tutorial 4: Database design

## Pre-requisites

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

## Complete the activities

Use the version of the data files in the `database` directory for these activities. A change has been made to the '
summer 1984' row in the data for this activity.

Tutorial activities can be found in the activities/week4 folder. These are:

1. [Introduction to database design and ERD (lecture recap)](4-1-database-design.md)
2. [Design and draw an Entity Relationship Diagram (ERD) for a database normalised to 3rd normal form (3NF)](4-2-ERD.md)
3. [Design and draw an Entity Relationship Diagram (ERD) for a database normalised to 3rd normal form (3NF) - part 2](4-3-ERD-part2.md)
4. [Data constraints and UPDATE/DELETE actions](4-4-constraints.md)
5. [Further practice/information](4-5-further-practice.md)

## Apply the knowledge to your coursework project

As a third year module, the coursework is not meant to be a series of instructions to follow. However, to get you
started this week here are some suggestions of what to do:

- Draw an ERD for your data set. Start with a single table then look for any issues that break the rules for
  normalisation up to the third normal form.
-

Do some extra research. There are many tutorials publicly available that focus on data preparation and exploration with
pandas. Try to find examples that do more that has been covered in this tutorial to expand your knowledge.

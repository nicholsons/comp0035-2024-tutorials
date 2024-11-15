# COMP0035 Tutorial 9: Testing (unit testing and continuous integration in GitHub)

## Pre-requisite: Configure your IDE to support pytest

Configure your project in your IDE to use a test runner for the library you are using, i.e. pytest. You will need
to read the documentation for your IDE:

    - [Pycharm help: Testing frameworks](https://www.jetbrains.com/help/pycharm/testing-frameworks.html)
    - [Python testing in VS Code](https://code.visualstudio.com/docs/python/testing)

## Pre-requisite: update the forked tutorial repository

The activities assume that you forked the COMP0035 tutorials repository, cloned it to your computer, and set up a
project with a virtual environment within your IDE (VS Code or PyCharm).

Login to GitHub and navigate to your forked copy of the COMP0035 tutorials repository.

Check whether any changes have been made. For example, the image below shows 1 new commit has been made to the original.
![Sync the forked repository](../img/gh-synch-fork.png)

If changes have been made, you will need to update your forked repository.

Click on the "Synch fork" button; and then on "Update branch".
![Update branch](../img/gh-update-branch.png)

Now, open your IDE (VS Code, PyCharm) and update the local copy of the repository. This assumes you have integrated your
IDE with your GitHub account in week 1. You may be prompted to log in to GitHub before you can carry out the
following.

- In PyCharm try menu option Git > Pull  (or Git > Synch)
- In VS Code click on the source code control icon on the left side panel, then when the source code control pane opens,
  click on the three dots and select Pull (or Synch).

There are other methods, look in the Help for either PyCharm or VSCode.

## Complete the activities

Tutorial activities can be found in the activities/week9 folder. These are:

1. [Introduction to unit testing and conventions](9-1-introduction.md)
2. [Unit testing with pytest](9-2-unit-testing.md)
3. [Pytest fixtures](9-3-fixtures.md)
4. [Running tests with GitHub Actions](9-4-ci-github.md)
5. [Reporting test coverage](9-5-coverage.md)
6. [Use of gen AI tools in unit testing](9-6-ai-testing.md)
7. [Further information](9-7-further.md)

## Apply the knowledge to your coursework project

- Read the testing section of the specification
- Write the test code

This is the last tutorial related to the coursework. The last tutorial has no new activities and is for you to work on
the coursework.
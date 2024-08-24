# COMP0035 Tutorial 1: Intro to using Git and GitHub; and setting up a project in your IDE

## Pre-requisites

You must have completed the following before attending the tutorial.

There will not be sufficient time to do this in the session.

1. Check that you have installed:
    - Python
    - Git
    - a Python IDE. Visual Studio Code or PyCharm Professional
      version ([free license with a student account](https://www.jetbrains.com/lp/leaflets-gdc/students/)) are
      suggested.
2. You should have created a GitHub
   account. [Sign up for free student account to get GitHub Pro](https://github.com/education/students).

## Introduction

This session introduces you to using Git, GitHub and GitHub Classroom. It then walks through setting up a project in an
IDE. The learning objective is that you should have sufficient knowledge to create a project in your IDE for your
coursework.

This class will not be sufficient to teach you the full use of Git, GitHub and their integration with your chosen code
editor or IDE. There are also video tutorials and guides in the Reading List. The best way to learn is to
keep using Git and GitHub throughout the COMP0035 and COMP0034 projects.

You can work with GitHub using a git command line from a terminal; directly on GitHub.com or using any number of source
code control software. In COMP0034 and COMP0035 it is assumed you will mostly work with GitHub using your IDE (VS Code,
PyCharm etc.) so this tutorial focuses on this method.

There are different ways to create a GitHub repository including:

1. Create a new empty repository directly on GitHub.com
2. Push existing code from a project on your computer to GitHub
3. Accept an assignment from GitHub classroom
4. Fork an existing GitHub repository

The two approaches you are most likely to use in the course are:

**Accept an assignment from GitHub Classroom** - used for the Coursework

1. Create your own copy of a repository by accepting a GitHub Classroom assignment. This creates a remote copy of the
   repository in the ucl-comp0035 organisation.
2. Clone this remote copy from GitHub to your IDE to create a project with a local repository
3. Create a virtual environment for the project (local repository) in your IDE
4. Edit code in the IDE and push changes from your local repository to the remote repository on GitHub

**Fork an existing GitHub repository** - used for the Tutorials (Coding practicals)

1. Fork the course repository for the tutorials. This creates a remote copy of the repository in your GitHub account.
2. Clone the repository to your IDE to create a project
3. Create a virtual environment for the project in your IDE
4. Edit code in the IDE and push changes to the remote repository

The tutorial will cover these steps in more detail.

## Complete the tutorial activities

**Note: The screenshots in the following activities provide a guide but may not exactly match your computer screen**. They
show
various repositories (not necessarily those in the instructions); and the interfaces to GitHub, PyCharm and VSCode vary
in different versions and on different operating systems.

Complete the activities in the separate documents linked below. Then return to this overview document to continue.

1. [Create a repository directly on GitHub (10 mins)](1-1-create-repository-github.md)
2. [Create a repository using GitHub Classroom (10 mins)](1-2-create-repository-github-classroom.md)
3. [Create a repository by forking a GitHub repository (5 mins)](1-1-create-repository-github.md)
4. [Find a repository (5 mins)](1-4-find-repository.md)
5. [Integrate your IDE with your GitHub account (10 mins)](1-5-integrate-IDE-github.md)
6. [Clone a repository to create a project in your IDE (5 mins)](1-6-clone-repository.md)
7. [Create a virtual Python environment for a project in your IDE (10 mins)](1-7-create-virtual-environment.md)
8. [Synchronise changes between the local and remote repository (5 mins)](1-8-synch-changes.md)


## Apply the knowledge to create and set up your coursework project

1. Accept the GitHub Classroom assignment for the coursework.
2. Clone the repository to your IDE.
3. Create and activate a virtual environment.
4. Install the libraries in the requirements.txt file.
5. Install the project in editable mode using the pyproject.toml file.
6. Add a .gitignore file.
7. Edit the README.md file.
8. Make a change to a file in the project and commit and push the change to the remote repository.
9. Find your dataset (see Moodle) and add it to your IDE project. See note below on data set files > 50MB.

Note that if your dataset is more than 50MB you will not be able to synch it to GitHub unless you
use [large file storage](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage)
and download and install
the [Git LFS package](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage).
If you find this too challenging, try excluding the large file from tracking in git by adding the filename and directory
to your .gitignore file.

## Going further

Once you have mastered the basic 'edit > add > commit > pull > push' workflow, there are other features of GitHub you
should explore.

- Merge conflicts
- Branches
- Pull requests

### Merge conflicts

Merge conflicts can, and will, arise when two people edit the same line of code. This is called a merge conflict. To
resolve it you will need to decide which version of the line, or lines, of code to keep.

The guidance for how to do this is specific to each IDE:

- [VS Code merge conflicts](https://code.visualstudio.com/docs/sourcecontrol/overview#_merge-conflicts)
- [PyCharm resolve conflicts](https://www.jetbrains.com/help/pycharm/resolving-conflicts.html#non-distributed-version-control-systems)

### Branches

You do not have to work with branches in this course.

The idea is that you only ever have production ready code in the 'main' branch and that to make a change you first
create a branch and then work with that branch. This way your 'main' branch always has working code than can be
deployed; while in the branches you can develop changes or add new features which may not always be working.

To make changes such as adding a new feature, you would first create a new branch and then later once the changes are
complete, merge that branch back to the main branch.

You can create the branches in your IDE or directly on GitHub.

Once you have created a branch then you need to make sure you switch to working on that branch until such time as you
decide to merge the branch back into the main.

- [GitHub branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository)
- [VS Code branches](https://code.visualstudio.com/docs/editor/versioncontrol#_branches-and-tags).
- [PyCharm Manage Git branches](https://www.jetbrains.com/help/pycharm/manage-branches.html)

### Pull requests

[Pull requests](https://docs.github.com/en/pull-requests) let you tell others about changes you've pushed to a branch in
a repository on GitHub. Once a pull request is opened, you can discuss and review the potential changes with
collaborators and add follow-up commits before your changes are merged into the base branch.

- [VS Code Pull Requests and Issues](https://code.visualstudio.com/docs/editor/github#_getting-started-with-github-pull-requests-and-issues)
  .
- [PyCharm work with GitHub pull requests](https://www.jetbrains.com/help/pycharm/work-with-github-pull-requests.html)

## Sources of information

- [Python Packaging](https://packaging.python.org/tutorials/packaging-projects/).
- [Cloning a repository - VS Code](https://code.visualstudio.com/docs/sourcecontrol/github#_cloning-a-repository)
- [Check out a project (clone) - PyCharm](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub)
- [GitHub README.md](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [GitHub documentation](https://docs.github.com/en)
- [Freecodecamp Git and GitHub playlist - not specific to VS Code](https://www.youtube.com/playlist?list=PLWKjhJtqVAbkFiqHnNaxpOPhh9tSWMXIF)
- [GitHub and VS Code playlist](https://www.youtube.com/playlist?list=PLpPVLI0A0OkLBWbcctmGxxF6VHWSQw1hi)
- [Video showing how to create a new project on GitHub from an existing code project in VS Code](https://www.youtube.com/watch?v=3Tn58KQvWtU)
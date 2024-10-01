## Computer setup for COMP0035

You need a python coding environment with the following. Install/set-up in the order they are shown below.

#### 1. Install Python

Check if you already have this installed on your computer.

Open Terminal (Mac) or Powershell (Windows), and at the command prompt type and enter:

```
python3 --version
```

If Python 3 is installed you should see a version number returned e.g. Python 3.10.5

If you don't already have python 3.7 or later than please download and install the relevant version
of [python](https://www.python.org/downloads/) for your operating system.

#### 2. Install Git

Git is the underlying source code control software that GitHub uses.

You need to have Git in order to work with code that is both on your computer and in GitHub.

[Download the relevant version of Git](https://git-scm.com/downloads) for your operating system and install it on your
computer.

You can work with GitHub directly from a Git command prompt. However, unless you feel comfortable using command line
environments then this method isn't generally recommended for those just starting to learn Git and GitHub.

PyCharm and VS Code have tools that integrate with GitHub. If you are using a python editor/IDE that doesn't have Git
support you may need to install a local Git desktop application. There are many Git clients that are freely available,
for convenience you might want to use GitHub Desktop software.

#### 3. Create a GitHub account

If you do not already have a GitHub account then please create a [GitHub account](https://github.com/join) and
optionally [signup for a student developer pack](https://education.github.com/pack).

Avoid usernames that would allow you to be easily identified if possible.

If you have an existing account you can use that for the course. To gain access to the
student developer pack, you can also associate your UCL email with your account. The student developer pack which gives
you access to additional resources, such as Copilot AI integration with VS Code.

[Guidance for how to add a second email
address](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/adding-an-email-address-to-your-github-account#)

If you cannot use GitHub for a specific reason please contact the course tutor to try and find an alternative.

#### 4. Install an interactive development environment (IDE) for Python

You need a coding environment to develop Python and in COMP0034 you will also need to edit SQL, HTML, CSS and possibly
JavaScript.

The most powerful way to edit code is to use an integrated development environment (IDE). IDEs have features that go
beyond simple code writing to make a developer's life easier. However, they can take some time to learn how to use, and
if you are installing on your own computer they can require a significant amount of disk space.

If you already have a preferred IDE or editor that supports Python, Flask (python, Jinja2), SQL, HTML, CSS and
JavaScript then feel free to continue using it.

If you do not have a suitable IDE then install one suitable for Python. Free options include:

- [Visual Studio Code](https://code.visualstudio.com/download).
- PyCharm Professional (NOT the community version). You will need
  to [apply for a free student license](https://www.jetbrains.com/community/education/#students) to be able to use the
  Professional version.
- [Atom](https://atom.io)

The teaching materials are based on VS Code, though notes are usually included where there are differences for PyCharm.
I use PyCharm, most students use VS Code.

Jupyter is not recommended for these modules. While jupyter is widely used in data science, and is useful for preparing
and visualising datasets, it isn't as well suited to developing apps as an IDE. You are not permitted to submit .ipynb
files for the coursework.

You may be able to use a basic text or code editor, however it is likely to be far more challenging to learn how to use
Git, create and run unit tests, check code compliance, and other things that we will be looking at in this course.

Most students set-up an environment on a computer to which they have regular access. If you are not able to install or
configure software on a computer you have access to then you could try
PythonAnywhere [free beginner account](https://www.pythonanywhere.com/pricing/).

UCL computers are not ideal for this course as you are unlikely to be able to install the necessary packages.

##### Extensions to install for VS Code

For VS Code you may also need to install extensions:

- [Python for VS Code](https://code.visualstudio.com/docs/languages/python)
- [GitHub Co Pilot for VS Code](https://code.visualstudio.com/docs/languages/python#_enhance-completions-with-ai)
- [SQLite support](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) There are other options
  if you search for SQLite in the marketplace.
- [flake8](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8). Optional. Linting support for flake8.
- [Mermaid chart](https://marketplace.visualstudio.com/items?itemName=MermaidChart.vscode-mermaid-chart) Optional. Draw
  diagrams in markdown.
- [gitignore](https://marketplace.visualstudio.com/items?itemName=codezombiech.gitignore) Optional. Create .gitignore
  files using templates.

##### Plugins to install for PyCharm Professional

For PyCharm Professional you may also need to install plugins:

- [ignore for .gitignore files](https://plugins.jetbrains.com/plugin/7495--ignore)
- [GitHub Co Pilot for PyCharm](https://plugins.jetbrains.com/plugin/17718-github-copilot)
- [Mermaid](https://plugins.jetbrains.com/plugin/20146-mermaid) to view and edit ERD and UML diagrams in markdown.

SQLite database tools are included in the PyCharm Professional version.
# Python applications: repository structure

**5 mins to read, 5 mins to code**

This minor focuses on developing data-driven software applications using Python.

Writing code for applications differs to simply writing code that functions. COMP0035 focuses on the supporting
practices.

In this tutorial, you are asked to write code considering how the code could be re-used as part of an application. This
implies also that other developers may use your code so your code needs to run for anyone, not just yourself.

Some of the considerations introduced in this tutorial are:

- Using modules, packages and functions to structure your application code
- How to import modules, packages and functions in your code
- Accessing data files in a way that is not specific only to your computer

## Understanding the tutorial project structure

Last week you created a virtual python environment and installed an editable version of your own code in it using
`pip install -e .`. Refer to [week 1 activity 7](../week1/1-7-create-virtual-environment.md).

This tells your IDE about the structure of your COMP0035 tutorials project.

In this case it tells it:

- You have a directory called 'src' which contains packages. Packages by default are auto discovered in the root of a
  project, not in a non-package subdirectory.
- You have a package called 'tutorialpkg'
- You have data files associated with the 'tutorialpkg' package in a directory named 'data' in the 'tutorialpkg'

This definition is derived from the [contents of `pyproject.toml`](../../pyproject.toml).

## Modules, packages, data files and functions

A Python [module](https://docs.python.org/3/tutorial/modules.html) is "a file containing Python definitions and
statements. The file name is the module name with the suffix .py appended."

A Python [package](https://docs.python.org/3/tutorial/modules.html#packages) is "a way of structuring Python’s module
namespace by using 'dotted module names'. For example, the module name A.B designates a submodule named B in a package
named A."

Note that there is a more advanced concept, 'namespace packages', in Python that is not covered in this minor. If you go
on to develop Python applications beyond this course then you may wish to explore that topic.

A Python [function](https://docs.python.org/3/glossary.html#term-function) is "A series of statements which returns some
value to a caller. It can also be passed zero or more arguments which may be used in the execution of the body."

You may also have directories (or folders) and files that are not code files, e.g. data files such as `.csv`, `.xlsx`;
or database files such as `.sqlite` or `.db` files.

Have a look in [src/tutorialpkg](../../src/tutorialpkg) at examples of each of these:

- 'week2', 'week2/mypkg1' and 'week2/mypkg2' are all examples of packages. Note the special file `__init__.py` inside
  each of these.
- 'data' is an example of a directory (or folder)
- 'data/paralympics_raw.csv' is an example of a data file
- in 'week2/mypkg2/mymodule2_1.py, 'calculate_area_of_circle(radius)' is an example of a function

## Typical Python application structures

There is no single pattern for structuring a Python application. However, there are common patterns. Adhering to these
is useful, as often Python tools will auto discover or recognise files and folders saved in these patterns; and it will
also help other developers to more easily understand your code.

There are examples of typical Python project structures on these sites:

- [Python Packaging User Guide](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/#src-layout-vs-flat-layout)
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/structure/#sample-repository)
- [Real Python](https://realpython.com/python-application-layouts/)

This tutorial project is not the best example, it is not really designed to be an app, it is designed as a weekly series
of activities and so there are repeated module names, repeated code etc. You will likely see lots of warnings in your
IDE about duplicated code!

A more suitable structure for your coursework might be something like the following, though you won't have tests in
coursework 1; and you should use meaningful package and module names and not 'myproject' and 'module1':

```text
my_python_project/
├── README.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── my_python_project/
│   ├── __init__.py
│   ├── main.py
│   ├── module1.py
│   └── module2.py
├── data/
│   ├── processed_data.csv
│   └── raw_data.csv
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_module1.py
│   └── test_module2.py
├── .venv/
```

## Importing modules and functions

You already know how to import from Python libraries, e.g.

```python
from math import sqrt  # import the sqrt module from the math package
import math  # import the math package
```

The [PEP8 style guide](https://peps.python.org/pep-0008/#imports) gives guidance on how to import.
The [Flake8 style checker](https://flake8.pycqa.org/en/stable/internal/writing-code.html#imports) further suggests that
imports should be in a particular order:

1. standard library imports
2. third-party dependency imports
3. local application imports

```python
import pathlib  # a standard library

from flake8 import exceptions  # third party dependency

from tutorialpkg.mypkg2.mymodule2_1 import calculate_area_of_circle  # local application import
```

Note: [some sources](https://docs.python-guide.org/writing/structure/#modules) will recommend that you import the whole
package and not just parts.

If you installed your own code using the `pyproject.toml` file and the command `pip install -e .` then you should also
be able to reference the packages and modules in `tutorialpkg`.

In this case, the following should work:

```python
import tutorialpkg
from tutorialpkg.mypkg2.mymodule2_2 import fetch_user_data
```

## File locations

### The problem with file paths

In this week's activities, and in your coursework, you will use a dataset that is one or more files that are stored in
your project's directory structure. You will need to be able to reference the location of these files in your Python
code.

You should not hard-code the file paths that are specific to your computer when writing code that others will use.

For the coursework, the marker will not have the same directory structure on their computer as you.

The main issues that arise if you hard-code a specific file path are:

1. Windows and Unix/Mac file paths are different.

   Consider a Mac/Unix style file path `/Users/jojo/py_project/test.py`
   and a Windows file path `C:\\Documents\py_project\test.py`. The syntax and structure are different. Further where you
   have the files for a project on your computer is likely different to where someone else does, so using shared code
   where file paths are written using a particular operating system format using a given person's directory structure
   quickly becomes problematic.

2. The root folder can differ depending on your code editor.

   If you are writing code in VSCode and PyCharm then filepath roots are typically the project root, that is you can add
   paths that are relative to your project root and ignore the preceding local file system directory structure. As an
   example a file in the data folder would be `data/file.csv` and not `C:\\Documents\py_project\data\file.csv`
   Different environments and editors may set the project root differently.

3. The relative path can differ depending on where the code is called from.

   If you use a file path in a code file so that it is relative to the current file, you are likely to get issues if you
   then import that file and execute it from another. For example:
   You have the following directories and files: `/data/datafile.csv`, `/module_a/code_a.py`
   and`/module_a/module_b/code_b.py`. In `code_a.py` if you reference the datafile using `../data/datafile.csv` in a
   function that you then import and use inside `code_b.py` you might get an issue as relative to `code_b.py` the data
   file is not in `../data/datafile.csv` but in `../../data/datafile.csv`. It's a little more complex than this,
   however, using relative file paths can lead to problems.

   When you are working with packages in Python then relative paths are relative to the current working directory rather
   than the code file it is written in.

4. Referencing files in web apps introduces further complexity.

   In web apps you will also need to consider that where files are located on a development platform for example is
   likely different to that of the deployed version. This isn't covered in COMP0035.

### Using Python libraries to determine the path

There are different ways you can do this in Python, and differing opinions on which is best. For this course, it doesn't
matter which you choose, it matters more that your files can be located by anyone running your code without making
manual changes to your code to do so.

The two main Python libraries used are both part of the base Python package so you do not need to `pip install` them.
These are `os` and `pathlib`.

Some solutions suggest the use of `os.path` however from Python 3.4 the `pathlib` module was introduced and will be used
in the teaching materials. Using Pathlib addresses many of the above-mentioned issues:

- Avoids the `\\` versus `/` issue by using the Pathlib `joinpath` method.
- Has methods that let you determine the current working directory e.g. `pathlib.Path.cwd()`. For
  example: `my_file_path = pathlib.Path.cwd().joinpath('data','datafile.csv')` instead of `data/datafile.csv`
  or `data\datafile.csv`
- Allows you to code relative to the current code file, whatever that file is
  e.g. `pathlib.Path(__file__).parent` would go to the directory that is the parent of the current file.

For example, given the file structure below:

```text
my_python_project/   (root)
├── this_script.py
├── data/
│   ├── example.csv
```

Then pathlib can be used in `this_script.py` to locate the `example.csv` file:

```python
from pathlib import Path

# This script is located in the project root, so find the path to the current file and then go to the parent of that file
project_root = Path(__file__).parent

# Find the .csv file relative to the project root and join to that path the data folder and then the example.csv file
csv_file = project_root.joinpath('data', 'example.csv')
# csv_file = project_root / 'data' / 'example.csv' # this notation would also work, even though you think the '/' is only unix/macOS

# Check if the file exists, this will print 'true' if it exists
print(csv_file.exists())
```

`Path(__file__)` refers to the file in which the code is i.e. `this_script.py`
`.parent` refers to the parent that the `this_script.py`is in, so `my_python_project` which is the project root, the
highest folder in the project
`.joinpath` takes the current location in this case `my_python_project` and joins to that the `data` directory and then
the `example.csv` so will be `my_python_project/data/example.csv`

You can use the same technique to navigate up through multiple hierarchical directories, 'parents', so given the next
scenario where the script and the data are in different subdirectories:

```text
my_python_project/   (root)
├── src/
│   ├── this_script.py
├── data/
│   ├── example.csv
```

then you can use pathlib like this:

```python
from pathlib import Path

# This script is located in a subfolder so you need to navigate up to the parent (src) and then its parent (project root), then down to the 'data' directory and finally the .csv file
csv_file = Path(__file__).parent.parent.joinpath('data', 'example.csv')
csv_file_v2 = Path(__file__).parent.parent / 'data' / 'example.csv'  # also works

# Check if the file exists
if csv_file.exists():
    print(f"CSV file found: {csv_file}")
else:
    print("CSV file not found.")
```

## Activities

1. Open [mymodule1.py](../../src/tutorialpkg/mypkg1/mymodule1.py)
2. Add imports to allow the following code to run:

   ```python
       if __name__ == '__main__':
           # The functions are in the modules in mypkg2. You will need to import them.

          # Calculate the area of a circle with a radius of 10. Print the result.
          area = calculate_area_of_circle(10)
          print(f"The area is {area}.")

          # Use the fetch_user_data(user_id, database) function to print the data for the user with ID 42 that is in `mock_database` variable.
          print(fetch_user_data(42, mock_database))
    ```
3. Add code to locate the data file `paralmpics_raw.csv` relative to the code file `mymodule1.py` using `pathlib.Path`.
   Prove it exists.


[Go to activity 2.2](2-2-pandas-open.md)

# Sources of information

[The Hitchhiker's Guide to Python: Structuring your project](https://docs.python-guide.org/writing/structure/)

[Python Packaging User Guide: Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

[freeCodeCamp: How to Build Your Very First Python Package](https://www.freecodecamp.org/news/build-your-first-python-package/)

[Real Python: Python Application Layouts: A Reference](https://realpython.com/python-application-layouts/)

[setuptools: Package Discovery and Namespace Packages](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html)

[setuptools: Data Files Support](https://setuptools.pypa.io/en/latest/userguide/datafiles.html)
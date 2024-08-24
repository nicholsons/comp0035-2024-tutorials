# COMP0035 Tutorial 9: Testing (including GitHub Actions for CI and code quality)

## Set up

1. Create a repository on GitHub by creating a copy of the template repository. Go
   to <https://github.com/nicholsons/comp0035-tutorial9> and then press 'Use this template' to create a new repository.

2. Clone the repository from your GitHub account to your computer. Remember to use the URL of your copy of the
   repository and not my repository (ie not the one in step 1 above!).

3. Create and activate a virtual environment.

4. Install pytest and pytest-cov in your virtual environment e.g. `pip install pytest pytest-cov`
   or `pip install -r requirements.txt`

5. Configure your project in your IDE to use a test runner for the library you are using which is pytest. You will need
   to check the documentation for your IDE for instructions.

    - [Pycharm help: Testing frameworks](https://www.jetbrains.com/help/pycharm/testing-frameworks.html)
    - [Python testing in VS Code](https://code.visualstudio.com/docs/python/testing)

## Run a test

In this tutorial the directory structure is given to you. For your own project,
read [choosing a test layout](https://docs.pytest.org/en/7.2.x/explanation/goodpractices.html#choosing-a-test-layout-import-rules)

In your project you have a `tests` directory which contains tests that test the code in the `paralympics` package.
The `paralympics` package is in the `src` directory.

There are different ways to run the tests including:

1. Using menu options in your IDE (in PyCharm and VSCode there is likely a green triangle in the code file that allows
   you to run the test)
2. From the command line (terminal) in your project venv
3. As a `if __name__ == '__main__':` function in your test file

Since everyone should have a venv, this tutorial states code for option 2 (though you can use any of the methods)

Try to run pytest in the top-level folder for the project from the Terminal in your IDE:

```text
python -m pytest -v
```

NB You might need to replace `python` with `python3` or `py` depending on your computer.

The `-v` parameter means verbose and gives you more detail in the terminal as to the tests that have run and any errors.
Refer to the [pytest documentation](https://docs.pytest.org/en/6.2.x/contents.html) for other parameters.

pytest will run all files with names in the form test_*.py or *_test.py in the current directory and its subdirectories.

Running the above line of code will result in an error with output that looks a little like this:

```
tests/test_models.py:3: in <module>
    from paralympics.models import Region
E   ModuleNotFoundError: No module named 'paralympics'
```

Go to the next step to solve this!

## Installing your own code in editable mode

This was covered in the second tutorial and now becomes important. Please refer to tutorial 2 as there is detail that is
not repeated here.

[Pytest good practices](https://docs.pytest.org/en/7.2.x/explanation/goodpractices.html#install-package-with-pip
) tells you to how to set up your project code in your virtual environment (venv).

The `paralympics` directory has an `__init__.py` file which makes it a package. The `__init__.py` file is empty in this
case.

The `src` directory is not a package, it is a directory.

To be able to use `import paralympics` in the code, the `paralympics` package needs to be installed in the venv. This
can be done by installing your code as a package in editable mode.

To do this, you need to have a file called `pyproject.toml` which tells `setuptools` info about how to install your
project and where your packages are. Open the `pyproject.toml` provided in the project files.

From the top-level folder for your project run:

`pip install -e .`

Note that the `.` in the code line above is not a mistake, it is part of the command.

You will get some output in the terminal pane that looks something like this if successful:

```text
(venv) localadmins-MacBook-Pro-7442:comp0035-tutorial9 localadmin$ pip install -e .
Obtaining file:///Users/localadmin/PycharmProjects/comp0035-tutorial9
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Installing backend dependencies ... done
  Preparing editable metadata (pyproject.toml) ... done
Building wheels for collected packages: comp0035-tutorial9
  Building editable for comp0035-tutorial9 (pyproject.toml) ... done
  Created wheel for comp0035-tutorial9: filename=comp0035_tutorial9-1-0.editable-py3-none-any.whl size=1330 sha256=6d46f0b8772d4f050e02a206f174114060c0f5834f0eb6bccc2a724fd238fe20
  Stored in directory: /private/var/folders/3r/90kdpbmj5rq1913cg7l4rhz00000gn/T/pip-ephem-wheel-cache-imsx9zsg/wheels/26/6f/c8/3f35c283f92582acce51867789ea25f7e9d1be816c786fa8ec
Successfully built comp0035-tutorial9
Installing collected packages: comp0035-tutorial9
Successfully installed comp0035-tutorial9-1
```

If you look in the project files pane you may see a hidden directory under the `src` directory
called `comp0035_tutorial9.egg-info`.

Your code should now be available for pytest to discover the `paralympics` package. Run pytest again:

```text
python -m pytest -v
```

It should now run and show something like the following in terminal:

```text
collected 1 item                                                                                                                                                 

tests/test_models.py::test_create_region_valid PASSED 
```

## Run tests with coverage

Coverage is a measure of the extent to which your source code is covered by the tests. There was more information
coverage and its use and limitations in the lecture.

To run the tests with coverage requires the --cov argument to indicate which Python package to check the coverage of a
package.

The following checks to what extent the tests cover the paralympics package.

```text
python -m pytest --cov=paralympics
```

Running the above will result in something like this:

```text
---------- coverage: platform darwin, python 3.11.5-final-0 ----------
Name                          Stmts   Miss  Cover
-------------------------------------------------
src/paralympics/__init__.py       0      0   100%
src/paralympics/models.py        60     31    48%
-------------------------------------------------
TOTAL                            60     31    48%
```

Investigate [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/reporting.html) to see how you can get more
detailed reports, for example:

```
python -m pytest -v --cov=paralympics --cov-report term-missing 
```

Results in something like this which shows which lines of code are not covered by the tests:

```text
---------- coverage: platform darwin, python 3.11.5-final-0 ----------
Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
src/paralympics/__init__.py       0      0   100%
src/paralympics/models.py        60     31    48%   24, 34-49, 53, 64-68, 72, 77-81, 90-91, 100, 108
-----------------------------------------------------------
TOTAL                            60     31    48%

```

You could then use this to identify where you need to write more tests. Remember: the goal is not necessarily 100%
coverage!

## Setup and run the tests on GitHub Actions

How to set up GitHub Actions and understanding the .yml file was covered in the code quality week when it was used to
report on linting results. This is also documented in
the [continuous integration guide](https://nicholsons.github.io/comp0034-5/guide/ci.html)

In summary:

- Go to your repository on GitHub
- Go to the Actions tab
- Find the workflow named 'Python application' and click on 'Configure'
  - You will see a workflow .yml file generated on the screen. Edit this with the following changes:

      - In the section `name: Install dependencies` at the end of this section but before the 'name: Lint with Flake 8'
        add a line to install your code `pip install -e .`
        ```yaml
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install flake8 pytest
            if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
            pip install -e .
        ```       
      - In the section `name: Test with pytest` change the code to run pytest with coverage
        e.g. `python -m pytest -v --cov=paralympics --cov-report term-missing `

      ```yaml
        - name: Test with pytest
          run: |
            python -m pytest -v --cov=paralympics --cov-report term-missing
      ```
    
     - Find the 'commit changes...' button which is likely to top right of the screen and press it. Change the message if you
    wish and then 'Commit changes' again.

This workflow will now run every time you push a change to GitHub. This is useful as it runs all your tests so you can
see if new code you have written breaks any previously working functionality.

To view the results of the workflow:

1. Go to the Action tab again in your GitHub repository.
2. There should be oe workflow run. If all went well it has a green tick, if there were issues there will be a red
   cross.
3. Click on the tick/cross on the workflow.
4. Click on the tick/cross on 'build'.
5. You should now see headings that correspond to the `name: ` sections in the .yml file.
6. Expand the Test with pytest section. The output should look similar to what you saw when you ran the code from the
   terminal.

If there is a red cross then find the section at step 5 that has the red cross, expand it and see what the error message
it. It should say what failed and why. You will then need to fix the error.

If you did not put in the `pip insall -e .` correctly then I'd expect the tests to fail with a module not found error as
happened at the start of this tutorial!

## Write a new test

Now that you can run tests, you need to write some.

A useful way to help you structure tests is to use 'GIVEN-WHEN-THEN'. GIVEN and WHEN tell you what you need to set up
for the test, THEN indicates the assertion (or assertions).

Write a test for the following case:

```python
"""
    GIVEN valid values an Admin object, email='test@test.com' and password='testpassword'
    WHEN the Admin object 'admin' is created
    THEN admin.email should equal 'test@test.com' and admin._password should be longer than 'testpassword' as it 
        is a hashed value
"""
```

1. Write an appropriate test case name

   The test functions inside the test python module (file) typically have the prefix `test_`. The test
   name should make it clear what is being tested e.g. `test_add_success_with_integers` is lengthy but more descriptive
   than `test_add` which only tells you the method being tested and not what behavior you are testing.

2. Add the test description as the docstring

    ```python
    """
        GIVEN valid values an Admin object, email='test@test.com' and password='testpassword'
        WHEN the Admin object 'admin' is created
        THEN admin.email should equal 'test@test.com' and admin._password should be longer than 'testpassword' as it 
            is a hashed value
    """
    ```

3. Write the code to set up the test conditions

    - Create an instance of Admin called 'admin' with the values email='test@test.com', password='testpassword'

4. Write the assertion code

    - Assert that `admin.email` is equal to 'test@test.com'
    - The password is hashed so will be longer than the original, assert that the length of 'admin._password' is longer
      than length of 'testpassword'. You can use Python to get the string length `len('somestring')`

5. Run the test and check it passes.

6. Optionally, commit and push the new code to GitHub and check that GitHub Actions also reported on the test.

## Write a test that raises and exception

The syntax
to [test exceptions](https://docs.pytest.org/en/7.1.x/how-to/assert.html#assertions-about-expected-exceptions) is
different.

Add this test to your code and run it:

```python

def test_invalid_code_raises_error():
    """
    GIVEN invalid data for the Region object code attribute, code="China"
    WHEN the Region object is created
    THEN a ValueException is raised
    """
    with pytest.raises(ValueError):
        Region("China", "China")
```

Now try and write a test for an event that sets the event_type to 'autumn' which should raise a ValueError.

You don't need all the fields to create and Event, the following should work.

```python
Event(event_type="autumn",
      year=2032,
      country="South Africa",
      host="Cape Town",
      noc="RSA",
      start="01/01/2032",
      end="14/01/2032",
      )
```

## Write a test with a fixture

If you find yourself writing tests where you use the same set up steps you can create reusable 'fixtures'.

[Pytest fixtures](https://docs.pytest.org/en/5.4.3/fixture.html#fixture) are used to provide common functions that you
may need for your tests. They are created (set up, yield) and removed (tear down, finalise) using the `@fixture`
decorator.

Fixtures are established for a particular scope using the syntax `@pytest.fixture(scope='module')`. Options for scope
are:

- `function` fixture is executed/run once per test function (if no scope is specified then this is the default)
- `class` one fixture is created per class of tests (if creating test classes)
- `module` fixture is created once per module (e.g., a test file)
- `session` one fixture is created for the entire test session

You may not need to make use of fixtures for COMP0035 coursework, however you will need to use these when we move on to
testing Flask and Dash apps in COMP0034.

Fixtures can be added either within the test file itself or in a separate python file called `conftest.py`. Placing them
in `conftest.py` to make them available to other test modules. `conftest.py` is typically placed in the root of
the `tests` directory, though you can have multiple `conftest.py` files (not covered here).

Create a pytext fixture for the details needed to create a paralympic event.

Add the following to the top of the `test_modules.py` file after the imports. You will need to
add `paralympics.models.Event` to the imports.

```python
from paralympics.models import Event


@pytest.fixture(scope='function')
def event():
    e = Event(event_type="winter", year=2032, country="South Africa", host="Cape Town", noc="RSA",
              start="01/01/2032", end="14/01/2032", disabilities_included="", countries=0, events=15,
              sports=0, participants_m=0, participants_f=0, participants=0, highlights="")
    return e
```

To use your fixture in a test, try adding the following to 'test_models.py':

```python
def test_event_created_with_valid_data(event):
    """
    GIVEN valid data for the Event object
    WHEN the Event object called event is created
    THEN check the event attributes are correct
    """
    assert event.event_type == "winter"
    assert event.year == 2032
    assert event.country == "South Africa"
    assert event.host == "Cape Town"
    assert event.noc == "RSA"
    assert event.start == "01/01/2032"
    assert event.end == "14/01/2032"
    assert event.disabilities_included == ""
    assert event.countries == 0
    assert event.events == 15
    assert event.sports == 0
    assert event.participants_m == 0
    assert event.participants_f == 0
    assert event.participants == 0
    assert event.highlights == ""
```

Try and add fixtures for a Region and an Admin.

## Write your own tests

Try and write some more tests.

Look at the classes in `src/paralympics/models.py` and determine tests e.g.

- test for an invalid password using Admin check_password() method
- test creating an event with the event_type as 'autumn' - it should raise a value error
- test that changing a password does set it to the new password, test that the old password is no longer valid

You should be able to come up with other ideas.

Create some that use fixtures and some that don't.

## Testing with GitHub CoPilot / ChatGPT

There are various ways to use the tools to help you.

The following assume you have the CoPilot extension for VS Code or the CoPilot Plugin for Pycharm.

[GitHub docs](https://docs.github.com/en/copilot/getting-started-with-github-copilot?tool=jetbrains) explain how to
setup and use CoPilot in PyCharm and VS Code.

- Write clear 'prompts' as docstrings or comments in the code. Move the cursor to the end of the comment and then use
  the instructions for your IDE to invoke CoPilot. Alternatively use the docstring, comment or prompts in ChatGPT.
- In VS Code write tests by going to the class code within src/paralympics/models.py, go to a class definition, right
  click and select **Copilot** then **Generate Tests**.
- In PyCharm as soon as you start to write the test case PyCharm should prompt a suggestion (assuming CoPilot is
  enabled).

Try using CoPilot or ChatGPT to generate tests for you and compare their code to yours.

## Further information

You can extend your knowledge of testing by the following:

- test
  for [error conditions (exceptions)](https://docs.pytest.org/en/7.1.x/how-to/assert.html#assertions-about-expected-exceptions)
- edge cases (handling extreme values of valid limits, some also test values beyond the limit (boundary value testing))
- organise tests in classes - this is an alternative way to group tests, it may
  have [advantages in some scenarios](https://stackoverflow.com/questions/50016862/grouping-tests-in-pytest-classes-vs-plain-functions).
- [parameterised tests](https://docs.pytest.org/en/latest/how-to/parametrize.html)
- [doctests using the docstrings](https://realpython.com/python-doctest/)
- use of mocks ([pytest-with-eric tutorial](https://pytest-with-eric.com/pytest-advanced/pytest-mocking/))

Other tutorials:

- [RealPython: Effective testing with Python](https://realpython.com/pytest-python-testing/)
- [freeCodeCamp: Python testing for beginners (video)](https://www.youtube.com/watch?v=cHYq1MRoyI0) - includes mocks and
  using ChatGPT for testing
- [Getting started with CoPilot](https://realpython.com/github-copilot-python/)

## Potential solutions

test_modules.py (NB: the fixtures are all in `confest.py`)

```python
import pytest
from paralympics.models import Admin, Event, Region


def test_create_admin_with_valid_data():
    """
        GIVEN valid values an Admin object, email='test@test.com' and password='testpassword'
        WHEN the Admin object 'admin' is created
        THEN admin.email should equal 'test@test.com' and admin._password should be longer than 'testpassword' as it 
        is a hashed value
        """
    admin = Admin(email='test@test.com', password='testpassword')
    assert admin.email == 'test@test.com'
    assert len(admin._password) > len('testpassword')
```

conftest.py

```python
import pytest

from paralympics.models import Region, Admin, Event


@pytest.fixture(scope='function')
def event():
    event = Event(event_type="winter", year=2032, country="South Africa", host="Cape Town", noc="RSA",
                  start="01/01/2032", end="14/01/2032", disabilities_included="", countries=0, events=15, sports=0,
                  participants_m=0, participants_f=0, participants=0, highlights="")
    return event


@pytest.fixture(scope='function')
def region():
    region = Region(region="Zedzedzedland", code="ZZZ", notes="This is a fictitious country.")
    return region


@pytest.fixture(scope='function')
def admin():
    admin = Admin(email="admin@test.com", password="adminpassword")
    return admin

```

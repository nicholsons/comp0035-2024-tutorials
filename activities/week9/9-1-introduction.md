# Introduction to unit testing

Please read the following guidance before you start to write unit test code.

## Unit testing in Python

Unit testing is a method for testing software that looks at the smallest testable pieces of code, i.e. a 'units'.

Unit testing aims to verify that each part of the code, including helper functions that may not be exposed to the user,
work correctly and as intended.

Other types of testing, such as integration tests, were covered in the lecture but are not covered in this tutorial or
the coursework. Integration testing will be covered in COMP0034.

In Python, the [unittest](https://docs.python.org/3/library/unittest.html) package is bundled with the main Python
installation. This tutorial covers [pytest](https://docs.pytest.org/en/stable/getting-started.html) which extends
unittest, and needs to be installed to use it (e.g. using `pip install pytest`). Pytest is
covered in this tutorial as you will also need to use it next term in COMP0034.

## Patterns in testing

There are common patterns for testing that if followed make it easier for you to write and run the test code, and for
others to understand it.

### General guidance

Unit tests typically test functions, methods, and classes.

They are short and focused on one behaviour/thing/variation.

They should not have any external dependencies. Where these are needed a 'mock' of the external thing should be used
instead.

Tests should run independently of each other. They should be runnable in any order.

Tests should be self-descriptive and intuitively understandable.

### Test directory structure

There are typical patterns for where to place the tests for an application.

Two
common [project layout patterns](https://docs.pytest.org/en/stable/explanation/goodpractices.html#choosing-a-test-layout)
are to place the tests in a separate directory outside the application code:

```text
├── pyproject.toml
├── src/
│   ├──package/
│   │   ├── __init__.py
│   │   ├── my_module.py
├── tests/
│   ├── test_my_module.py
```

Or to place tests within the application.

```text
├── pyproject.toml
├── src/
│   ├── package/
│   │   ├── __init__.py
│   │   ├── my_module.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_my_module.py
```

The course activities all follow the first of these as it separates the packaging of the
application code from the code that tests it.

### Test naming

Packages such as pytest will detect test files that follow certain naming patterns.

The directory containing the tests is usually named 'tests' or 'test'.

The test modules file names are prefixed with `test_` such as `test_module.py` or suffixed with `_test` such as
`module_test.py`.

The test file name typically also refers to the module, package or feature being tested; though this does not affect
auto discovery of tests.

The tests cases within the modules may be written as classes or functions. The naming convention should make it clear
what they test, e.g. `class TestMyPackage` is a class containing test cases for the MyPackage package.
`test_redirect_success` tests that a call to a given url successfully redirects.

In general, you should have a pretty good idea what the test is testing for from its name. Given this, test names such
as `test_function_a_1`, `test_function_a_2` etc. are not considered a good style, while they relate to 'function a',
it is not clear what 1 and 2 refer to.

The way that Pytest discovers names
is [documented here](https://docs.pytest.org/en/stable/explanation/goodpractices.html#conventions-for-python-test-discovery).

### GIVEN-WHEN-THEN pattern

This pattern can help to determine the behaviour to be tested.

It is from an approach referred to as behaviour driven development and you will see guides that reference
the [Gherkin](https://cucumber.io/docs/gherkin/) syntax that follow this. You do not need to understand this syntax to
use the general GIVEN>WHEN>THEN structure to help you think about your tests.

For example:

```text
Test Scenario: Simple Google search
    Given the Google home page is displayed
    When the user searches for "Python pandas"
    Then the results page shows links related to "Python pandas"
```

In the course materials I typically use this pattern for the test case documentation or docstring.

These elements then flow to the structure of the code which is described in the next section.

For an example see [Pytest with eric](https://pytest-with-eric.com/bdd/pytest-bdd/).

### ARRANGE-ACT-ASSERT pattern

This pattern for the structure of writing tests is referenced in the pytest documentation.

It follows the same general approach as above: (Given > Arrange) (When > Act) (Then > Assert )

It is a way of structuring the code within your tests:

1. **Arrange**: Set up everything the test will need before starting, e.g. initialise a test object, access a database,
   login to a web app.
2. **Act**: Carry out some action on the thing that is being tested. For example a function or method call; call a REST
   API; interact with a web page.
3. **Assert**: Verify that the action produced the expected result. Sometimes, assertions are as simple as checking
   numeric or string values. Other times, they may require checking multiple aspects of an application. Assertions
   determine if the test passes or fails.

The following example shows a unit test
for [Python's absolute value function](https://www.w3schools.com/python/ref_func_abs.asp):

```python
def test_abs_for_a_negative_number():
    # Arrange: define a negative number to be tests
    negative = -6

    # Act: call the function to be tested and pass the negative number
    answer = abs(negative)

    # Assert: use a pytest assertion, in this case the 'correct' behaviour from the function 
    # when called on -6 is to return 6
    assert answer == 6
```

[Next activity](9-2-unit-testing.md)
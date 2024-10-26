# Going further

There is more to unit testing with Pytest than can be covered in one tutorial.

If you are interested, investigate other aspects such as:

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
# Coverage

## What is coverage?

In software testing, coverage refers to a metric that measures the extent to which the codebase is tested by a set of
test cases. It helps ensure that the tests are validating the functionality and quality of the software. It

Theoretically, the higher code coverage is, the fewer defects a system should have. This depends on the tests, and unit
testing alone is unlikely to be sufficient to catch all kinds of errors.

Aiming for 100% coverage is not usually practical due to the cost and time; nor necessary depending on the impact if the
system were to fail. [This Google blog post](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html)
provides a summary of the implications of coverage; and in it, they suggest that for their organisation:
> ... at Google we offer the general guidelines of 60% as "acceptable", 75% as "commendable" and 90% as "exemplary".

For the coursework you might achieve 100% since your code base is relatively small.

## Python coverage tools

Tools that measure coverage report the results; typically to a specified output such as the terminal, a text file or
HTML.

[`coverage.py`](https://pypi.org/project/coverage/) is a widely used Python coverage tool. [
`pytest-cov`](https://pypi.org/project/pytest-cov/) extends coverage with additional reporting.

The tools report on aspects such as:

- the number of statements in the code base that are covered by tests
- identifying lines of code not covered by tests
- branch coverage: for example, if-statements (and similar mechanisms) direct execution flow of the code. Possible code
  paths are called branches. Branch coverage reports on how many of these different pathways are covered by tests.

Some tools will also cover other aspects of coverage.

## Pytest coverage using pytest-cov

Perhaps the simplest way to run coverage is to execute at the command line when running pytest, with the results output
to the Terminal.

```terminal
pytest --cov 
```

Which would give a report similar to the following:

```text
---------- coverage: platform darwin, python 3.11.5-final-0 ----------
Name                          Stmts   Miss  Cover
-------------------------------------------------
src/paralympics/__init__.py       0      0   100%
src/paralympics/models.py        60     31    48%
-------------------------------------------------
TOTAL                            60     31    48%
```

Whereas for an HTML formatted report saved to a directory called 'coverage_report' try:

```terminal
pytest --cov --cov-report=html:coverage_report
```

Other options that can be specified include:

- the path of the code to report coverage on: `-cov=PATH`
- reporting on the lines of code not covered (missed) by the tests: `–cov-report=term-missing`
- reporting on branch coverage: `–cov-branch`

Reporting can also be integrated in the GitHub Actions workflow. Update the line in the .yml to include a line to report
the coverage, e.g.:

```yaml
  - name: Test with pytest
      run: |
        pytest --cov
```

## Try it

Run the tests you have written for this tutorial again and include one of the options for reporting on coverage.

[Next activity](9-6-ai-testing.md)
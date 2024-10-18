"""Poorly formatted code.
    This is a module that contains a function that will be linted in activity 3.6
"""

globalTEST = 'This is a global variable'

def inCorrect_functionName():
    print('This is a function with a poorly formatted name')


def missing_docstring(message):
    print(message)
    print("This is a function that is missing it's docstring")
    result = "message printed"
    return result

def incorrect_spacing_between_functions():
    print('This function has incorrect spacing between it and the function above')


def incorrect_spacing_between_functions():
    print("This is a duplicated function name")


def incorrect_whitespace(x, y):
    result =  x+y
    print(result)
    return result
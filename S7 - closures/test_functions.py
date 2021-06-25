import pytest
import random
# Importing all four functions from functions.py module
from functions import *
import functions


"""
###########  fibonacci Function ############
"""

def test_fibonacci_random_output():
    obj = fibonacci()
    rand = random.randint(1,11)
    print(rand)
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,]
    for i in range(rand):
        output = obj()
        print(output)
    assert output == expected[rand-1], "Output of fibonacci number doesn't seem right."
    

"""
###########  check_docstrings Function ############
"""

def test_check_docstrings_non_int_input():
    try:
        obj = check_docstrings(1.1)
    except AssertionError as e:
        assert str(e) == '`docstring_length` can only be a positive integer', 'The input param `docstring_length`' \
            'can only be integer.'
        pass
    else:
        raise AssertionError(f'Edge Case Not Handled - The input param `docstring_length` can only be integer.')
    
    
def test_check_docstrings_non_negative_input():
    try:
        obj = check_docstrings(-11)
    except AssertionError as e:
        assert str(e) == '`docstring_length` cannot be negative', 'The input param `docstring_length` cannot be negative.'
        pass
    else:
        raise AssertionError(f'Edge Case Not Handled - The input param `docstring_length` cannot be negative.')
    
    
def test_check_docstrings_True_behavior():
    obj = check_docstrings(10)
    
    def docstring_func():
        """This is more than 10 characters of docstring.
        """
        pass
    
    output = obj(docstring_func)
    assert output is True, 'Incorrect output from the function.'


def test_check_docstrings_False_behavior():
    obj = check_docstrings(100)
    
    def docstring_func():
        """This is more than 10 characters of docstring.
        """
        pass
    
    output = obj(docstring_func)
    assert output is False, 'Incorrect output from the function.'

   
"""
###########  call_counter_log_global Function ############
"""

def test_call_counter_log_global_mul():
    obj = call_counter_log_global(mul)
    assert obj(5,6) == 30, "it should multiply the two numbers"

def test_call_counter_log_global_mul_dict_check():
    obj = call_counter_log_global(mul)
    obj(5,6)
    obj(5,8)
    assert count_dict == {'mul': 3}, "it should match the dictionary"

def test_call_counter_log_global_add():
    obj = call_counter_log_global(add)
    assert obj(5,6) == 11, "it should add the two numbers"

def test_call_counter_log_global_add_dict_check():
    obj = call_counter_log_global(add)
    obj(5,6)
    obj(5,8)
    assert count_dict == {'mul': 3, 'add': 3,}, "it should match the dictionary"

def test_call_counter_log_global_div():
    obj = call_counter_log_global(div)
    assert obj(10,2) == 5, "it should divide the two numbers correctly"

def test_call_counter_log_global_div_dict_check():
    obj = call_counter_log_global(div)
    obj(5,6)
    obj(5,8)
    assert count_dict == {'mul': 3, 'add': 3, 'div': 3}, "it should match the dictionary"


"""
###########  call_counter_log Function ############
"""

def test_call_counter_log_mul():
    data = {}
    obj = call_counter_log(mul, data)
    assert obj(5,6) == 30, "it should multiply the two numbers"

def test_call_counter_log_mul_dict_check():
    data = {}
    obj = call_counter_log(mul, data)
    obj(5,6)
    obj(5,8)
    assert data == {'mul': 2}, "it should match the dictionary"
    
def test_call_counter_log_add():
    data = {}
    obj = call_counter_log(add, data)
    assert obj(5,6) == 11, "it should add the two numbers"

def test_call_counter_log_add_dict_check():
    data = {}
    obj = call_counter_log(add, data)
    obj(5,6)
    obj(5,8)
    assert data == {'add': 2}, "it should match the dictionary"

def test_call_counter_log_div_dict_check():
    data = {}
    obj = call_counter_log(div, data)
    obj(5,6)
    obj(5,8)
    assert data == {'div': 2}, "it should match the dictionary"

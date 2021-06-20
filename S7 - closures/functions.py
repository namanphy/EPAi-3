"""
The file contains the function to generate the next Fibonacci number.
"""
from typing import Callable

# count_dict = dict()

def fibonacci():
    """This is a closure. It returns a funcrion that generates the next Fibonacci number every time the instance of 
    this closure is called.

    Returns:
        callable: Function to generate the next Fibonacci number.
    
    Closure Function Returns:
        int: The next Fibonacci number.
    """
    n1, n2 = 0, 1
    def calc_next_number():
        nonlocal n1, n2
        nth = n1 + n2
        n1 = n2
        n2 = nth
        return nth
    return calc_next_number


def check_docstrings(docstring_length: int = 50):
    """It is a closure. It returns a funcrion that check whether the function passed has a docstring with more than 
    given characters or not.

    Args:
        docstring_length (int, optional): The required minimum length of the docstring. Defaults to 50.

    Returns:
        callable: Function to check whether the function passed has a docstring with more than 50 characters.
        
    Closure Function Returns:
        bool: True if given function has a docstring with more than 50 characters else False.
    """

    assert type(docstring_length) == int, "`docstring_length` can only be a positive integer"
    assert docstring_length >= 0, "`docstring_length` cannot be negative"
    def check(func: Callable):
        nonlocal docstring_length
        docs = func.__doc__
        if docs:
            docs_length = len(docs)
            if docs_length < docstring_length:
                print(f"Error: Docstring length is less than {docstring_length}")
                return False
            else:
                return True
        print("Error: No docstrings found.")
        return False
    return check


def call_counter_log_global(func: Callable):
    """It is closure. It returns a same function as input with counts how many times a given function was called and updates
    the count in a global dictionary.

    Args:
        func (Callable): The function whose call count is to be tracked.

    Returns:
        callable: The same function whose check the call count for the given function.
    """

    global count_dict
    count_dict = dict()
    print("Initializing a global dictionary named - `count_dict`")
    cnt = 0
    def count(*args, **kwargs):
        nonlocal count
        cnt =+ 1
        count_dict[func.__name__] = cnt
        return func(*args, **kwargs)
    return count


def call_counter_log(func: Callable, count_dict: dict):
    cnt = 0
    def count(*args, **kwargs):
        nonlocal cnt
        nonlocal count_dict
        cnt =+ 1
        count_dict[func.__name__] = cnt
        return func(*args, **kwargs)
    return count

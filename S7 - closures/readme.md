# Closures

Four different closures are implemented here. For each the closure function, there are test associated ensuring the bug 
free working of the functions.


## 1. `fibonacci()`
A closure that gives you the next Fibonacci number.

```
def fibonacci()
    count = 0
    n1, n2 = 0, 1
    def calc_next_number():
        nonlocal n1, n2, count
        if count == 0:
            count += 1
            return n1
        elif count == 1:
            count += 1
            return n2
        nth = n1 + n2
        n1 = n2
        n2 = nth
        return nth
    return calc_next_number
```



## 2. `check_docstrings()`
A closure that takes a function and then check whether the function passed has a docstring with more than `n`(Given) characters.

```
def check_docstrings(docstring_length: int = 50):
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
```



## 3. `call_counter_log_global()`
A closure that counts how many times a function was called and update a global dictionary variable with the counts.

```
def call_counter_log_global(func: Callable):
    global count_dict    
    if func.__name__ not in count_dict.keys():
        count_dict[func.__name__] = 0

    def count(*args, **kwargs):
        count_dict[func.__name__] += 1
        return func(*args, **kwargs)
    return count
```



## 4. `call_counter_log()`
A closure that counts how many times a function was called and update a dictionary that is passed as parameter to the function.


```
def call_counter_log(func: Callable, count_dict: dict):
    if func.__name__ not in count_dict.keys():
        count_dict[func.__name__] = 0

    def count(*args, **kwargs):
        nonlocal count_dict
        count_dict[func.__name__] += 1
        return func(*args, **kwargs)
    return count
```

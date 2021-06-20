import pytest
import random
# Importing all four functions from functions.py module
from functions import *


def test_fibonacci_random_output():
    obj = fibonacci()
    rand = random.randint(1,11)
    print(rand)
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,]
    for i in range(rand):
        output = obj()
        print(output)
    assert output == expected[rand-1], "Output of fibonacci number doesn't seem right."
    
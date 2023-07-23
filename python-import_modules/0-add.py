#!/usr/bin/python3

"""Import a simple function"""

from add_0 import add

a = 1
b = 2
result = add(a, b)

print("{} + {} = {}".format(a, b, result))
if add.__name__ != 'add':
    print("Warning: The add function is not the correct function from add_0.py")

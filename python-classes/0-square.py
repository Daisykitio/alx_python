"""
Module 0-square
==============

This module defines the Square class that represents a square with a private
attribute "size". The size attribute is essential for a square as it is used in
computing the area and other operations. Keeping it private ensures proper
control over its value and type.

Example:
    # Create a square with size 5
    square = Square(5)
"""
class Square:
    def __init__(self, size):
        self.__size = size

# Testing the Square class
if __name__ == "__main__":
    square = Square(5)
    # Accessing the private attribute directly will raise an AttributeError
    # print(square.__size)  # This would raise an AttributeError

    # Accessing the private attribute using a "name mangling" syntax (_ClassName__attribute)
    # This is not recommended as it violates the encapsulation principle
    print(square._Square__size)

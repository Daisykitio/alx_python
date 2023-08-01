"""
Module 1-square
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
    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

# Testing the Square class
if __name__ == "__main__":
    try:
        square1 = Square(5)
        print("square1 size:", square1._Square__size)  # Output: 5

        square2 = Square()  # Default size (0)
        print("square2 size:", square2._Square__size)  # Output: 0

        # Testing with invalid sizes
        square3 = Square("invalid")  # Raises TypeError
        square4 = Square(-2)  # Raises ValueError
    except Exception as e:
        print("Error:", e)


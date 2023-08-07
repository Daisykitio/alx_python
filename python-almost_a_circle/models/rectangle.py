"""
models.rectangle
================

This module contains the definition of the Rectangle class, which inherits from the Base"""

from models.base import Base

class Rectangle(Base):
    """The Rectangle class represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle's position. Defaults to 0.
            y (int, optional): y-coordinate of the rectangle's position. Defaults to 0.
            id (int, optional): ID of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Existing properties and setters...

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Display the rectangle using '#' characters, considering x and y positions."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a custom string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update attributes with the provided arguments."""
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)


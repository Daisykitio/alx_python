"""
models.rectangle
================

This module contains the definition of the Rectangle class, which inherits from the Base"""
from models.base import Base

class Square(Rectangle):
    """The Square class represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the Square class.

        Args:
            size (int): Size of the square (same as width and height).
            x (int, optional): x-coordinate of the square's position. Defaults to 0.
            y (int, optional): y-coordinate of the square's position. Defaults to 0.
            id (int, optional): ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    # The __str__ method is inherited from Rectangle

    def update(self, *args, **kwargs):
        """Update attributes with the provided arguments."""
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    @property
    def size(self):
        """Getter for the size attribute (same as width and height)."""
        return self.width
    
    @size.setter
    def size(self, value):
        """Setter for the size attribute  (same as width and height)."""
        self.width = value
        self.height = value

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


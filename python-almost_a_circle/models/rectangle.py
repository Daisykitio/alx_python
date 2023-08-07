"""
models.rectangle
================

This module contains the definition of the Rectangle class, which inherits from the Base class.
"""
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
    

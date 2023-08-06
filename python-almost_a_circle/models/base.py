"""This module contains the definition of the Base class, which is the base of all other classes in this project."""

class Base:
    """The Base class is used as the base for all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for the Base class.

        If `id` is provided, assign it to the public instance attribute `id`.
        Otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

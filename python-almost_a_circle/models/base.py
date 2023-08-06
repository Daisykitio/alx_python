class Base:
    # Private class attribute to keep track of objects created
    __nb_objects = 0

    def __init__(self, id=None):
        # If id is provided, assign it to the public instance attribute id
        if id is not None:
            self.id = id
        else:
            # Increment __nb_objects and assign the new value to id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


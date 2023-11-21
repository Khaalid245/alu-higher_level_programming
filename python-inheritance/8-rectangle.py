#!/usr/bin/python3
"""Module for the Rectangle class"""

class BaseGeometry:
    """A class representing base geometry"""

    def area(self):
        """Placeholder method for area calculation"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value as an integer greater than 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """A class representing a rectangle"""

    def __init__(self, width, height):
        """Initialize a rectangle instance"""
        super().__init__()
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return the rectangle representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

# For testing purposes
if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r)
    print(dir(r))

    try:
        print("Rectangle: {} - {}".format(r.__width, r.__height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

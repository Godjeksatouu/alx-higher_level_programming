#!/usr/bin/python3
class Square:
    """
    Represents a square object.
    """
    def __init__(self, side_length=0):
        """
        Initializes an instance of a square.

        Args:
            side_length (int): Length of the square's side.
                It must be a positive integer.
        """
        if type(side_length) is not int:
            raise TypeError("side_length must be an integer")
        if side_length < 0:
            raise ValueError("side_length must be >= 0")
        self.__side_length = side_length

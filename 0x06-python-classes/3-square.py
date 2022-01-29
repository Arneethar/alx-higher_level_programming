#!/usr/bin/python3
"""Defining a class square"""

class Square:
    """Initializing a square
    Args:
    params(int):size of the square
    """
    def __init__(self,size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueErroe("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

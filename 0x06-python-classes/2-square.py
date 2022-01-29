#!/usr/bin/python3
"""Defining a class square"""
class Square:
    """instantiatio with optional size
    private instance attritube: size

    Args:
    param 1(int): size is optional.
    """
    def __init__(self,size=0):
        try:
            if not isinstance(size,int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
        finally:
            self.size = size

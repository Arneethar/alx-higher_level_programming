#!/usr/bin/python3
"""
Private instance attribute: size:
  property def size(self): to retrieve it
  property setter def size(self, value): to set it:
  size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Private instance attribute: position:
  property def position(self): to retrieve it
  property setter def position(self, value): to set it:
  position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
position should be use by using space - Don’t fill lines by spaces when position[1] > 0
"""
class Square:
  """This class creates a square"""
  def __init__(self,size = 0,position=(0, 0)):
    self.__size = size
    self.__position = position
    

  @property
  def size(self):
    """Returns the current size"""
    return self.__size

  @size.setter
  def size(self,value):
    if not isinstance(value, int):
      raise TypeError("size must be an integer")
    elif value < 0:
      raise ValueError("size must be >= 0")
    self.__size = value

  @property
  def position(self):
    """Return the current position"""
    return self.__position

  @position.setter
  def position(self,value):
    if not isinstance(value,tuple):
      if len(value) != 2:
        if value[0] < 0 and value[1] < 0:
          raise TypeError("position must be a tuple of 2 positive integers")
    self.__position = value


  def area(self):
    """Returns the area of self"""
    return self.__size ** 2

  def my_print(self):
    if self.__size == 0:
          print()
          return
    for ch in range(self.__position[1]):
      print()
    leng = self.__position[0]
    for ch in range(self.__size):
      print("{}{}".format(" "*leng,"#"*self.__size),end="")
      print()

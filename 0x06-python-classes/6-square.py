#!/usr/bin/python3
"""
Defining a square class
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
    if (not isinstance(value,tuple) or len(value) != 2) or not all(isinstance(num, int) for num in value) or not all(num >= 0 for num in value):
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

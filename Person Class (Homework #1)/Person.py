#####################################################################
# author: Logan Stelter
# date: 3/12/23
# description: A simple Class that can move and find distance from another "player" as well a print it's variables.
#####################################################################
# import math for sqrt()
import math

# global Constants to restrict the maximum x and y values that a person object
# can have.
MAX_X = 800
MAX_Y = 600

# A class representing a person. A person can be initialized with a
# name, as well as x and y coordinates. However, there are default
# values for all those (i.e. player 1, 0 and 0 respectively). A person
# also has a size which is set to 1 by default. A person can go left, 
# go right, go up and go down. A person also has a string function 
# that prints out their name location, and size. A person also has a 
# function that calculates the euclidean distance from another person 
# object.
class Person:
    def __init__(self, name = "name 1", x = 0, y = 0, size = 1):
        self.name = name
        self.x = x
        self.y = y
        self.size = size
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        if len(val) >= 2:
            self._name = val
        else:
            self._name = "name 1"
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, val):
        if val <= 0:
            self._x = 0
        elif val >= MAX_X:
            self._x = MAX_X
        else:
            self._x = val

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, val):
        if val <= 0:
            self._y = 0
        elif val >= MAX_Y:
            self._y = MAX_Y
        else:
            self._y = val

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, val):
        if val >= 1:
            self._size = val
    
    def goLeft(self, distance = 1):
        self.x -= distance

    def goRight(self, distance = 1):
        self.x += distance

    def goUp(self, distance = 1):
        self.y -= distance

    def goDown(self, distance = 1):
        self.y += distance
    
    def getDistance(self, other):
        return math.sqrt(((other.x - self.x)**2)+((other.y - self.y)**2))
    
    def __str__(self):
        return f"Person({self.name}):\tsize = {self.size},\tx = {self.x}\ty = {self.y}"

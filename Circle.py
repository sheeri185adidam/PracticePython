import math
from Shape import Shape

class Circle(Shape):
    '''Definition of a Circle shape class'''
    def __init__(self, radius):
        super(Shape, self).__init__()
        self.__radius = radius
 
    def get_name(self):
        print("Circle")

    def get_radius(self):
        return self.__radius
 
    def set_radius(self, radius):
        self.__radius = radius
 
    def get_area(self):
        return math.pi * self.__radius ** 2
 
    def get_perimeter(self):
        return 2 * math.pi * self.__radius
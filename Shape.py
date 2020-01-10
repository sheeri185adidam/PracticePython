import math

class Shape(object):
    ''' This function defines shape base class'''     
    def __init__(self, color='black', filled=False):
        self.__color = color
        self.__filled = filled
        self.__area = 0
        self.get_name()

    def get_name(self):
        print("Shape")

    def get_color(self):
        return self.__color
 
    def set_color(self, color):
        self.__color = color
 
    def get_filled(self):
        return self.__filled
 
    def set_filled(self, filled):
        self.__filled = filled

    def get_area(self):
        return self.__area
#---------------------------------logic----------------------------------------
#   1- read photo
#   2- resize photo
#   3- convert photo to numpy array
#   4- for each pixel in photo use set_color to set color of word in text
#   5- save it as .sh file
#   6- run it

#-----------------------------import libraries---------------------------------

#import modules
import os
from PIL import Image
from numpy import asarray

#--------------------------create class and functions---------------------------

class Photo:
    def __init__(self,path = 'IMG.jpg', text=" ", size='30*50', front=False,
                 height = 50, width = 30):
        self.__path = path
        self.__text = text
        self.__size = size
        self.__front = front
        self.__height = height
        self.__width = width
        
    #setters
    
    def set_path(self, path):
        if type(path) == str:
            self.__path = path
        else:
            print("path must be a string")

    def set_text(self, text):
        self.__text = str(text)

    def set_size(self, size):
        self.__size = size

    def set_front(self, front):
        if type(front) == bool:
            self.__front = front
        else:
            print("front must be a boolean")

    def set_height(self, height):
        if type(height) == float or type(height) == int:
            self.__height = height

    def set_width(self, width):
        if type(width) == float or type(width) == int:
            self.__width = width
    #getters

    def get_path(self):
        return self.__path

    def get_text(self):
        return self.__text

    def get_size(self):
        return self.__size

    def get_front(self):
        return self.__front

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

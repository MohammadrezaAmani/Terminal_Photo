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
    def __init__(self, path='IMG.jpg', text=" ", size='30*50', front=False):
        """Photo class constructor
        this class get some parameters and set and use them to create a colored text from photo

        Args:
            path (str, optional): [path of image]. Defaults to 'IMG.jpg'.
            text (str, optional): text to be shown in foreground. Defaults to " ".
            size (str, optional): text of image in width*height format, example = 30*50. Defaults to '30*50'.
            front (bool, optional): ro set color in background = False, in foreground = True. Defaults to False.
        """
        self.__path = path
        self.__text = text
        self.__size = size
        self.__front = front
        self.__height = size.split('*')[1]
        self.__width = size.split('*')[0]

    #------------setters------------
    # 1. path setter
    def set_path(self, path):
        if type(path) == str:
            self.__path = path
        else:
            print("path must be a string")
    # 2. text setter

    def set_text(self, text):
        self.__text = str(text)
    # 3. size setter

    def set_size(self, size):
        if type(size) == str:
            if size.find('*') != -1:
                self.__size = size
            else:
                print("size must be a string in format 'width*height' exapmle: '30*50'")
        else:
            print("size must be a string")
    # 4. front setter (True or False)

    def set_front(self, front):
        if type(front) == bool:
            self.__front = front
        else:
            print("front must be a boolean")
    # 5.height settter

    def set_height(self, height):
        if type(height) == float or type(height) == int:
            self.__height = height
    # 6. width setter

    def set_width(self, width):
        if type(width) == float or type(width) == int:
            self.__width = width
    #-----------------getters-----------------
    # 1. path getter

    def get_path(self):
        return self.__path
    # 2. text getter

    def get_text(self):
        return self.__text
    # 3. size getter

    def get_size(self):
        return self.__size
    # 4. front getter

    def get_front(self):
        return self.__front
    # 5. height getter

    def get_height(self):
        return self.__height
    # 6. width getter

    def get_width(self):
        return self.__width
    
    #-----------------functions-----------------
    # set color of pixel in photo
    def set_color(r, g, b, text = ' ', position = 48):
        """this function get the color of each pixel in photo and
           set it to the color of the word in text

        Args:
            r ([int]): [red color]
            g ([int]): [green color]
            b ([int]): [blue color]
            text (str, optional): [a char to be shown]. Defaults to ' '.
            position (int, optional): [color is for foreground or background, forground = 38, background = 48 ]. Defaults to 48.

        Returns:
            [str]: [color and text of pixel]
        """
        return '\033[{};2;{};{};{}m'.format(position,r, g, b) + text + '\033[0m'

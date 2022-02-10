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

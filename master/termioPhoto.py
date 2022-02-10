#---------------------------show photo in terminal----------------------------
# author: Mohammadreza Amani
# GitHub: https://www.github.com/MohammadrezaAmani
# Linkedin: https://www.linkedin.com/in/mohammadreza-amani/
# Date: 2021/11/18

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
    def setPath(self, path):
        if type(path) == str:
            self.__path = path
        else:
            print("path must be a string")
    # 2. text setter

    def setText(self, text):
        self.__text = str(text)
    # 3. size setter

    def setSize(self, size):
        if type(size) == str:
            if size.find('*') != -1:
                self.__size = size
                self.__height = size.split('*')[1]
                self.__width = size.split('*')[0]
            else:
                print("size must be a string in format 'width*height' exapmle: '30*50'")
        else:
            print("size must be a string")
    # 4. front setter (True or False)

    def setFront(self, front):
        if type(front) == bool:
            self.__front = front
        else:
            print("front must be a boolean")
    # 5.height settter

    def setHeight(self, height):
        if type(height) == float or type(height) == int:
            self.__height = height
    # 6. width setter

    def setWidth(self, width):
        if type(width) == float or type(width) == int:
            self.__width = width
    #-----------------getters-----------------
    # 1. path getter

    def getPath(self):
        return self.__path
    # 2. text getter

    def getText(self):
        return self.__text
    # 3. size getter

    def getSize(self):
        return self.__size
    # 4. front getter

    def getFront(self):
        return self.__front
    # 5. height getter

    def getHeight(self):
        return self.__height
    # 6. width getter

    def getWidth(self):
        return self.__width

    #-----------------functions-----------------
    # func: set color of pixel in photo
    def setColor(self, r, g, b, text=' ', position=48):
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
        return '\033[{};2;{};{};{}m'.format(position, r, g, b) + text + '\033[0m'
    # func: Image Processing

    def imageProccing(self):
        """this function read the photo, resize it and convert it to numpy array

        Returns:
            [numpy array]: [numpy array of photo]
        """
        # read photo
        img = Image.open(self.__path)
        # resize photo
        img = img.resize((int(self.__width), int(self.__height)))
        # convert photo to numpy array
        img = asarray(img)
        return img
    # func: create file and write text in it

    def saveFile(self, fileName='file.sh'):
        """this function save the file as .sh file

        Args:
            fileName (str, optional): [file name]. Defaults to 'file.sh'.
        """
        # open file
        file = open(fileName, 'w')
        self.fileName = fileName
        # write to file
        file.write('#!/bin/bash\n')
        file.write('\n')
        # read photo
        img = self.imageProccing()
        # front or background
        if self.__front:
            position = 38
        else:
            position = 48
        # for each pixel in photo
        for i in range(len(img)):
            file.write('echo "')
            for j in range(len(img[i])):
                # set color of pixel
                file.write(self.setColor(
                    img[i][j][0], img[i][j][1], img[i][j][2], self.__text[j % len(self.__text)], position))
            # write to file
            file.write('"\n')
        file.close()
    # func: run file

    def runFile(self):
        """ function to run the project
        """
        #if in system == linux
        if os.name == 'posix':
            #clear screen
            os.system('clear')
            path = os.getcwd() + '/' + self.fileName
            os.system('chmod +x ' + self.fileName)
            os.system(path)
        #if in system == windows
        else:
            os.system('cls')
            with open(self.fileName, 'r') as file:
                os.system(file.read())

#-----------------------------example---------------------------------


def example():
    """this function run the project
    """
    # create object of class
    obj = Photo()
    # set path of photo
    obj.setPath('Example.jpg')
    # set text to be shown
    obj.setText('MohammadrezaAmani')
    # set size of photo
    obj.setSize('100*60')
    # set front or background
    obj.setFront(False)
    # create file and write text in it
    obj.saveFile()
    # run file
    obj.runFile()


example()

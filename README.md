# Terminal_Photo
 
### Description
a class that can be used to show a photo in terminal 

### Usage
1. place the file in the same directory as the python file
2. from termioPhoto import *
3. create an object of the class 
4. set the path of the photo using the setPath() function
5. set the size of the photo using the setSize() function
6. set the text to be displayed using setText() function
7. if you want to color the text set setSize() to True and for Background set it to False
8. you can choose where you want to save the .sh file using saveFile() function (inter the path in the function)
9. use the runFile() function to show the photo in terminal
### Requirements
- [Python](https://www.python.org/)
- [Pillow](https://pillow.readthedocs.io/en/stable/) 
  - `pip install pillow`
- [NumPy](https://numpy.org/)
  - `pip install numpy`
### Example
        from termioPhoto import *
        obj = Photo()
        # set path of photo
        obj.setPath('Example.jpg')
        # set text to be shown
        obj.setText(' ')
        # set size of photo
        obj.setSize('300*100')
        # set front or background
        obj.setFront(False)
        # create file and write text in it
        obj.saveFile()
        # run file
        obj.runFile()
> #### output
![outputImage](https://github.com/MohammadrezaAmani/Terminal_Photo/blob/master/images/output.png)

### functions 
#### 1. setColor()
> ![setColor](https://github.com/MohammadrezaAmani/Terminal_Photo/blob/master/images/setColor.png)
this function get the color of each pixel in photo and set it to the color of the word in text
#### 2. imageProcessing()
> ![imageProcessing](https://github.com/MohammadrezaAmani/Terminal_Photo/blob/master/images/imageProcessing%20.png)
#### 3. saveFile()
> ![saveFile](https://github.com/MohammadrezaAmani/Terminal_Photo/blob/master/images/saveFile%20.png)
#### 4. runFile()
> ![runFile](https://github.com/MohammadrezaAmani/Terminal_Photo/blob/master/images/runFile%20.png)


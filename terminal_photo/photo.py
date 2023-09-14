#  ---------------------------show photo in terminal----------------------------
#  author: Mohammadreza Amani
#  GitHub: https://www.github.com/MohammadrezaAmani
#  Linkedin: https://www.linkedin.com/in/mohammadreza-amani/
#  Date: 2021/11/18

#  ---------------------------------logic----------------------------------------
#    1- read photo
#    2- resize photo
#    3- convert photo to numpy array
#    4- for each pixel in photo use set_color to set color of word in text
#    5- save it as .sh file
#    6- run it

#  -----------------------------import libraries---------------------------------

from PIL import Image

#  --------------------------create class and functions---------------------------


class Photo:
    def __init__(self, path=None, text=None, size=None, front=False, mode="run"):
        """Photo class constructor
        this class get some parameters and set and use them to create a colored text from photo

        Args:
            path (str, optional): [path of image]. Defaults to 'IMG.jpg'.
            text (str, optional): text to be shown in foreground. Defaults to " ".
            size (str, optional): text of image in width*height format, example = 30*50. Defaults to '30*50'.
            front (bool, optional): ro set color in background = False, in foreground = True. Defaults to False.
        """
        self.path = path
        self.text = text
        self.size = size
        self.front = front
        self.mode = mode

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path_value: str):
        if path_value is None:
            self._path = None
            return
        if isinstance(path_value, str):
            self._path = path_value
        else:
            raise BaseException("Path must be `String`.")

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text_value: str):
        if text_value is None:
            self._text = " "
            return
        try:
            self._text = str(text_value)
        except Exception as e:
            raise BaseException("Text must be `String` or `Char`.")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height_value: int):
        if height_value is None:
            self._height = 50
            return
        try:
            self._height = int(height_value)
        except Exception as e:
            raise BaseException("Height must be `Integer`.")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width_value: int):
        if width_value is None:
            self._width = 50
            return
        try:
            self._width = int(width_value)
        except Exception as e:
            raise BaseException("Width must be `Integer`.")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size_value: str):
        if type(size_value) in [tuple, list, set]:
            size_value = "*".join([str(i) for i in size_value])
        if size_value is None:
            self._size = "30*50"
            self.width = 30
            self.height = 50
            return
        try:
            if (
                isinstance(size_value, tuple)
                or isinstance(size_value, set)
                or isinstance(size_value, list)
            ):
                size_value = "*".join(size_value)
            self._size = str(size_value)
            self.width = size_value.split("*")[0]
            self.height = size_value.split("*")[1]
        except Exception as e:
            raise BaseException(
                "Size must be a string in format 'width*height' exapmle: '30*50."
            )

    @property
    def front(self):
        return self._front

    @front.setter
    def front(self, front_value: bool):
        if isinstance(front_value, bool):
            self._front = front_value
        else:
            raise BaseException("Front must be `Boolean`.")

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode_value: str):
        if mode_value.lower() in ["html", "bash", "run"]:
            self._mode = mode_value
        else:
            raise BaseException("Mode must be `html` or `bash` or run.")

    def set_color_cli(self, r, g, b, text=" ", position=48):
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
        return "\033[{};2;{};{};{}m".format(position, r, g, b) + text + "\033[0m"

    def set_color_html(self, r, g, b, text=" ", position=48):
        if position == 38:
            return "<span style='color:rgb({},{},{});background-color:rgb({},{},{})'>{}</span>".format(
                r, g, b, 255 - r, 255 - g, 255 - b, text
            )
        else:
            return "<span style='background-color:rgb({},{},{}); color:rgb({},{},{})'>{}</span>".format(
                r, g, b, 255 - r, 255 - g, 255 - b, text
            )

    def process_image(self):
        """this function read the photo, resize it and convert it to numpy array

        Returns:
            [numpy array]: [numpy array of photo]
        """

        img = Image.open(self.path)

        img = img.resize((int(self.height), int(self.width)))

        return img.getdata()

    def save_bash(self, img, fileName="file.sh"):
        """this function save the file as .sh file

        Args:
            fileName (str, optional): [file name]. Defaults to 'file.sh'.
        """

        file = open(fileName, "w")
        self.fileName = fileName

        file.write("!/bin/bash\n")
        file.write("\n")
        position = 38 if self.front else 48

        for i in range(self.width):
            file.write('echo "')
            for j in range(self.height):
                file.write(
                    self.set_color_cli(
                        img[i * self.height + j][0],
                        img[i * self.height + j][1],
                        img[i * self.height + j][2],
                        self.text[j % len(self.text)],
                        position,
                    )
                )

            file.write('"\n')
        file.close()

    def run(self, img):
        position = 38 if self.front else 48

        for i in range(self.width):
            for j in range(self.height):
                print(
                    self.set_color_cli(
                        img[i * self.height + j][0],
                        img[i * self.height + j][1],
                        img[i * self.height + j][2],
                        self.text[j % len(self.text)],
                        position,
                    ),
                    end="",
                )
            print()

    def save_html(self, img, fileName="file.html"):
        with open(fileName, "w") as file:
            file.write("<html>\n")
            file.write(
                """
                       <head>
                          <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>MohammadrezaAmani</title>
                            <style>
                            pre {
                                font-family: monospace;
                                font-size: 1em;
                                white-space: pre-wrap;
                                white-space: -moz-pre-wrap;
                                white-space: -pre-wrap;
                                white-space: -o-pre-wrap;
                                word-wrap: break-word;
                                line-height: 0.55;
                            }
                            </style>
                            </head>
                            """
            )
            file.write("<body>\n")
            file.write("<pre>\n")
            position = 38 if self.front else 48

            for i in range(self.width):
                for j in range(self.height):
                    file.write(
                        self.set_color_html(
                            img[i * self.height + j][0],
                            img[i * self.height + j][1],
                            img[i * self.height + j][2],
                            self.text[j % len(self.text)],
                            position,
                        )
                    )
                file.write("<br>\n")
            file.write("</pre>\n")
            file.write("</body>\n")
            file.write("</html>\n")

    def start(self, fileName="file.sh"):
        img = self.process_image()
        if self.mode == "bash":
            self.save_bash(img, fileName)
        if self.mode == "run":
            self.run(img)
        if self.mode == "html":
            self.save_html(img, fileName)

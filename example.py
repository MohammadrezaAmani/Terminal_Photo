from terminal_photo.photo import Photo

obj = Photo("./assets/Example.jpg", "Mohammadreza", (50, 180), front=False)

# ? show image in terminal?
obj.start()

# ? how to export html?
obj.mode = "html"
obj.start("index.html")

# ? how to export bash?
obj.mode = "bash"
obj.start("index.sh")

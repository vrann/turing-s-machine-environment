"""
Will test using canvas and Pillow to open a jpg image, and handle mouse click events
"""
from tkinter import *
from PIL import ImageTk, Image

class PhotoCanvas(Frame):

    def __init__(self):

        """Sets up window and widgets"""
        Frame.__init__(self)
        self.master.title("BURG")
        self.grid()

        # opens the photo and convert them to Tkinter-compatible image objects
        self.image1 = Image.open("f1.gif")
        self.photo = ImageTk.PhotoImage(self.image1)

        # returns tuple of width and height of image
        (iWidth, iHeight) = self.image1.size 

        # create a canvas and place in frame
        self.canvas = Canvas(self, width = iWidth, height = iHeight)
        self.canvas.grid(row = 0, column = 0)

        # places image in upper left corner (NW) on the canvas at x=0, y=0
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

def main():
    PhotoCanvas().mainloop

main()

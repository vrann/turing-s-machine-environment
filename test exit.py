#!/usr/bin/python3
# write tkinter as Tkinter to be Python 2.x compatible
from tkinter import *
def hello(event):
    print("Single Click, Button-l") 
def quit(event):                           
    print("Double Click, so let's stop") 
    import sys; sys.exit() 

widget = Button(None, text='Mouse Clicks')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit) 
widget.mainloop()

##from tkinter import *
##class App:
##  def __init__(self, master):
##    frame = Frame(master)
##    frame.pack()
##    self.button = Button(frame, 
##                         text="QUIT", fg="red",
##                         command=quit)
##    self.button.pack(side=LEFT)
##    self.slogan = Button(frame,
##                         text="Hello",
##                         command=self.write_slogan)
##    self.slogan.pack(side=LEFT)
##  def write_slogan(self):
##    print("Tkinter is easy to use!")
##
##root = Tk()
##app = App(root)
##root.mainloop()

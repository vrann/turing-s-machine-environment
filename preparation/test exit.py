
##  Turing Machine Visual - a software developed to simulate Turing machine
##    Copyright (C) 2017 Artemii Yanushevskyi
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU Affero General Public License as
##    published by the Free Software Foundation, either version 3 of the
##    License, or (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU Affero General Public License for more details.
##
##    You should have received a copy of the GNU Affero General Public License
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
##    You can contact me by email: argoniton@gmail.com
##
##  This is BETA 6 of this application.


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


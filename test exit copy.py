#!/usr/bin/python3
# write tkinter as Tkinter to be Python 2.x compatible
from tkinter import *
from tkinter import messagebox

def hello(event):
    print("Single Click, Button-l") 
def close(event):                           
    print("Double Click, so let's stop") 
    w.destroy()
def hide(event):                           
    print("Click, so let's hide it") 
    w.withdraw()
def iiconfy(event):
    print('click, iconfy;')
    w.iconfy()
def d():
    def hello1(event):
        w.deiconify()
    w2 = Tk()
    b = Button(w2, text='Mouse Clicks')
    b.pack()
    b.bind('<Button-1>', hello1)
    b.bind('<Double-1>', close)

w = Tk()

b = Button(w, text='Mouse Clicks')
b.pack()
b.bind('<Button-1>', hello)
b.bind('<Double-1>', close)

h = Button(w, text='Hide')
h.pack()
h.bind('<Button-1>', hide)

i = Button(w, text='Iconfy')
i.pack()
i.bind('<Button-1>', iiconfy)
d()
mainloop()


print('moving on')

answer = input('continue?')
if answer == 'y':
    print('continue!')
    def hello1(event):
        w.deiconify()
    def nein(*args):
        if messagebox.askokcancel('quit', 'wanna quit?'):
            w2.destroy()
    w2 = Tk()
    w2.protocol("WM_DELETE_WINDOW", nein)
    w2.bind('<Escape>', nein)
    b = Button(w2, text='Mouse Clicks')
    b.pack()
    b.bind('<Button-1>', hello1)
    b.bind('<Double-1>', close)
    
    

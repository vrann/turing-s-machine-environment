# MySummer.py
from tkinter import Tk, Button, Label
import threading

def button_press():
    def callback():
        total = 0
        for i in range(100000000):
            total += i
        label.config(text = str(total))
    threading.Thread(target = callback).start()

master = Tk()
label = Label(master)
label.pack()
Button(master, text = "Add it up",command = button_press).pack()

master.mainloop()

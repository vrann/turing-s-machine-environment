
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


# MySummer.py
from tkinter import Tk, Button, Label
import threading

def button_press():
    def callback():
        master2 = Tk()
        label2 = Label(master2)
        label2.pack()
        total = 0
        for i in range(70000000):
            total += i
        label2.config(text = str(2039485766))
    threading.Thread(target = callback).start()

master = Tk()
label = Label(master)
label.pack()
Button(master, text = "Add it up",
    command = button_press).pack()

master.mainloop()


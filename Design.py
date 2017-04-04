
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


# design
import tkinter as tk
from EventHandler import register, InterfaceClick
width = 640
# colors:
specific = '#00BAB9'
primary = '#404099'
# define main window
top = None
class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        global top
        top = self


class StatusBar(tk.Canvas):
    height = 25 # status bar height
    def __init__(self, *args, **kwargs):
        register(self, 'StatusBar')
        tk.Canvas.__init__(self, top, *args, width=640,
                           height=StatusBar.height,
                           bg=specific,
                           highlightthickness=0,bd=0,
                           **kwargs)
        c = self
        indicators = []
        for i in range(3):
            indicators.append(c.create_oval(30+i*25,5,45+i*25,20, fill=primary, outline=primary, width=0))
        c.itemconfig(indicators[1], fill='gray', outline=primary, width=0)


class SetupBar(tk.Canvas):
    height = 200
    def __init__(self, *args, **kwargs):
        register(self, 'SetupBar')
        tk.Canvas.__init__(self, top, *args, width=640,
                           height=SetupBar.height,
                           highlightthickness=0,bd=0,
                           **kwargs)

    def displayInstructions(self):
        c = self
        c.img = tk.PhotoImage(file="CodeCompileValues.gif")
        c.create_image(0,0, anchor='nw', image=self.img)
        def SetupBarClick(event):
            ''' I call this function when I click on SetupBar'''
            InterfaceClick(panel_name='SetupBar',
                           click_coords={'x':event.x,'y':event.y})
        c.bind("<Button-1>", SetupBarClick)

class RunBar(tk.Canvas):
    height = 150
    def __init__(self, *args, **kwargs):
        register(self, 'RunBar')
        tk.Canvas.__init__(self, top, *args, width=640,
                           height=RunBar.height,
                           highlightthickness=0,bd=0,
                           **kwargs)

    def displayInstructions(self):
        c = self
        c.img = tk.PhotoImage(file="RunTheMachine.gif")
        c.create_image(0,0, anchor='nw', image=self.img)
        def RunBarClick(event):
            ''' I call this function when I click on RunBar'''
            InterfaceClick(panel_name='RunBar',
                           click_coords={'x':event.x,'y':event.y})
        c.bind("<Button-1>", RunBarClick)



class TuringMachineFrame(tk.Frame):
    def __init__(self):
        register(self, 'TuringMachineFrame')
        tk.Frame.__init__(self, top)
        from TuringCore import TuringMachine
        self.turingmachine = TuringMachine(self)
        self.turingmachine.pack()
        



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


import tkinter as tk

canvas_width = 420
canvas_height = 210
start = None
value = None
master = tk.Tk()

canvas = tk.Canvas(master, 
           width=canvas_width, 
           height=canvas_height, bd=0, highlightthickness=0)
canvas.pack()

img = tk.PhotoImage(file="inputandcode.gif")
canvas.create_image(0,0, anchor='nw', image=img)

def onclick_handler(event):
    ''' I call this function when I click on canvas'''
    global start
    start = {'x':event.x, 'y':event.y}
    print(start)
    if start['x'] < canvas_width/2:
        print('you are in first case')
        values = getValues()
    else:
        print('you are in second case')

def onrelease_handler(event):
    ''' I call this function when I release click on canvas'''
    global start
    if start is not None:
        x = start['x']
        y = start['y']
        # event.widget.create_rectangle(x, y, event.x, event.y)
        start = None

def getValues():
    global value
    root = tk.Tk()
    S = tk.Scrollbar(root)
    T = tk.Text(root, height=4, width=50)
    S.pack(side='right', fill='y')
    T.pack(side='left', fill='y')
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """HAMLET: To be, or not to be--that is the question:
    Whether 'tis nobler in the mind to suffer
    The slings and arrows of outrageous fortune
    Or to take arms against a sea of troubles
    And by opposing end them. To die, to sleep--
    No more--and by a sleep to say we end
    The heartache, and the thousand natural shocks
    That flesh is heir to. 'Tis a consummation
    Devoutly to be wished."""
    T.insert('end', quote)
    stringvar = tk.StringVar()
    stringvar.set('3 2 1')
    entry = tk.Entry(root, textvariable = stringvar)
    entry.pack()
    
    def submit():
        global value
        value = entry.get()
        print(value)
        print('you can close this window now')
        import sys; sys.exit()
        
    
    button = tk.Button(root, text='submit', command=submit)
    button.pack()
        
    tk.mainloop()

canvas.bind("<Button-1>", onclick_handler)
canvas.bind("<ButtonRelease-1>", onrelease_handler)
tk.mainloop()


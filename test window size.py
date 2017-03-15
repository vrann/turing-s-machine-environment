import tkinter as tk
from tkinter.filedialog import askopenfilename
import application

start = None
value = None
code = None
delete = False
    
canvas_width = 800

master = tk.Tk()
f1 = tk.Frame(master)
canvas1 = tk.Canvas(f1, 
           width=800, 
           height=300, bd=0, highlightthickness=0)
canvas1.pack()
f1.pack()

def getValues():
    global value
    root = tk.Tk()
    frame = tk.Frame(root)
    S = tk.Scrollbar(frame)
    T = tk.Text(frame, height=4, width=50)
    S.pack(side='right', fill='y')
    T.pack(side='left', fill='y')
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """HAMLET: To be, or not to be--that is the question:
    Whet her 'tis nobler in the mind to suffer'
    Write your input values like that:
    9, 4, 6
    -OR-
    9 4 6
    
    Or to take arms against a sea of troubles
    And by opposing end them. To die, to sleep--
    No more--and by a sleep to say we end
    The heartache, and the thousand natural shocks
    That flesh is heir to. 'Tis a consummation
    Devoutly to be wished."""
    T.insert('end', quote)
    frame.pack()

    entry = tk.Entry(root)
    entry.pack()

    def submit():
        global value
        value = entry.get()
        Mframe.mGUI.machine.values = value
        Mframe.mGUI.machine.stripe.createstripe(value)
        print('you can close this window now')
        valuesandcode(root)
        
    button = tk.Button(root, text='submit', command=submit)
    button.pack(fill='both')
        
    tk.mainloop()

def getCode():
    global code
    root = tk.Tk()

    def submit():
        global code
        code = askopenfilename()
        valuesandcode(root)
        Mframe.mGUI.machine.codepath = code
        Mframe.mGUI.machine.open(code)

        
    button = tk.Button(root, text='choose', command=submit)
    button.pack(fill='both')
        
    tk.mainloop()

def valuesandcode(root):
    root.destroy()
    if value and code:
        print(value,code)
        print('we are ready to run turing machine')
    else:
        print('you\'re missing something')

def canvas1click(event):
    ''' I call this function when I click on canvas'''
    global start
    start = {'x':event.x, 'y':event.y}
    if start['x'] < canvas_width/2:
        print('you are in window for typing input values')
        getValues()
    else:
        print('you are in window for selecting program code')
        getCode()

canvas1.bind("<Button-1>", canvas1click)

f2 = tk.Frame(master)
canvas2 = tk.Canvas(f2, 
           width=800, 
           height=100, bd=0, highlightthickness=0)
canvas2.pack()
f2.pack()

def canvas2click(event):
    ''' I call this function when I click on canvas'''
    global start
    start = {'x':event.x, 'y':event.y}
    if canvas_width/3 < start['x'] < 2*canvas_width/3:
        print('machine run')
        Mframe.mGUI.machine.act()

canvas2.bind("<Button-1>", canvas2click)       

img1 = tk.PhotoImage(file="f1.gif")
canvas1.create_image(0,0, anchor='nw', image=img1)
img2 = tk.PhotoImage(file="f2.gif")
canvas2.create_image(0,0, anchor='nw', image=img2)

Mframe = application.MainApplication(master)
Mframe.pack(side="top", fill="both", expand=True)

tk.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
canvas_width = 420
canvas_height = 210
start = None
value = None
code = None
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
        getValues()
    else:
        getCode()
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
        print(value)
        print('you can close this window now')
        import sys; sys.exit()
        
    button = tk.Button(root, text='submit', command=submit)
    button.pack(fill='both')
        
    tk.mainloop()

def getCode():
    global code
    root = tk.Tk()

    def submit():
        global code
        code = askopenfilename()
        print(code)
        print('you can close this window now')
        import sys; sys.exit()
        valuesandcode()
        
    button = tk.Button(root, text='choose', command=submit)
    button.pack(fill='both')
        
    tk.mainloop()

def valuesandcode():
    print(values,code)

canvas.bind("<Button-1>", onclick_handler)
canvas.bind("<ButtonRelease-1>", onrelease_handler)
tk.mainloop()

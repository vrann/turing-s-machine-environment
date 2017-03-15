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

image = tk.PhotoImage(file="inputandcode.jpg")
canvas.create_image(0, 0, anchor=NW, image=image, tags="bg_img")


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

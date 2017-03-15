import tkinter as tk
from tkinter.filedialog import askopenfilename
import application
canvas_width = 420
canvas_height = 210
while True:
    start = None
    value = None
    code = None
    delete = False

    def onclick_handler(event):
        ''' I call this function when I click on canvas'''
        global start
        start = {'x':event.x, 'y':event.y}
        if start['x'] < canvas_width/2:
            print('you are in window for typing input values')
            getValues()
        else:
            print('you are in window for selecting program code')
            getCode()

    def deletemaster(*args):
        global delete
        delete = True
        # the following command will destroy the window,
        master.destroy()
        # next command is located right below tk.mainloop()

    master = tk.Tk()
    master.protocol("WM_DELETE_WINDOW", deletemaster)
    canvas = tk.Canvas(master, 
               width=canvas_width, 
               height=canvas_height, bd=0, highlightthickness=0)
    canvas.pack()
    img = tk.PhotoImage(file="inputandcode.gif")

    canvas.create_image(0,0, anchor='nw', image=img)
    canvas.bind("<Button-1>", onclick_handler)

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
            
        button = tk.Button(root, text='choose', command=submit)
        button.pack(fill='both')
            
        tk.mainloop()

    def valuesandcode(root):
        root.destroy()
        if value and code:
            print(value,code)
            print('we are ready to run turing machine')
            master.destroy()
        else:
            print('you\'re missing something')


    tk.mainloop()
    if delete == True:
        break
    print('GOOD TO GO!!')
    
    root = tk.Tk(screenName='The Turing\'s machine',baseName='Machine', className=' Visual Turing',) #main window
    frame = application.MainApplication(root)
    frame.pack(side="top", fill="both", expand=True)

print('program has stopped working')

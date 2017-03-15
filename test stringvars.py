import tkinter as tk

m = tk.Tk()
sv = tk.StringVar()
sv.set('jhgf')
f = tk.Entry(m, textvariable=sv)
f.pack()

def d():
    m = tk.Tk()
    sv = tk.StringVar()
    sv.set('jhgf')
    f = tk.Entry(m, textvariable=sv)
    f.pack()
    tk.mainloop()
d()
tk.mainloop()

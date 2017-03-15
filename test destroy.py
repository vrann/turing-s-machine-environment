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

    def close():
        m.destroy()
        print('    window is closed')

    def hide():
        m.withdraw()
        print('    window is hidden')

    bclose = tk.Button(m)
    bclose['command'] = close
    bclose['text'] = 'close'
    bclose.pack()

    bhide = tk.Button(m)
    bhide['command'] = hide
    bhide['text'] = 'hide'
    bhide.pack()

    tk.mainloop()

    
d()
print('program is done') # you will see that if all windows are destroyed

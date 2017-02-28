import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.test = tk.Label(self, text='tesst')
        self.test.pack()

if __name__ == "__main__":
    root = tk.Tk(screenName='The Turing\'s machine',baseName='Machine', className=' Visual Turing',)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

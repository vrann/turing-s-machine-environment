
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

class AskCodeWindow(tk.Tk):
    def __init__(self, *args, send=None, statusbar=None, machine=None, **kwargs):
        tk.Tk.__init__(self, *args,
                       className=' Imput Code', **kwargs)
        statusbar.changeStatus(1, 'not ready')
        tk.Label(self, text='InputV window').pack()
        tk.Label(self, text=send.path+' - is code path').pack()
        
        entry = tk.Entry(self)
        entry.pack()
        entry.insert(0, '/Users/argoniton/Desktop/addtiton of 2 numbers.turing')
        
        self.code = send
        
        def submit():
            self.code.path = entry.get()
            statusbar.changeStatus(1, 'ready')
            machine.codepath = self.code.path
            print('you can close this window now')
            self.destroy()

        button = tk.Button(self, text='submit', command=submit)
        button.pack(fill='both')

def askCode(code, objects):
    '''procedure'''
    statusbar = objects['StatusBar']
    machine = objects['TuringMachineFrame'].turingmachine.machine
    a = AskCodeWindow(send=code, statusbar=statusbar, machine=machine)
    tk.mainloop()
    

if __name__=='__main__':
    class Code:
        def __init__(self, path):
            self.path = path

    
    code = Code('some/path')
    askCode(code)
            



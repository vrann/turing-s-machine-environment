
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

class AskValuesWindow(tk.Tk):
    def __init__(self, *args, send=None, statusbar=None, machine=None, **kwargs):
        tk.Tk.__init__(self, *args,
                       className=' Imput Values', **kwargs)
        statusbar.changeStatus(3, 'not ready')
        tk.Label(self, text='InputV window').pack()
        values = send.v
        tk.Label(self, text=values + ' are values').pack()
        send.v = '42'
        
        entry = tk.Entry(self, text='1 2')
        entry.pack()
        entry.insert(0, '1 2')
        
        self.values = send
        
        def submit():
            # turn on first indicator
            self.values.v = entry.get()
            statusbar.changeStatus(3, 'ready')
            print(self.values.v, machine)
            machine.values = self.values.v
            print('you can close this window now')
            self.destroy()

        button = tk.Button(self, text='submit', command=submit)
        button.pack(fill='both')

def askValues(values, objects):
    '''procedure'''
    statusbar = objects['StatusBar']
    machine = objects['TuringMachineFrame'].turingmachine.machine
    a = AskValuesWindow(send=values, statusbar=statusbar, machine=machine)
    tk.mainloop()

if __name__=='__main__':
    class Values:
        def __init__(self, v):
            self.v = v

    
    values = Values('1 3 1')
    askValues(values)
            



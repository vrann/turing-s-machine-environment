# clear and consice
# imorting modules
import tkinter as tk
import inspect
from tkinter.filedialog import askopenfilename
# design
font_family = 'Lucida Grande' # app typeface
font_family = 'Menlo'
# define some colors
gray = '#97ACB3'
lightgray = '#f6f6f6'
canvas_size = 400 # size of canvas area


class Menue:
    ''' create menu'''
    def __init__(self, parent):
        menu = tk.Menu(parent)
        parent.config(menu=menu)
        # buttons in menue call those functions 
        def NewFile():
            print("New File!")
        def OpenFile():
            name = askopenfilename()
            print(name)
            return name
        def About():
            print("This is a simple example of a menu")
        filemenu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=NewFile)
        filemenu.add_command(label="Open...", command=OpenFile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)

        helpmenu = tk.Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=About)
        
class Navbar(tk.Frame):
    pass
class Toolbar(tk.Frame):
    pass
class Statusbar(tk.Frame):
    pass
class Main(tk.Frame):
    pass

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        # making menu
        self.parent = parent
        self.menu = Menue(parent)
##        self.toolbar = Toolbar(self, ...)
##        self.navbar = Navbar(self, ...)
##        self.main = Main(self, ...)
##
##        self.statusbar.pack(side="bottom", fill="x")
##        self.toolbar.pack(side="top", fill="x")
##        self.navbar.pack(side="left", fill="y")
##        self.main.pack(side="right", fill="both", expand=True)
        # main part
        self.test = tk.Label(self, text='BETA 3.0')
        self.test.pack()
        self.mGUI = MachineGUI(self) # create a MachineGUI instance -> creating window and UI
        b = tk.Button(self, text='Act!',
                      command=self.create_and_act,
                      font=(font_family, 12, 'normal'))
        b.pack(side='right')
        # check **kwargs, whether or not it has input values and code
        self.values = None
        self.codepath = None
        if 'code' in kwargs.keys():
            self.codepath = kwargs['code']
            self.mGUI.machine.codepath = kwargs['code']
        if 'values' in kwargs.keys():
            self.values = kwargs['values']
            self.mGUI.machine.values = kwargs['values']
        
    def create_and_act(self):
        # provide input values
        if not self.mGUI.machine.running.get():
            self.mGUI.machine.stripe.createstripe(self.values) # fill the stripe with numbers in array
            # open and compile code
            if not self.codepath:
                appname = askopenfilename()
                self.mGUI.machine.open(appname)
            else:
                if not self.compile:
                    self.mGUI.machine.open(self.codepath)                   
            # run machine
            self.mGUI.machine.act()

class MachineGUI:
    def __init__(self, root):
        # create canvas
        self.root = root
        self.machine = Machine(self.root, 'white', width=800, height=210, bg='darkgreen', bd=0, highlightthickness=0)
        self.machine.pack()
        # make buttons and labels
        self._make_interface()

    def _make_interface(self):
        ''' creates labels, buttons etc'''
        label = tk.Label(self.root, text = 'Turing\'s Machine', font=(font_family, 20, 'normal'))
        label.pack()
        label = tk.Label(self.root, text = 'Industrial version', font=(font_family, 12, 'bold'))
        label.pack()
        leftButton = tk.Button(self.root, text='Turn Left',
                      command=self.machine.stripe.L,
                      font=(font_family, 12, 'normal'))
        leftButton.pack(side='left')
        rightButton = tk.Button(self.root, text='Turn Right',
                      command=self.machine.stripe.R,
                      font=(font_family, 12, 'normal'))
        rightButton.pack(side='right')
        # set button-1 (mouse) to call functions
        self.machine.bind("<Button-1>", onclick_handler)
        self.machine.bind("<ButtonRelease-1>", onrelease_handler)


class Machine(tk.Canvas):
    def __init__(self, top, linecolor, *args, **kwargs):
        tk.Canvas.__init__(self, top, *args, **kwargs)
        self.stripe = Stripe(self, linecolor) # making a stripe
        # make a smart variable moved and acting
        self.moved = tk.IntVar()
        self.moved.set(1) # set it equal to 1, '1' means that nothing is moving
        self.running = tk.IntVar()
        self.running.set(0) # program doesn't run if it's '1' 
        self.codepath = None # stores code path
        self.code = None # stores code
        self.compiled = None # stores compiled code
        self.state = 'q1' # machine.state at the beginning
        # display self.state under stripe
        self.stateT = self.create_text(400, 164, text=self.state,
                                       font=(font_family, 30), tag='machineState',
                                       fill=gray,
                                       activefill=lightgray)

    def open(self, source):
        '''open and compile code'''
        file = open(source, 'r') # open code
        # convert turing app code to dictionary (compile)
        # using regular expression
        LINE = r"^[\s]*[.^\(]*\([\s]*([^\,\s]+)\,[\s]*(\d)[\s]*\)[\s]*->[\s]*\([\s]*([^\,\s]*)[\s]*\,[\s]*(\d)[\s]*,[\s]*([LRSlrs])[\s]*\).*$"
        self.compiled = {} # the dictionary
        import re
        # get values from each line matching the pattern
        for i, line in enumerate(file, 1):
            # check whether or  not the line matches pattern
            match = re.match(LINE, line)
            if match: # if yes, parse values into variables
                qInitial = match.group(1)
                vInitial = int(match.group(2))
                qResult = match.group(3)
                vResult = int(match.group(4))
                action = match.group(5)
                #print(qInitial, vInitial,'->',qResult, vResult, action)
                # add keyword and corresponding values into dictionary
                self.compiled[(qInitial, vInitial)] = (qResult, vResult, action)
        # save code in a variable
        self.code = file.read()
        #print(self.compiled)
        file.close()

    def track(self):
        '''get current value and state'''
        print(self.get, self.state)

    def action(self):
        '''make a single move'''
        work = True
        # 210, 170
        # obtain new values
        action = self.compiled[(self.state, self.stripe.current.value)]
        # 'unpack action'
        self.state = action[0]
        value = action[1]
        move = action[2]        
        self.itemconfig(self.stateT, text=self.state) # display new state
        self.stripe.valueChange(value) # change a value of current place
        # what to do next:
        if move == 'L' or move == 'l':
            self.stripe.L()
        elif move == 'R' or move == 'r':
            self.stripe.R()
        elif move == 'S' or move == 's':
            self.stripe.S()
            print('machine has stopped')
            work = False
        else:
            print('error executing', move)
            work = False
        return work
        
    def act(self):
        '''act untill stop'''
        work = True
        self.running.set(1)
        while work:
            work = self.action()
        self.running.set(0)
        print('Done')


class Stripe:
    def __init__(self, machine, *args, display=5, **kwargs):
        linecolor = args[0]
        self.machine = machine
        self.display = display
        self.machine.create_line(20, 20, 780, 20, fill=linecolor)
        self.machine.create_line(20, 190, 780, 190, fill=linecolor)
        self.current = None
        self.animate = True

    def valueChange(self, value):
        self.current.value = value
        rect_id = self.current.visual[0]
        text_id = self.current.visual[1]
        self.machine.itemconfig(text_id, text=str(value))
        self.machine.itemconfig(rect_id, fill='gray')

    def createPlaceHere(self, left, right, value):
        def makePlaceAtCenter():
            print('making rectangle here')
            returnPlace1 = self.machine.create_rectangle(175,70,245,140, fill='cyan', tag='place'),                    
            returnPlace2 = self.machine.create_text(210, 105, text=str(value), font=(font_family, 34), tag='place')
            return returnPlace1, returnPlace2
        
        if left == right == None:
            place = Place(self, value, None, None, 'first')
        elif right != None:
            place = Place(self, value, None, right)
            right.left = place
        elif left != None:
            place = Place(self, value, left, None)
            left.right = place
        self.current = place
        place.visual = makePlaceAtCenter()
        print('place has been made', place.value, place.left, place.right)
        return place

    def createNewPlaceR(self, value, left):
        def makePlaceAtCenter():
            print('making rectangle l')
            returnPlace1 = self.machine.create_rectangle(175,70,245,140, fill='cyan', tag='place'),                    
            returnPlace2 = self.machine.create_text(210, 105, text=str(value), font=(font_family, 34), tag='place')
            return returnPlace1, returnPlace2
        
        place = Place(self, value, left, None)
        if left == None:
            place.visual = makePlaceAtCenter()
        else:
            left.right = place
            place.visual = makePlaceAtCenter()
        self.current = place
        #print('place has been made',place.value, place.left, place.right)
        return place

    def createNewPlaceL(self, value, right):
        def makePlaceAtCenter():
            print('making rectangle l')
            returnPlace1 = self.machine.create_rectangle(175,70,245,140, fill='cyan', tag='place'),                    
            returnPlace2 = self.machine.create_text(210, 105, text=str(value), font=(font_family, 34), tag='place')
            return returnPlace1, returnPlace2
        
        place = Place(self, value, None, right)
        if right == None:
            place.visual = makePlaceAtCenter()
        else:
            right.left = place
            place.visual = makePlaceAtCenter()
        self.current = place
        print('place has been made',place.value, place.left, place.right)
        return place

    def createFirstPlace(self, value):
        place = Place(self, value, None, None)
        print('created first place        current = self.createFirstPlace(1)')

        return place

    def moveL(self):
        self.moveCarefuly('place', 100, 0)
        self.current = self.current.left

    def moveR(self):
        self.moveCarefuly('place', -100, 0)
        self.current = self.current.right

    def L(self):
        if self.machine.moved.get() == 1:
            memo = self.current
            self.moveL()
            if self.current == None:
                newplace = self.createNewPlaceL(0, memo)
                self.current = newplace
        else:
            print('hold your HORSES right there for a second')

    def R(self):
        if self.machine.moved.get() == 1:
            memo = self.current
            self.moveR()
            if self.current == None:
                newplace = self.createNewPlaceR(0, memo)
                self.current = newplace
        else:
            print('hold your HORSES right there for a second')

    def S(self):
        print('Machine encountered S')

    def createstripe(self, inputNumbers):
        ''' Input might look like this: [63, 86, 12]'''
        print(inputNumbers)
        inputNumbers = [int(a) for a in inputNumbers.split()]
        print(inputNumbers)
        self.machine.running.set(1)
        current = self.createPlaceHere(None, None, 0)
        left = current
        for n in inputNumbers:
            for i in range(n+1):
                self.moveR()
                newPlace = self.createPlaceHere(left, None, 1)
                left = newPlace
            #making 0
            self.moveR()
            emptyPlace = self.createPlaceHere(left, None, 0)
            left = emptyPlace
        self.current = emptyPlace
        for i in range(sum(inputNumbers)+2*len(inputNumbers)-1):
            self.L()
        self.machine.running.set(0)

    def moveCarefuly(self, thing, dx, dy):
        coordsX, coordsY, m1, m2 = self.machine.coords(thing)
        if (dx != 0 or dy != 0): # є що і куди переміщувати
            if self.animate: # якщо пересувати повільно
                # встановити зсув на 1 крок рівним 1, 0 або -1
                # у залежності від dx, dy
                ddx = _sign(dx)
                ddy = _sign(dy)
                # обчислити фінальні координати
                xfinal = coordsX + dx
                yfinal = coordsY + dy
                # запустити анімацію пересування
                self.machine.moved.set(0)
                self._movestep(thing, ddx, ddy, xfinal, yfinal)
                # очікувати зміни значення self.moved
                self.machine.wait_variable(self.machine.moved)
            else:
                # пересунути одразу на dx, dy
                self.machine.move(thing, dx, dy)

    def _movestep(self, thing, ddx, ddy, xfinal, yfinal):
        '''Зробити 1 крок для "повільного" пересування об'єкту.

           id - номер об'єкту,
           ddx, ddy - кроки по x, y,
           xfinal, yfinal - кінцеві координати лівого верхнього кута
        '''
        x, y, mx, my = self.machine.coords(thing) # отримати поточні координати
        # обчислити нові значення ddx, ddy
        if x == xfinal:
            ddx = 0
        if y == yfinal:
            ddy = 0
        if ddx or ddy: # якщо не дійшли до кінця
            self.machine.move(thing, ddx, ddy) # перемістити об'єкт
            # встановити виклик переміщення на наступний крок
            # через 5 мілісекунд
            self.machine.after(1, self._movestep, thing, ddx, ddy, xfinal, yfinal)
        else:
            # змінити self.moved, щоб зафіксувати завершення переміщення
            self.machine.moved.set(1)


class Place:
    def __init__(self, stripe, value, left, right, *args):
        self.stripe = stripe
        self.value = value
        self.left = left
        self.right = right
        self.visual = None
        if args:
            self.note = args[0]
            print(args)
        
    def __str__(self):
        return str(self.value)

def _sign(val):
    '''signum(val)'''
    if val > 0:
        sign = 1
    elif val == 0:
        sign = 0
    else:
        sign = -1
    return sign

start = None # I use it to store coords from click_handler

def onclick_handler(event):
    ''' I call this function when I click on canvas'''
    global start
    start = (event.x, event.y)
    print(start)

def onrelease_handler(event):
    ''' I call this function when I release click on canvas'''
    global start
    if start is not None:
        x = start[0]
        y = start[1]
        event.widget.create_rectangle(x, y, event.x, event.y)
        start = None

print('you are working with', __name__)
if __name__ == "__main__":
    root = tk.Tk(screenName='The Turing\'s machine',baseName='Machine', className=' Visual Turing',) #main window
    frame = MainApplication(root)
    frame.pack(side="top", fill="both", expand=True)
    root.mainloop()

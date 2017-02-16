from tkinter import *
import inspect
font_family = 'Lucida Grande'
font_family = 'Menlo'
canvas_size = 400

def _sign(val):
    "signum(val)"
    if val > 0:
        sign = 1
    elif val == 0:
        sign = 0
    else:
        sign = -1
    return sign

class MachineGUI:
    def __init__(self):
        self.top = Tk()
        self.app = 'preparation/app.turing'
        self.machine = Machine(self.top, 'white', number=60, width=420, height=210, bg='darkgreen', bd=0, highlightthickness=0)
        self.machine.pack()
        self._make_controls()

    def _make_controls(self):
        label = Label(self.top, text = 'Turing\'s Machine', font=(font_family, 20, 'normal'))
        label.pack()
        label = Label(self.top, text = 'Industrial version', font=(font_family, 12, 'bold'))
        label.pack()
        leftButton = Button(self.top, text='Turn Left',
                      command=self.machine.strip.L,
                      font=(font_family, 12, 'normal'))
        leftButton.pack(side='left')
        rightButton = Button(self.top, text='Turn Right',
                      command=self.machine.strip.R,
                      font=(font_family, 12, 'normal'))
        rightButton.pack(side='right')


class Machine(Canvas):
    def __init__(self, top, linecolor, *args, number=42, **kwargs):
        Canvas.__init__(self, top, *args, **kwargs)
        self.linecolor = linecolor
        self.number = 42
        self.strip = Strip(self, linecolor)
        self.moved = IntVar()
        self.moved.set(1)
        self.compiled = None
        self.code = None
        self.state = 'q1'

    def open(self, source):
        file = open(source, 'r')
        LINE = r"^[\s]*[.^\(]*\([\s]*([^\,\s]+)\,[\s]*(\d)[\s]*\)[\s]*->[\s]*\([\s]*([^\,\s]*)[\s]*\,[\s]*(\d)[\s]*,[\s]*([LRSlrs])[\s]*\).*$"
        self.compiled = {}
        import re
        for i, line in enumerate(file, 1):
            match = re.match(LINE, line)
            if match:
                qInitial = match.group(1)
                vInitial = int(match.group(2))
                qResult = match.group(3)
                vResult = int(match.group(4))
                action = match.group(5)
                #print(qInitial, vInitial,'->',qResult, vResult, action)
                self.compiled[(qInitial, vInitial)] = (qResult, vResult, action)
        self.code = file.read()
        #print(self.compiled)
        file.close()

    def track(self):
        print(self.get, self.state)

    def action(self):
        work = True
        action = self.compiled[(self.state, self.strip.current.value)]
        self.state = action[0]
        value = action[1]
        self.strip.valueChange(value)
        move = action[2]
        if move == 'L' or move == 'l':
            self.strip.L()
        elif move == 'R' or move == 'r':
            self.strip.R()
        elif move == 'S' or move == 's':
            self.strip.S()
            print('machine has stopped')
            work = False
        else:
            print('error executing', move)
            work = False
        return work
        
    def act(self):
        work = True
        while work:
            work = self.action()
        print('Done')


class Strip:
    def __init__(self, machine, *args, display=5, **kwargs):
        linecolor = args[0]
        self.machine = machine
        self.display = display
        self.machine.create_line(20, 20, 400, 20, fill=linecolor)
        self.machine.create_line(20, 190, 400, 190, fill=linecolor)
        self.current = None
        self.animate = True

    def valueChange(self, value):
        self.current.value = value
        rect_id = self.current.visual[0]
        text_id = self.current.visual[1]
        self.machine.itemconfig(text_id, text=str(value))
        self.machine.itemconfig(rect_id, fill='gray')

    def createNewPlaceR(self, value, left):
        def makePlaceAtCenter():
            return (self.machine.create_rectangle(175,70,245,140, fill='cyan', tag='place'),                    
                    self.machine.create_text(210, 105, text=str(value), font=(font_family, 34), tag='place'))

        place = Place(self, value, left, None)
        if left == None:
            place.visual = makePlaceAtCenter()
        elif left == self.current:
            self.current.right = place
            self.moveR()
            place.visual = makePlaceAtCenter()
        self.current = place
        #print('place has been made',place.value, place.left, place.right)
        return place

    def createNewPlaceL(self, value, right):
        def makePlaceAtCenter():
            return (self.machine.create_rectangle(175,70,245,140, fill='cyan', tag='place'),                    
                    self.machine.create_text(210, 105, text=str(value), font=(font_family, 34), tag='place'))

        place = Place(self, value, None, right)
        if right == None:
            place.visual = makePlaceAtCenter()
        elif right == self.current:
            self.current.left = place
            self.moveL()
            place.visual = makePlaceAtCenter()
        self.current = place
        print('place has been made',place.value, place.left, place.right)
        return place

    def moveL(self):
        self.moveCarefuly('place', 100, 0)
        self.current = self.current.left

    def moveR(self):
        self.moveCarefuly('place', -100, 0)
        self.current = self.current.right

    def L(self):
        memo = self.current
        self.moveL()
        if self.current == None:
            newplace = self.createNewPlaceL(0, memo)
            self.current = newplace

    def R(self):
        memo = self.current
        self.moveR()
        if self.current == None:
            newplace = self.createNewPlaceR(0, memo)
            self.current = newplace

    def S(self):
        print('Machine encountered S')

    def createStrip(self, inputNumbers):
        ''' Input might look like this: [63, 86, 12]'''
        current = self.createNewPlaceR(1, None)
        left = current
        for n in inputNumbers:
            for i in range(n+1):
                newPlace = self.createNewPlaceR(1, left)
                left = newPlace
            #making 0
            emptyPlace = self.createNewPlaceR(0, left)
            left = emptyPlace

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
    def __init__(self, strip, value, left, right):
        self.strip = strip
        self.value = value
        self.left = left
        self.right = right
        self.visual = None
        
    def __str__(self):
        return str(self.value)


m = MachineGUI()
m.machine.strip.createStrip([3, 4, 2])
m.machine.open('app.turing')
    # print('\n\n')
    # print(machine.code)
for i in range(12):
    m.machine.strip.L()
m.machine.act()

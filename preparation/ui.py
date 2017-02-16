from tkinter import *
import inspect
font_family = 'Lucida Grande'
window_size = 400

def _sign(val):
    "signum(val)"
    if val > 0:
        sign = 1
    elif val == 0:
        sign = 0
    else:
        sign = -1
    return sign

class GridCanvas(Canvas):
    def __init__(self, master, rows, cols, selection_handler, *args,
                 bordercolor='black', evenbg='', ratio = 0.85,
                 highlightbg='grey', **kwargs):
        Canvas.__init__(self, master, *args, **kwargs)
        self.rows = rows
        self.cols = cols
        self.selection_handler = selection_handler
        self.bordercolor = bordercolor
        self.evenbg = evenbg
        self.highlightbg = highlightbg
        self.ratio = ratio
        # width and height of one 
        self.cellwidth = int(self['width'])//self.cols
        self.cellheight = int(self['height'])//self.rows
        # заповнити матрицю зв'язаних об'єктів значенням None
        self.grid = []
        for row in range(rows):
            self.grid.append([])
            for col in range(cols):
                self.grid[row].append(None)
        # зобразити поле
        self._drawgrid()
        # прив'язати подію натиснення лівої клавіші миші над клітинкою поля
        # self.bind('<Button-1>', self.on_click)
        self.moved = IntVar()
        self.moved.set(1)
        self.animate = False

    def animate_toggle(self):
        self.animate = not self.animate

    def moveCarefuly(self, thing, dx, dy):
        coordsX, coordsY, m1, m2 = self.coords(thing)
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
                self.moved.set(0)
                self._movestep(thing, ddx, ddy, xfinal, yfinal)
                # очікувати зміни значення self.moved
                self.wait_variable(self.moved)
            else:
                # пересунути одразу на dx, dy
                self.move(thing, dx, dy)

    def _movestep(self, thing, ddx, ddy, xfinal, yfinal):
        '''Зробити 1 крок для "повільного" пересування об'єкту.

           id - номер об'єкту,
           ddx, ddy - кроки по x, y,
           xfinal, yfinal - кінцеві координати лівого верхнього кута
        '''
        print('inside movestep')
        x, y, mx, my = self.coords(thing) # отримати поточні координати
        # обчислити нові значення ddx, ddy
        if x == xfinal:
            ddx = 0
        if y == yfinal:
            ddy = 0
        if ddx or ddy: # якщо не дійшли до кінця
            self.move(thing, ddx, ddy) # перемістити об'єкт
            # встановити виклик переміщення на наступний крок
            # через 5 мілісекунд
            self.after(5, self._movestep, thing, ddx, ddy, xfinal, yfinal)
        else:
            # змінити self.moved, щоб зафіксувати завершення переміщення
            self.moved.set(1)
    
    def _tagstr(self, row, col):
        '''Побудувати рядок з тегом для клітинки (row, col).
           Наприклад: 't001002'
        '''
        return 't{:0>3}{:0>3}'.format(row, col)

    def left(self):
        self.moveCarefuly('places', -10, 20)
        
    def right(self):
        self.moveCarefuly('places', 10, -20)

    def _drawgrid(self):
        '''Зобразити поле з прямокутників.
        '''
        for row in range(self.rows):
            for col in range(self.cols):
                # визначити границі прямокутника
                # для клітинки (row, col)
                xstart = col * self.cellwidth
                ystart = row * self.cellheight
                xend = xstart + self.cellwidth + 1
                yend = ystart + self.cellheight + 1
                # визначити колір заповнення
                if self.evenbg and (row + col) % 2 == 0:
                    bg = self.evenbg
                else:
                    bg = self['bg']
                # зобразити прямокутник та встановити його тег
                self.create_rectangle(xstart, ystart, xend, yend,
                                      width = self['bd'], fill = bg,
                                      outline = self.bordercolor,
                                      tags=self._tagstr(row, col))

top = Tk()
c = GridCanvas(top, 8, 8, 'handler', bordercolor = 'grey',
                evenbg = 'white',
                width=window_size, height=window_size, bg='red', bd=0, highlightthickness=0)
c.pack()

label = Label(top, text = 'Turing\'s Machine', font=(font_family, 20, 'normal'))
label.pack()
label = Label(top, text = 'Industrial version', font=(font_family, 12, 'bold'))
label.pack()
leftButton = Button(top, text='Turn Left',
              command=c.left,
              font=(font_family, 12, 'normal'))
leftButton.pack(side='left')
rightButton = Button(top, text='Turn Right',
              command=c.right,
              font=(font_family, 12, 'normal'))
rightButton.pack(side='right')
def clean():
     c.delete('all')
runButton = Button(top, text = 'Make up the shit', command=top.quit, bg = 'red', relief = 'flat')
runButton.pack(fill = 'both')

r = c.create_rectangle(10,10,100,100, fill='cyan', tag='places')
r = c.create_rectangle(110,110,200,200, fill='green', tag='places')
r = c.create_rectangle(210,210,300,300, fill='cyan', tag='places')

def proceed(event):
    c.move(r, 5, -20)
    
def color(event):
     c.itemconfig('group1',fill="darkgreen",width=3)
     
# c.after(100, c.move, r, 10, 20)

c.bind('<Button-1>',proceed)
c.bind('<Button-2>',color)


oval = c.create_oval(30,10,130,80,tag="group1")
c.create_line(10,100,450,100,tag="group1")
def killwaste(event):
    print(event)
    c.delete('group1')
c.tag_bind(oval,'<Button-1>', killwaste)

animate = Button(top, text = 'Animate', command=c.animate_toggle)
animate.pack(fill='both')

c.moveCarefuly('group1', 20, 20)
c.animate = True
c.moveCarefuly('group1', -20, -20)

mainloop()

class Machine:
    def __init__(self, strip):
        self.strip = strip
        self.place = self.strip.current
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
                print(qInitial, vInitial,'->',qResult, vResult, action)
                self.compiled[(qInitial, vInitial)] = (qResult, vResult, action)
        self.code = file.read()
        print(self.compiled)
        file.close()

    def track(self):
        print(self.get, self.state)

    def action(self):
        work = True
        action = self.compiled[(self.state, self.place.value)]
        self.state = action[0]
        value = action[1]
        self.strip.current.value = value
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
        self.place = self.strip.current
        return work
        
    def act(self):
        work = True
        while work:
            work = self.action()
        print('Done')


class Place:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        
    def updateR(self):
        newPlace = Place(0, self, None)
        self.right = newPlace
        
    def updateL(self):
        newPlace = Place(0, None, self)
        self.left = newPlace
        
    def __str__(self):
        return str(self.value)


class Strip:
    def __init__(self, inputNumbers):
        if type(inputNumbers) == type([1,2,3]):
            self.createStrip(inputNumbers)
        elif type(inputNumbers) == type(Place(0, None, None)):
            self.current = inputNumbers
            
    def __str__(self):
        return self.current.__str__()
    
    def R(self):
        if self.current.right:   
            self.current = self.current.right
        else:
            self.current.updateR()
            self.current = self.current.right
        return self.current
    
    def L(self):
        if self.current.left:   
            self.current = self.current.left
        else:
            self.current.updateL()
            self.current = self.current.left
        return self.current

    def S(self):
        print(self)
    
    def createStrip(self, inputNumbers):
        ''' Input might look like this: [63, 86, 12]'''
        current = Place(0, None, None)
        left = current
        for n in inputNumbers:
            for i in range(n+1):
                newPlace = Place(1, left, None)
                left.right = newPlace
                left = newPlace
            #making 0
            emptyPlace = Place(0, left, None)
            left.right = emptyPlace
            left = emptyPlace
        self.current = current.right
        
    def __str__(self):
        returnString = ''
        watch = self.current
        while(watch != None):
            returnString += str(watch)
            watch = watch.right
        return returnString

    
def test2():
    strip = Strip([3, 4, 2])
    print(strip)
    machine = Machine(strip)
    machine.open('app.turing')
    # print('\n\n')
    # print(machine.code)
    machine.act()

test2()

def test1():
    p = Place(1, None, None)
    strip = Strip(p)
    print(strip)
    strip.L()
    print(strip)
    strip.L()
    print(strip)
    strip.L()
    print(strip)

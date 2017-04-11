
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


class Event:
    def __init__(self, *args, **kwargs):
        print('created new event')
        print('args:', args)
        print('kwargs:', kwargs)
        if 'click_coords' in kwargs.keys():
            self.click_coords = kwargs['click_coords']
        else:
            click_coords = None
        
    def __str__(self):
        ''' print(<obj>)==<obj>.__str__()'''
        return 'it is an event'

class InterfaceClick(Event):
    def __init__(self, panel_name=None, click_coords=None):
        kwargs = {'panel_name':panel_name, 'click_coords':click_coords}
        Event.__init__(self, **kwargs)

        from Design import width
        if panel_name == 'StatusBar':
            print(panel_name)
            print(objects)
        elif panel_name == 'SetupBar':
            if self.click_coords['x']>=width/2:
                print(click_coords)
                
                from InputValues import askValues
                class Values:
                    def __init__(self, v):
                        self.v = v
                    def __repr__(self):
                        return self.v

                values = Values('2 3 1')
                register(values, 'InputValues')
                window = askValues(values, objects)
                objects['TuringMachineFrame'].turingmachine.machine.values(values.v)
            elif width/3<=self.click_coords['x']<width/2:
                objects['StatusBar'].changeStatus(2, 'not ready')
                print('Compiling ...')
                objects['TuringMachineFrame'].turingmachine.machine.open(objects['InputCode'].path)
                print('Compiled!')
                objects['StatusBar'].changeStatus(2, 'ready')

            elif self.click_coords['x']<width/3:
                print(click_coords)
                
                from InputCode import askCode
                class Code:
                    def __init__(self, path):
                        self.path = path
                    def __repr__(self):
                        return self.path

                code = Code('1 3 1')
                register(code, 'InputCode')
                window = askCode(code, objects)
                objects['TuringMachineFrame'].turingmachine.machine.codepath(code.path)
        elif panel_name == 'RunBar':
            objects['TuringMachineFrame'].turingmachine.machine.create_and_act()
        elif panel_name == 'TuringMachineFrame':
            if click_coords == '':
                print(click_coords)
        elif panel_name == '':
            if click_coords == '':
                print(click_coords)
        else:
            print('no panel found')


objects = {}

def register(object, name):
    objects.update({name: object})
        
##a = Event('click', 'mouse', area='define', part=2)
##Output:
##    args: ('click', 'mouse')
##    kwargs: {'part': 2, 'area': 'define'}


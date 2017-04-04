
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
        
    def __str__(self):
        ''' print(<obj>)==<obj>.__str__()'''
        return 'it is an event'

class InterfaceClick(Event):
    def __init__(self, panel_name=None, click_coords=None):
        kwargs = {'panel_name':panel_name, 'click_coords':click_coords}
        Event.__init__(self, **kwargs)
        if panel_name == 'StatusBar':
            print(panel_name)
        elif panel_name == 'SetupBar':
            if click_coords['x'] < 20:
                print(click_coords)
        elif panel_name == 'RunBar':
            if click_coords == '':
                print(click_coords)
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
    objects.update({object: name})
        
##a = Event('click', 'mouse', area='define', part=2)
##Output:
##    args: ('click', 'mouse')
##    kwargs: {'part': 2, 'area': 'define'}


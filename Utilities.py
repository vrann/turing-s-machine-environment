
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


# utilities
import re
from tkinter.filedialog import askopenfilename

def sign(val):
    '''signum(val)'''
    if val > 0:
        sign = 1
    elif val == 0:
        sign = 0
    else:
        sign = -1
    return sign

def compile_turing_code(path):
    try:
        file = open(path, 'r') # open code
        # convert turing app code to dictionary (compile)
        # using regular expression
        LINE = r"^[\s]*[.^\(]*\([\s]*([^\,\s]+)\,[\s]*(\d)[\s]*\)[\s]*->[\s]"\
        "*\([\s]*([^\,\s]*)[\s]*\,[\s]*(\d)[\s]*,[\s]*([LRSlrs])[\s]*\).*$"
        compiled = {} # the dictionary
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
                # print(qInitial, vInitial,'->',qResult, vResult, action)
                # add keyword and corresponding values into dictionary
                compiled[(qInitial, vInitial)] = (qResult, vResult, action)
        # save code in a variable
        # code = file.read()
        # print(compiled)
        file.close()
    except FileNotFoundError:
        compiled = None
        print('file not found')
    return compiled

def open_file():
    return askopenfilename()


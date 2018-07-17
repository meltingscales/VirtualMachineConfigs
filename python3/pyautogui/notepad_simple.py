from pprint import pprint

import pywinauto
from pywinauto import *

try:
    w: Application = Application().connect(title='Untitled - Notepad')
except pywinauto.findwindows.ElementNotFoundError:
    w: Application = Application().start(cmd_line=u'notepad.exe')

pprint(w.windows())

notepad: WindowSpecification = w['Notepad']

notepad.TypeKeys('hi')

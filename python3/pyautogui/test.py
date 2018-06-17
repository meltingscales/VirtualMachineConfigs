import os
from pprint import pprint

import pywinauto
from pywinauto import *
import pyautogui
from win32 import win32clipboard


def copy(w: WindowSpecification, k='^c'):
    w.TypeKeys(k)
    win32clipboard.OpenClipboard()
    return win32clipboard.GetClipboardData()


def binary_op(calc: Application, x, y, op='{+}'):
    calc.CalcFrame.TypeKeys(str(x) + op + str(y) + '{ENTER}')
    return copy(calc.CalcFrame)


def add(calc: Application, x, y):
    return binary_op(calc, x, y, '{+}')


def sub(calc: Application, x, y):
    return binary_op(calc, x, y, '{-}')


def mult(calc: Application, x, y):
    return binary_op(calc, x, y, '{*}')


def clear(calc: Application):
    calc.CalcFrame: WindowSpecification
    for i in range(0, 3):
        calc.CalcFrame.TypeKeys('{ESC}')


try:
    calc = Application().connect(title='Calculator')
except ElementNotFoundError as e:
    calc = Application().start(cmd_line='calc.exe')

clear(calc)
x = add(calc, 1, 2)
print(x)

for i in range(0, 10):
    x = mult(calc, i, i + 1)
    print(x)

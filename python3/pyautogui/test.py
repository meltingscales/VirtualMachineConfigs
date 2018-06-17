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


class Calculator(object):
    window: Application

    def __init__(self):
        try:
            self.window = Application().connect(title='Calculator')
        except ElementNotFoundError as e:
            self.window = Application().start(cmd_line='calc.exe')

    def binary_op(self, x, y, op='{+}'):
        self.window.CalcFrame.TypeKeys(str(x) + op + str(y) + '{ENTER}')
        return copy(self.window.CalcFrame)

    def add(self, x, y):
        return self.binary_op(x, y, '{+}')

    def sub(self, x, y):
        return self.binary_op(x, y, '{-}')

    def mult(self, x, y):
        return self.binary_op(x, y, '{*}')

    def div(self, x, y):
        return self.binary_op(x, y, '{/}')

    def clear(self):
        for i in range(0, 2):
            self.window.CalcFrame.TypeKeys('{ESC}')


calc = Calculator()

calc.clear()
x = calc.add(1, 2)
print(x)

for i in range(0, 10):
    x = calc.mult(i, i + 1)
    print(x)

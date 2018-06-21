import os
from pprint import pprint

import pywinauto
from pywinauto import *
from pywinauto.findbestmatch import MatchError
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

    def get_frame(self):
        try:
            return self.window.CalcFrame
        except MatchError:
            pass

        try:
            return self.window.ApplicationFrameInputSinkWindow
        except MatchError:
            pass
    
    def binary_op(self, x, y, op='{+}'):
        self.window.CalcFrame.TypeKeys(str(x) + op + str(y) + '{ENTER}')
        return copy(self.get_frame())

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

    def fib(self, n=0):
        if n == 0:
            return 0

        if n == 1:
            return 1

        return self.add(self.fib(n - 1), self.fib(n - 2))


calc = Calculator()

calc.clear()
x = calc.add(1, 2)
print(x)

print(calc.fib(6))


for i in range(0, 10):
    x = calc.mult(i, calc.add(i, 1))
    print(x)

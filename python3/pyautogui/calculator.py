import os
from pprint import pprint

import pywinauto
from pywinauto import *
from pywinauto.findbestmatch import MatchError
import pyautogui
from win32 import win32clipboard
from win32com.client import Dispatch
from packaging.version import Version, parse


def copy(w: WindowSpecification, k='^c'):
    w.TypeKeys(k) # Mimics CTRL-C
    win32clipboard.OpenClipboard() # Open clipboard
    return win32clipboard.GetClipboardData() # Return clipboard contents as string


class Calculator(object):
    window: Application
    frame: WindowSpecification
    version: dict

    def __init__(self, path='C:/Windows/System32/calc.exe'):
        try:
            self.window = Application().connect(title='Calculator')
        except ElementNotFoundError as e:
            self.window = Application().start(cmd_line=path)

        self.frame = None
        self.version = parse(Dispatch('Scripting.FileSystemObject').GetFileVersion(path))
        print(self.version)

    def get_frame(self):
	
        if self.frame is not None: # If we haven't asked for our frame yet
            return self.frame # Return what we found previously, and bypass version check

        print('first time asked for frame!!')

        if self.version < Version('10'):
            self.frame = self.window.CalcFrame
            return self.frame
        else:
            self.frame = self.window.ApplicationFrameInputSinkWindow
            return self.frame

    def binary_op(self, x, y, op='{+}'):
        s = str(x) + op + str(y) + '{ENTER}'
        print(s)
        self.get_frame().TypeKeys(s)
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
            self.get_frame().TypeKeys('{ESC}')

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
    x = calc.mult(i, i+1)
    print(x)

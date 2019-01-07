# https://docs.python.org/3.3/library/turtle.html?highlight=turtle

from turtle import *

# A black outline.
color('black')

size = int(textinput("Side lengths","How big should our circle be? (200 is medium)"))

for i in range(0, 4):
    forward(size/4) # We define our algorithm in terms of user input here.
    left(90)

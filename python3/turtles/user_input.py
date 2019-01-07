# https://docs.python.org/3.3/library/turtle.html?highlight=turtle

from turtle import *

# A black outline.
color('black')

# Start filling.
begin_fill()

size = input("How big should our circle be? (200 is medium)")

for i in range(0, 4): # Since we use a loop, we can save code and perhaps generalize some aspects of the code.
    forward(size)
    left(90)

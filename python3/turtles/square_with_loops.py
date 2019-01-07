# https://docs.python.org/3.3/library/turtle.html?highlight=turtle

from turtle import *

# A black outline.
color('black')

# Start filling.
begin_fill()

# Go forward 200 steps, and turn left.
# If we do this four times, we draw the four lines of a square!

for i in range(0, 4): # Since we use a loop, we can save code and perhaps generalize some aspects of the code.
    forward(200)
    left(90)

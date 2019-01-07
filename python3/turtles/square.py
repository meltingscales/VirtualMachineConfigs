# https://docs.python.org/3.3/library/turtle.html?highlight=turtle

from turtle import *

# A black outline.
color('black')

# Start filling.
begin_fill()

# Go forward 200 steps, and turn left.
# If we do this four times, we draw the four lines of a square!
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

# Something to note here is how 360 divided by 4 gives you 90...
# 
# We can use this to our advantage to generalize our code to produce ANY shape!

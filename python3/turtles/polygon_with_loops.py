# https://docs.python.org/3.3/library/turtle.html?highlight=turtle

from turtle import *

# A black outline.
color('black')

# Start filling.
begin_fill()

while True:

    # Ask for sides
    sides = int(textinput("Sides!", "Enter number of sides: "))

    # Delete previous drawings
    reset()

    # Produce a polygon!
    for i in range(0, sides):

        # We divide here to prevent each segment from being 100 units long.
        # Rather, we essentially say the radius is 100 here.
        forward(200/sides)
        left(360.0/sides)

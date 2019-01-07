# https://docs.python.org/3.3/library/turtle.html?highlight=turtle

from turtle import *

# A black outline.
color('black')

# This is a function definition.

# Functions are re-usable pieces of code that can make your code a lot
# easier to read and write.

# Declaring it here doesn't actually cause anything inside of it to execute,
# but you can use it later.
def draw_square():
    for i in range(0, 4):
        forward(200/4)
        left(90)


# Here we'll use our newly created draw_square function to make a 3x2 grid!


## FIRST ROW ##
draw_square() # Draw a square
setx(xcor()+50) # Move 50 to the right

draw_square() # Draw a square
setx(xcor()+50) # Move 50 to the right

draw_square() # Draw a square
setx(xcor() - 100) # Move back to the start
sety(ycor() - 50) # Go down 50

## SECOND ROW ##
draw_square() # Draw a square
setx(xcor()+50) # Move 50 to the right

draw_square() # Draw a square
setx(xcor()+50) # Move 50 to the right

draw_square() # Draw a square
setx(xcor()+50) # Move 50 to the right

# Just like our example where we draw four lines "manually", and then later
# generalize it, we can do the same here and create a re-usable "grid-drawing"
# function that can draw an arbitrarily-large grid!

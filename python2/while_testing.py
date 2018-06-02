
from while_testing import double_number
#from module import thingy #



cool_beans = ['cool','beans']


def gimme_bananas():

    x = "apple"

    while ('banana' not in x):

        x = raw_input("give me the bananas: ") #set x to user's input

        if ('banana' not in x):
            print("no bananas >:(")

def gimme_a_pos_number():
    x = -1

    while (x < 0):
        x = int(raw_input('non-negative number: '))

        if (x < 0):
            print("x is negative, try again!")

#gimme_bananas()

#pretty
x = int(raw_input("gimme da numbers!")) #original number

x = double_number(x) #double it

print(x) #print it
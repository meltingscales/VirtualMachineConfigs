# example of how to import functions from other files ('modules')
# from .while_true_loop import gimme_bananas
# from .while_true_loop import gimme_bananas as bananas_func
# from .while_true_loop import gimme_bananas, gimme_a_pos_number, cool_beans
# import * from .while_true_loop
# gimme_bananas()


#keyword  #name of function         #(arguments function takes, if any):
def       f                         (x, y):
    pass


def dont_gimme_five():

    x = 0

    while(x != 5): #when x is five, this is FALSE and we stop looping.

        x = int(raw_input("Don't enter 5 :")) #ask for input, turn it into an integer

    # we know they entered five because it would keep looping otherwise
    print("What did I tell you?!?")

# dont_gimme_five()

# a function that takes a number as an argument and doubles it, and returns it.
# This function can NOT take input from the user.

def double_number(x):

    x = x * 2

    return x


if __name__ == '__main__':
    x = int(raw_input("Enter a number to be doubled: "))

    while(x < 100):

        print("Just checked if "+str(x)+" was < 100.")
        x = double_number(x) #x = 64*2 = 128
        print(x) #128

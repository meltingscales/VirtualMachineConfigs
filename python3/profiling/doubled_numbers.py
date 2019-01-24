# Props for this file go to Patrick.

import cProfile

def doubled_numbers_1(size):
    """Gives you a list of numbers from 0 to size, but doubled."""

    # list from [0,1,2,3]
    single_numbers = [i for i in range(0, size)]

    # empty list
    lst = []

    # for [0,1,2...]
    for n in single_numbers:

        # add the number, but doubled.
        lst.append(n*2)

    return lst

def doubled_numbers_2(size):
    """Gives you a list of numbers from 0 to size, but doubled."""
    # good old list comprehension. this is very fast!
    return [i for i in range(0, size*2, 2)]

def doubled_numbers_3(size):
    """Gives you a list of numbers from 0 to size, but doubled."""

    # empty list
    lst = []
    
    # from i to size
    for i in range(0, size):
        
        # append i times two
        lst.append(i*2)
    
    return lst

def doubled_numbers_4(size):
    """Gives you a list of numbers from 0 to size, but doubled."""
    # good old list comprehension. this is also very fast!
    return [i*2 for i in range(0, size)]


# Sanity checks to make sure our functions work.
# You can consider this a teeny unit test.
assert(doubled_numbers_1(3) == [0,2,4])
assert(doubled_numbers_2(3) == [0,2,4])
assert(doubled_numbers_3(3) == [0,2,4])
assert(doubled_numbers_4(3) == [0,2,4])
assert(doubled_numbers_2(3) == doubled_numbers_1(3)) # Same arguments should give same results to functions that are supposed to return the same objects

# Profile all our functions with 1 million numbers 
print("doubled_numbers_1 performance:")
cProfile.run("doubled_numbers_1(1000000)")

print("doubled_numbers_2 performance:")
cProfile.run("doubled_numbers_2(1000000)")

print("doubled_numbers_3 performance:")
cProfile.run("doubled_numbers_3(1000000)")

print("doubled_numbers_4 performance:")
cProfile.run("doubled_numbers_4(1000000)")

# Joe Schmoe
# 20
# Brown

# no lists, no data structure. pls don't do this!
print('')
print("Single vars:")
fname = "Joe"
lname = "Schmoe"
age = 20
hair = "brown"

fname2 = "Joe"
lname2 = "Schmoe"
age2 = 20
hair2 = "brown"

print(fname, lname, age, hair)
print(fname2, lname2, age2, hair2)  # ew!

# using lists. A little better!!
print('')
print("lists:")
person = ["Joe", "Schmoe", 20, "brown"]
person2 = ["Joe", "Schmoe", 20, "brown"]

people = [person, person2]

for p in people:
    print(p)  # print person. MUCH better.

# using classes. a very good solution (not the 'best', as that's an opinion)
print('')
print('classes:')


class Person:
    def __init__(self, fn, ln, age, hc):
        self.firstname = fn
        self.lastname = ln
        self.age = age
        self.hair = hc

    def __str__(self):
        return "{} {} is {} years old and has {} hair.".format(
            self.firstname, self.lastname, self.age, self.hair)


people = [
    Person('joe', 'schmoe', 20, 'brown'),
    Person('sally', 'jane', 20, 'red'),  # assignment is very easy!
]

for p in people:
    print(str(p))  # yay!

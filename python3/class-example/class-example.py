# Defines a new datatype/object/class called 'Human'
class Human:

    # When you say `me = Human('Me')`, this function is called.
    # This is called a `constructor`, and it returns a new Human object.
    def __init__(self):
        self.name = 'joe'
        self.age = 0
        self.alive = True
        self.favorite_color = 'blue'

    def __eq__(self, other):  # Called when we do person1 == person2.
        return ((self.name == other.name) and
                (self.age == other.age) and
                (self.alive == other.alive) and
                (self.favorite_color == other.favorite_color))


# Create joe1 -> ("joe", 20, dead.)
joe1 = Human()
joe1.name = 'joe'
joe1.age = 20
joe1.alive = False

# Create joe2 -> ("schmoe", 20, dead.)
joe2 = Human()
joe2.name = 'schmoe'
joe2.age = 20
joe2.alive = False

print("Does joe1 == joe2?", joe1 == joe2)  # Check if they're the same?
# This is the same as     joe1.__eq__(joe2)
# Essentially this is     Human.__eq__(joe1, joe2)

joe2.name = "joe"  # Make them the same!

print("How about now?", joe1 == joe2)


# This is the bad/non-extensible way/long way NOT using classes.

# Here are some reasons why:
# If we want to add a thing to our `proto-human` class, we have to:
# - Add two arguments to compare_humans_bad()
# - Compare the two arguments
# - Make sure ALL other 'proto-human' objects have appropriate data
#
# This is in contrast with simply adding comstructor and __eq__ logic for the
# truly class-based version.

def compare_humans_bad(name1, age1, alive1, fc1, name2, age2, alive2, fc2):
    return ((name1 == name2) and
            (age1 == age2) and
            (alive1 == alive2) and
            (fc1 == fc2))


joebad1 = {'name': 'joe',
           'age': 20,
           'alive': False,
           'fc': 'blue'}

joebad2 = {'name': 'joe',
           'age': 20,
           'alive': False,
           'fc': 'blue'}

compare_humans_bad(joebad1['name'], joebad1['age'], joebad1['alive'], joebad1['fc'],
                   joebad2['name'], joebad2['age'], joebad2['alive'], joebad2['fc'])

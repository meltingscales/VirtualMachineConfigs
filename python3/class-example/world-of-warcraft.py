
class Being(object):
    alive = True
    name = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __add__(self, other):
        return str(self) + " and " + str(other) + " love eachother!"

    def kill(self, other):
        other.alive = False
        print(str(self)+" has killed "+str(other))

class Orc(Being):
    def __init__(self):
        super(Being, self).__init__()
        self.color = 'green'
        self.height = 'tall'

    

class Undead(Being):
    pass

class Human(Being):
    pass

class Mage(object):
    def __init__(self):
        attack = "magic"

class Warrior(object):
    def __init__(self):
        attack = "melee"

class Priest(object):
    def __init__(self):
        attack = "holy"

class OrcMage(Orc, Mage):
    pass

class OrcWarrior(Orc, Warrior):
    pass

class HumanMage(Human, Mage):
    pass

class HumanWarrior(Human, Warrior):
    pass

class HumanPriest(Human, Priest):
    pass

class UndeadMage(Undead, Mage):
    pass

class UndeadPriest(Undead, Priest):
    pass

om = OrcMage()
um = UndeadMage()
hm = HumanMage()

print(om.color)

Gormath = OrcWarrior()
Gormath.name = "Gormath"

Rust = UndeadPriest()
Rust.name = "Rust"
print(Rust)
print(Rust.alive)
print(Gormath.alive)


Rust.kill(Gormath)

print(Rust + Gormath)

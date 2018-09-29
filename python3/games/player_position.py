import os
import random
import copy #Allows to copy enemy object
from enum import Enum

# Credits to Christian for code from our lessons!

try:
    from getch import getch # Python 2 on Windows does not have getch.
except ImportError as e:

    if os.name == 'nt': # They're windows, use msvcrt.
        import msvcrt
        getch = msvcrt.getch
    else:
        raise e # They're Mac/Linux and do NOT have the getch package.

try:
    input = raw_input # Input handling for Python 2.
except NameError:
    pass

class ItemTypes(Enum): # Enumerated type, aka 'enum'. Used to mark something as belonging to one group of things.
    FIST = -1
    SWORD = 0
    WAND = 1
    BRICK = 2
    FROG = 3
    FRYING_PAN = 4
    COOL_SHOE = 5

class Materials(Enum):
    FLESH = -2
    MUD = -1
    WOODEN = 0
    GOLDEN = 1
    DIAMOND = 2
    HAIRY = 3
    CHEESE = 4
    PLATINUM = 5

def random_enum_type(e):
    random_pos = random.randint(0, len(e) - 1) # random number from 0 to 4
    #ItemTypes[3] # KeyError, as it only knows 'SWORD', 'WAND', etc...
    all_enums = list(e) # Instead of a dict, turn this into a list which can be indexed numerically.
    return all_enums[random_pos] # item at that position

class Item:

    def __init__(self, name, weaponType, materialType, attack, durability=100):
        self.name = name
        self.materialType = materialType
        self.weaponType = weaponType
        self.attack = attack
        self.durability = durability

    def __str__(self):
        return "{} {}".format(self.materialType.name, self.weaponType.name)

    def lose_durability(self, x):

        if self.durability is None: # It's unbreakable
            return

        self.durability -= x


def totally_random_item():

    type = random_enum_type(ItemTypes)
    mat = random_enum_type(Materials)
    att = random.randint(0, 15)

    name = type.name + " " + mat.name
    return Item(name, type, mat, att)

class Player:

    def __init__(self, name, health, attack, staminacap):
        self.name = name
        self.health = health
        self.attack = attack
        self.staminacap = staminacap
        self.stamina = staminacap # full, initially.
        self.item = Item("Fists", ItemTypes.FIST, Materials.FLESH, None) # Fists initially.
        self.x = 0
        self.y = 0
        # return self

    def hurt(self, damage): # When i am attacked.
        if(damage < 0): # Prevent negative damage.
            damage = 0
        self.health = self.health - damage
        if(self.health < 0): # Prevent negative health.
            self.health = 0


class Enemy:
    def __init__(self, name, health, attack): # Called when you do `Enemy(...)`
        self.name = name
        self.health = health
        self.attack = attack

    def __str__(self):
        return self.name

    def hurt(self, damage): # When i am attacked.
        if(damage < 0):
            damage = 0
        self.health = self.health - damage

    #def alive(self):
        #return "TODO"


enemies = [ # A list of pre-constructed Enemy instances to use later
    Enemy("Teeny", 10, 5),
    Enemy("Squirrel", 3, 25),
    Enemy("Goblin", 20, 4),
    Enemy("Brick", 100, 1),
    Enemy("Elite Squirrel", 55, 29),
]

name = input('Please enter your playername: ')
player = Player(name=name, health=100, attack=15, staminacap=100)

print("WASD to move.")
print("Q to quit.")

def fight_enemy():
    global player

    random_pos = random.randint(0, len(enemies)-1) # From zero to 3 (as len(enemies)-1 is 3)
    enemy = copy.deepcopy(enemies[random_pos]) # A random enemy
    # We use copy.deepcopy to create a new instance of our list of template enemies.

    print("You've encountered an enemy, a "+str(enemy)+"!")

    while enemy.health > 0 and player.health > 0: # While both are alive
        playerRandStrength = random.randint(0, 10) # Strength initiative


        print("Choose attack:")
        print("z. Light attack with {}".format(player.item))
        print("x. Heavy attack (Requires 10 stamina)")

        has_item = False

        if(player.item.materialType is not Materials.FLESH and
            player.item.weaponType is not ItemTypes.FIST and
            player.item.durability > 0):
            has_item = True
            print("c. Use your {} (costs 10 durability)".format(player.item))

        print("Stamina: " + str(player.stamina))
        print("Durability: " + str(player.item.durability))

        inp = getch()

        totalDamage = 0
        enemyDamage = 0

        if inp == b'z': # light attack
            totalDamage = player.attack - playerRandStrength #i.e. 15 - 3
            enemyDamage = enemy.attack + random.randint(0, 5) - 3

        if inp == b'x': # heavy attack

            if player.stamina > 0:
                totalDamage = player.attack + playerRandStrength #i.e. 15 + 3
                player.stamina = player.stamina - 10
                enemyDamage = enemy.attack + random.randint(0, 10) + 3

            if player.stamina <= 0:
                print("You are out of stamina for this attack :")

        if has_item and inp == b'c':
            totalDamage = player.attack + playerRandStrength + player.item.attack
            enemyDamage = enemy.attack + random.randint(0, 10) + 3
            player.item.lose_durability(10)

        player.hurt(enemyDamage)
        print("The "+str(enemy)+" has attacked you for "+str(enemyDamage) +"!")

        print("You hit the "+str(enemy)+" for "+str(totalDamage) +"!")
        enemy.hurt(totalDamage)

    if(enemy.health <= 0):
        print("The "+str(enemy)+" has perished!")
        print ("Your health is now: ")
        print(player.health)
        
        player.item = totally_random_item()
        print ("You recieved " +str(player.item))

    if(player.health <= 0):
        print("The "+str(enemy)+" has defeated " +str(name))
        exit()


def player_move():
    global player # Reference top scope

    inp = getch() # Gets a single character from the command line.

    print("You entered:")
    print(inp)

    if inp == b'w':  # up
        player.y += 1

    if inp == b'a':  # left
        player.x += -1

    if inp == b's':  # down
        player.y += -1

    if inp == b'd':  # right
        player.x += 1

    if inp == b'q':
        print("Exiting.")
        exit(0)

    if player.y < -10:
        print("It's sweltering down south!")
        player.hurt(1)
        print("HP: " + str(player.health))




while True: # Main loop

    player_move()

    if random.randint(0, 5) == 0: #1/5 chance per move of encountering enemy
        fight_enemy()

    print(player.x, player.y)

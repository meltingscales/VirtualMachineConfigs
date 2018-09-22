from getch import getch
import random
import copy #Allows to copy enemy object

#worky for python2
try:
    input = raw_input
except NameError:
    pass

class Player():
    def __init__(self, name, health, attack, staminacap):
        self.name = name
        self.health = health
        self.attack = attack
        self.staminacap = staminacap
        self.stamina = staminacap # full, initially.
        self.x = 0
        self.y = 0
        # return self

class Enemy:
    def __init__(self, name, health, attack): # Called when you do `Enemy(...)`
        self.name = name
        self.health = health
        self.attack = attack
        # return self

    def __str__(self):
        return self.name

    def hurt(self, damage): # When i am attacked.
        if(damage < 0):
            damage = 0
        self.health = self.health - damage

    def alive(self): # Am I alive?
        return "TODO"

enemies = [ # A list of pre-constructed Enemy instances to use later
    Enemy("Teeny", 10, 5),
    Enemy("Squirrel", 3, 15),
    Enemy("Goblin", 20, 4),
    Enemy("Brick", 100, 1),
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
        print("z. Light attack")
        print("x. Heavy attack (Requires 10 stamina)")
        print("Stamina: " + str(player.stamina))

        inp = getch()

        totalDamage = 0

        if inp == b'z': # light attack
            totalDamage = player.attack - playerRandStrength #i.e. 15 - 3

        if inp == b'x': # heavy attack

            if player.stamina > 0:
                totalDamage = player.attack + playerRandStrength #i.e. 15 + 3
                player.stamina = player.stamina - 10

            if player.stamina <= 0:
                print("You are out of stamina for this attack :")

        print("You hit the "+str(enemy)+" for "+str(totalDamage) +"!")
        enemy.hurt(totalDamage)

        # now have enemy attack

        # player.health gets subtracted by enemy.attack plus random number


    if(enemy.health <= 0):
        print("The "+str(enemy)+" has perished!")

    if(player.health <= 0):
        print("The "+str(enemy)+" has defeated you!")

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
        player.hp = player.hp - 1
        print("HP: " + str(player.hp))




while True: # Main loop

    player_move()

    if random.randint(0, 5) == 0: #1/5 chance per move of encountering enemy
        fight_enemy()

    print(player.x, player.y)

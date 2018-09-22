from getch import getch

x, y = 0, 0
hp = 100

print("WASD to move.")
print("Q to quit.")


def player_move():
    global x, y, hp

    inp = getch()

    print("You entered:")
    print(inp)

    if inp == b'w':  # up
        y += 1

    if inp == b'a':  # left
        x += -1

    if inp == b's':  # down
        y += -1

    if inp == b'd':  # right
        x += 1

    if inp == b'q':
        print("Exiting.")
        exit(0)

    if y < -10:
        print("It's sweltering down south!")
        hp = hp - 1
        print("HP: " + str(hp))


while True:
    player_move()

    print(x, y)

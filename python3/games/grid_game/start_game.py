from os import system, name
from pprint import pprint

from control import inputs
from game import Game
from getch import *
from item import Item
from location import Location
from player import Player
from tile import Tile
from world import World


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # it be linux
    else:
        _ = system('clear')


if __name__ == '__main__':

    player = Player(sprite="@")
    world = World()
    game = Game(player=player, world=world)

    coolbeantile = Tile(name="cool bean", sprite=',')

    coolbeantile.add_item(Item(sprite='*', name="Asterisk of Power"))

    world[2, 1] = coolbeantile

    while True:

        inp: str = getch()

        buf = game.render_grid()

        clear()

        if inp == inputs['UP'].key:
            game.move_player(Location(0, -1))

        elif inp == inputs['LEFT'].key:
            game.move_player(Location(-1, 0))

        elif inp == inputs['DOWN'].key:
            game.move_player(Location(0, 1))

        elif inp == inputs['RIGHT'].key:
            game.move_player(Location(1, 0))

        elif inp == inputs['QUIT'].key:
            exit(0)

        buf[game.player.location.y - 1][game.player.location.x - 1] = game.player.sprite

        for row in buf:
            if isinstance(row, list):
                for char in row:
                    print(char, end='')
                print('\n')

        pprint(buf)

        print(repr(game.player.location))
        print(" > ", end='')
        try:
            print(inp.decode("utf-8") + " aka " + str(inp))
        except UnicodeDecodeError as e:
            print(inp)

        current_tile = world[player.location]

        print(f"Below you is a '{current_tile.name}'.")

        if len(current_tile.ground) > 0:
            print(f"At your feet lie the following item(s):")
            print(repr(current_tile.ground))

from copy import deepcopy

from location import Location
from tile import Tile, tiles


class World(object):
    """
    A World.
    """

    width: int = 5
    """How wide is this World?"""

    height: int = 5
    """How tall is this World?"""

    grid: [[Tile]] = []
    """What's in this World?"""

    def __getitem__(self, item: Location) -> Tile:

        if isinstance(item, list) or isinstance(item, tuple):
            # They pass in a list instead of a tuple
            item = Location(item)

        if not isinstance(item, Location):
            raise IndexError(f"You must index a {World.__name__} at a {Location.__name__}, not '{item}'!")

        return self.grid[item.y - 1][item.x - 1]

    def __setitem__(self, item: Location, value: Tile):

        if isinstance(item, list) or isinstance(item, tuple):
            # They pass in a list instead of a tuple
            item = Location(item)

        if not isinstance(item, Location):
            raise IndexError(f"You must index a {World.__name__} at a {Location.__name__}, not '{item}'!")

        self.grid[item.y - 1][item.x - 1] = value

    def init_blank_grid(self):

        for i in range(self.height):
            tr = []

            for i in range(self.width):
                tr.append(deepcopy(tiles['stone_floor']))

            self.grid.append(tr)

    def __init__(self):
        self.init_blank_grid()

    def tick(self):
        """Called when one unit of in-game time has passed."""
        pass

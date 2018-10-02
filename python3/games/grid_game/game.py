from location import Location
from tile import Tile


class Game:

    def position_player_in_middle(self):
        self.player.location.x = self.world.width // 2
        self.player.location.y = self.world.height // 2

    def __init__(self, *args, **kwargs):
        self.player = kwargs.pop("player")
        self.world = kwargs.pop("world")

        self.position_player_in_middle()

    def normalize_player_position(self):

        if self.player.location.x >= self.world.width:  # x too large
            self.player.location.x -= self.world.width  # make x smaller

        if self.player.location.x < 0:  # x too small
            self.player.location.x += self.world.width  # make x bigger

        if self.player.location.y >= self.world.height:  # y too large
            self.player.location.y -= self.world.height  # make y smaller

        if self.player.location.y < 0:  # y too big
            self.player.location.y += self.world.width  # make y bigger

    def move_player(self, vector: Location):
        """Move the player relative to a vector."""
        self.player.location += vector

        self.normalize_player_position()

    def fill_grid(self, tile: Tile, start=Location(0, 0), end=Location(3, 3)):
        pass

    def render_grid(self) -> [[str]]:

        ret = []

        for row in self.world.grid:
            ts = []

            tile: Tile
            for tile in row:
                ts.append(tile.display_sprite())

            ret.append(ts)

        return ret

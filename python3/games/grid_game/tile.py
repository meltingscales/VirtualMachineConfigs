from utilspie.collectionsutils import frozendict

from entity import Entity
from hassprite import HasSprite
from item import Item


class Tile(HasSprite):
    """
    A Tile.
    Can have Items on it, and Entities occupying it.
    """

    name = "Unnamed Tile"
    """The name of the tile."""

    ground = []
    """A list of all Items on the ground of this Tile."""

    entities: [Entity] = []
    """A list of all Entities occupying this Tile."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = kwargs.get('name', self.name)
        self.ground = kwargs.get('ground', self.ground)
        self.entities = kwargs.get('entities', self.entities)

    def add_item(self, item: Item):
        self.ground.append(item)


# Useful list of tiles.
tiles = frozendict({
    "stone_floor":
        Tile(sprite="_", name="Stone floor"),
})

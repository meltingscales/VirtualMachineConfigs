from hassprite import HasSprite
from location import Location


class Player(HasSprite):
    location = Location(0, 0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

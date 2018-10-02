from .hassprite import HasSprite


class Block(HasSprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

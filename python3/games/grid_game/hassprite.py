class HasSprite(object):
    sprite = '?'
    animations = ['!', '.']

    def __init__(self, *args, **kwargs):
        self.sprite = kwargs.pop('sprite')
        self.animations = kwargs.pop('animations') if 'animations' in kwargs else self.animations

    def display_sprite(self, ticks=None):
        """
        :param ticks: The ticks to use to display the animation of this sprite.
                Just returns the base sprite if no ticks given.
        :return: The visual representation of this sprite.
        """
        if ticks is None:  # They don't want any animation
            return self.sprite
        else:
            return self.animations[ticks % len(self.animations)]

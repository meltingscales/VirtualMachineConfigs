from utilspie.collectionsutils import frozendict

from hassprite import HasSprite


class Item(HasSprite):
    name = "Default Item"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = kwargs.get("name", self.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


# Useful list of items.
items = frozendict({
    'pebble':
        Item(sprite=".", name="pebble"),

    'stick':
        Item(sprite="/", name="stick"),
})

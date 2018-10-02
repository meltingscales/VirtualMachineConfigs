class Control(object):

    def __init__(self, key: str, name: str, desc: str):
        self.key = key
        self.name = name
        self.desc = desc

    def __str__(self):
        return f"<{self.name}>: {self.desc}"


inputs = {
    "UP": Control(b'w', "UP", "Move player up."),
    "LEFT": Control(b'a', "LEFT", "Move player left."),
    "DOWN": Control(b's', "DOWN", "Move player down."),
    "RIGHT": Control(b'd', "RIGHT", "Move player right."),

    "PICKUP ITEM": Control(b'p', "PICKUP ITEM", "Picks up item at player's feet."),

    "QUIT": Control(b'q', "QUIT", "Quits the game."),
}

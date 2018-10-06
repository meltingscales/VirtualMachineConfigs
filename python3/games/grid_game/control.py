class Control(object):

    def __init__(self, key: str, name: str, desc: str):
        self.key = key
        self.name = name
        self.desc = desc

    def __str__(self):
        return f"<{self.key.decode('utf-8')}: {self.name:15s} >: {self.desc}"


inputs = {
    "UP": Control(b'w', "UP", "Move player up."),
    "LEFT": Control(b'a', "LEFT", "Move player left."),
    "DOWN": Control(b's', "DOWN", "Move player down."),
    "RIGHT": Control(b'd', "RIGHT", "Move player right."),

    "PICKUP ITEM": Control(b'p', "PICKUP ITEM", "Picks up item at player's feet."),

    "HELP": Control(b'?', "HELP", "Display help."),
    "QUIT": Control(b'q', "QUIT", "Quits the game."),
}


def print_controls():
    for key, control in inputs.items():
        print(control)

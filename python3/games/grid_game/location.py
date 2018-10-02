class Location(object):
    x, y = 0, 0

    def __init__(self, x=None, y=None):
        if (isinstance(x, list) or isinstance(x, tuple)):
            # They pass x as a list instead of (int,int)
            y, x = x[0], x[1]

        if x is None or y is None:
            raise Exception("Location was passed bad x or y coords:", x, y)

        self.x = x
        self.y = y

    def __add__(self, other):
        return Location(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Location(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Location(-self.x, -self.y)

    def __mul__(self, other):
        return Location(self.x * other.x, self.y * other.y)

    def __eq__(self, other):
        return self.x is other.x \
               and self.y is other.y

    def __repr__(self):
        return f"({self.x},{self.y})"


# List of Locations for convenience.
#
# If you want NW, just add d['N'] + d['W'].
# Etc.
directions = {
    "N": Location(0, 1),
    "S": Location(0, -1),
    "E": Location(1, 0),
    "W": Location(-1, 0),
}

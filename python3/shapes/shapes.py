import math
from pprint import pprint
import time

import numpy as np
from numba import jit
from functools import lru_cache

scale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\" ^`'. "
scale2 = " .:-=+*#%@"


def square(x=5, y=5, char='*', sep=' '):
    s = ''
    s += x * char
    s += '\n'

    for i in range(1, y - 1):
        s += char
        s += sep * (x - 2)
        s += char
        s += '\n'

    s += x * char

    return s


@lru_cache(maxsize=None, typed=False)
def distance(p1, p2):
    return math.sqrt(math.pow((p1[0] - p2[0]), 2) +
                     math.pow((p1[1] - p2[1]), 2))


@jit
def mandelbrot(c, maxiter):
    z = c
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return 0


@lru_cache(maxsize=None, typed=False)
def number_to_char(number, min=-5, max=5, chars=scale2):
    """Given a number and a range, return a character that falls within that range.

    If you don't know what that means, just try giving it a range."""
    ns = np.linspace(max, min, len(chars))

    for i in range(0, len(chars)):
        # print(f"comparing {number} to {ns[i]} @ index {i}")
        if number >= ns[i]:
            # print("!!!")
            return chars[i]
    return chars[-1]


@lru_cache(maxsize=None)
def circle_distances(radius=5, center=(3, 3)):
    r = radius + 1

    ret = [[[] for i in range(r)] for i in range(r)]

    for y in range(0, r, 1):
        for x in range(0, r, 1):
            ret[y][x] = (distance((x, y,), center))
    return ret


@jit
def mandelbrot_set(x=(-1.0, 1.0,), y=(-1.0, 1.0,), width=50, height=50, maxiter=100):
    xmin, xmax = x
    ymin, ymax = y

    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j * r2[j], maxiter)
    return (r1, r2, n3)


if __name__ == '__main__':
    print(square())
    print()
    print(square(x=3, y=3))

    for i in range(-5, 6):
        print(f"{i:2} = {number_to_char(i)}")

    rad = 50
    center = (rad // 2, rad // 2)
    cd = circle_distances(rad, center)

    for row in cd:
        for i in row:
            print(number_to_char(i, 0, rad // 2), end='')
        print()

    time.sleep(1)

    ms = mandelbrot_set()[2]

    for row in list(ms):
        for i in list(row):
            # print(i)
            print(number_to_char(float(i)), end='')
        print()

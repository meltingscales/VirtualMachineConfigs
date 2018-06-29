import math
import time
from functools import lru_cache

import numpy as np
from lib import read_file_cached
from numba import jit

scale1 = read_file_cached('scale1.txt')[0]
scale2 = read_file_cached('scale2.txt')[0]


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


@lru_cache(maxsize=None)
def mandelbrot(c, maxiter, pow=2.0, f=lambda z, c, pow: (z ** pow) + c):
    z = c
    for n in range(maxiter):
        if abs(z) > 2.0:
            return n
        z = f(z, c, pow)
    return 0.0


@lru_cache(maxsize=None, typed=False)
def number_to_char(number: float, shading=(-5.0, 5.0), shaders=scale2):
    """Given a number and a range, return a character that falls within that range.

    If you don't know what that means, just try giving it a range."""
    minimum, maximum = shading

    ns = np.linspace(maximum, minimum, len(shaders))

    for i in range(0, len(shaders)):
        # print(f"comparing {number} to {ns[i]} @ index {i}")
        if number >= ns[i]:
            # print("!!!")
            return shaders[i]
    return shaders[-1]


@lru_cache(maxsize=None)
def circle_distances(radius=5, center=(3, 3)):
    r = radius + 1

    ret = [[[] for i in range(r)] for i in range(r)]

    for y in range(0, r, 1):
        for x in range(0, r, 1):
            ret[y][x] = (distance((x, y,), center))
    return ret


@jit
def mandelbrot_set(x=(-1.0, 1.0,), y=(-1.0, 1.0,), dim=(50, 50), maxiter=100):
    xmin, xmax = x
    ymin, ymax = y
    width, height = dim

    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((height, width))
    for i in range(width):
        for j in range(height):
            n3[j, i] = mandelbrot(r1[i] + 1j * r2[j], maxiter)
    return (r1, r2, n3)

@jit
def mandel_to_text(set, shading, shaders, conversion=lambda x: float(x)):
    ret = []

    for row in set:
        tr = ""

        for x in row:
            tr += number_to_char(conversion(x), shading, shaders)

        ret.append(tr)

    return ret


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
            print(number_to_char(i, (0, rad / 2)), end='')
        print()

    time.sleep(1)

    a, b, ms = mandelbrot_set(dim=(10, 10))

    print(ms)
    print(a)
    print(b)
	
    for row in list(ms):
        for i in list(row):
            # print(i)
            print(number_to_char(float(i)), end='')
        print()

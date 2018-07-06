from tkinter import *
from functools import lru_cache

@lru_cache(maxsize=None)
def mandel(kx, ky, color):
    """ calculates the pixel color of the point of mandelbrot plane
        passed in the arguments """

    maxIt = 256
    c = complex(kx, ky)
    z = complex(0.0, 0.0)
    for i in range(maxIt):
        z = z * z + c
        if abs(z) >= 2.0:
            return (255 - color[i], 0, 0)
    return (0, 0, 0)


def prepare_mdb(x, y, dim):
    """ pre-calculates coordinates of the mandelbrot plane required for each
      pixel in the screen"""
    xa, xb = x
    ya, yb = y
    w, h = dim

    xm = [xa + (xb - xa) * kx / w for kx in range(w)]
    ym = [ya + (yb - ya) * ky / h for ky in range(h)]

    return [xm, ym]

@lru_cache(maxsize=None)
def mandel_pixels(dim, x, y, palette):
    xm, ym = prepare_mdb(x, y, dim)  # Make all possible x,y coords.

    pixels = " ".join(
        ("{" + " ".join(('#%02x%02x%02x' % mandel(i, j, palette) for i in xm)) + "}" for j in ym))

    return pixels

class MandelImage(PhotoImage):
    x = [-2.0, 1.0]
    y = [-1.5, 1.5]
    dim = [640, 480]
    palette = tuple([int(255 * (i / 255) ** 12) for i in range(255, -1, -1)])

    def __init__(self, *args, **kwargs):
        if 'width' in kwargs and 'height' in kwargs:
            self.dim = [kwargs['width'], kwargs['height']]

        if 'palette' in kwargs:
            self.palette = kwargs.pop('palette')

        super().__init__(*args, **kwargs)

    def display_mandelbrot(self):
        
        pixels = mandel_pixels(tuple(self.dim), tuple(self.x), tuple(self.y), self.palette)
        
        self.put(pixels)

    def offset(self, vector):
        x, y = vector

        self.x[0] += x
        self.x[1] += x

        self.y[0] += y
        self.y[1] += y


if __name__ == '__main__':
    root = Tk()

    dim = [500, 500]
    w, h = dim

    # Second method, with a function...
    window = Toplevel(master=root)
    canvas = Canvas(window, width=w, height=h, bg='#000000')
    image = MandelImage(width=w, height=h)
    canvas.create_image((0, 0), image=image, state="normal", anchor=NW)
    canvas.image = image

    canvas.image.display_mandelbrot()

    canvas.pack()

    # Callbacks
    window.bind('<Up>', lambda event: (canvas.image.offset([0, -1]), canvas.image.display_mandelbrot()))
    window.bind('<Down>', lambda event: (canvas.image.offset([0, 1]), canvas.image.display_mandelbrot()))
    window.bind('<Left>', lambda event: (canvas.image.offset([-1, 0]), canvas.image.display_mandelbrot()))
    window.bind('<Right>', lambda event: (canvas.image.offset([1, 0]), canvas.image.display_mandelbrot()))

    # Mainloop
    mainloop()

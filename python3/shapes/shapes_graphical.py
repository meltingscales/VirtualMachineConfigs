from tkinter import *
from functools import lru_cache
from lib import *

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

@lru_cache(maxsize=None)
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
    xm, ym = prepare_mdb(tuple(x), tuple(y), dim)  # Make all possible x,y coords.

    pixels = " ".join(
        ("{" + " ".join(('#%02x%02x%02x' % mandel(i, j, palette) for i in xm)) + "}" for j in ym))

    return pixels

class MandelImage(PhotoImage):

    def reset_coords(self):
        self.x = [-2.0, 1.0]
        self.y = [-1.5, 1.5]
        self.dim = [200, 200]
        self.palette = tuple([int(255 * (i / 255) ** 12) for i in range(255, -1, -1)])

    def __init__(self, *args, **kwargs):
        self.reset_coords()
        
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

        mult = abs(self.x[0] - self.x[1]) / 10  # a tenth of screen width

        self.x[0] += (x * mult)
        self.x[1] += (x * mult)

        self.y[0] += -(y * mult)
        self.y[1] += -(y * mult)

    def zoomybad(self, factor: float):
        """Flawed zoom.
        Biased towards [0,0].
        A result of my laziness ;) """
 
        if factor == 0.0:
            factor = 1.0

        if factor > 0.0:
            self.x[0] *= factor
            self.x[1] *= factor

            self.y[0] *= factor
            self.y[1] *= factor
        else:
            factor = -factor  # Don't want to flip our coords around!

            self.x[0] /= factor
            self.x[1] /= factor

            self.y[0] /= factor
            self.y[1] /= factor


    def zoomy(self, factor):
        mid = midpoint((self.x[0],self.y[0]), (self.x[1],self.y[1]))

        p1, p2 = ((self.x[0], self.y[0]), (self.x[1], self.y[1]))
        
        print(f'midpoint of {p1} and {p2} is {mid}.')

        mid1 = midpoint(p1, mid)
        mid2 = midpoint(p2, mid)

        print(mid1)
        print(mid2)

        if(factor <= 1): # TODO fix this and have factor var scale the actual zooming factor
            self.x[0], self.y[0] = list(mid1)
            self.x[1], self.y[1] = list(mid2)
        else:
            self.x[0], self.y[0] = addpoint(mid1, p1)
            self.x[1], self.y[1] = addpoint(mid2, p2)

if __name__ == '__main__':
    root = Tk()

    dim = [200, 200]
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
    window.bind('<Up>', lambda event: (canvas.image.offset([0.0, 1.0]), canvas.image.display_mandelbrot()))
    window.bind('<Down>', lambda event: (canvas.image.offset([0.0, -1.0]), canvas.image.display_mandelbrot()))
    window.bind('<Left>', lambda event: (canvas.image.offset([-1.0, 0.0]), canvas.image.display_mandelbrot()))
    window.bind('<Right>', lambda event: (canvas.image.offset([1.0, 0.0]), canvas.image.display_mandelbrot()))

    window.bind('<=>', lambda event: (canvas.image.zoomy(0.5), canvas.image.display_mandelbrot()))
    window.bind('<Key-minus>', lambda event: (canvas.image.zoomy(2.0), canvas.image.display_mandelbrot()))

    window.bind('r', lambda event: (canvas.image.reset_coords(), canvas.image.display_mandelbrot()))
    window.bind('q', lambda event: (exit(0)))
    
    canvas.image.zoomy(1.5)
    
    # Mainloop
    mainloop()

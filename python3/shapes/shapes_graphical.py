from tkinter import *


class MandelImage(PhotoImage):
    pass


def up_key(event):
    print("WHO PRESSED UP?")


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


def display_mandelbrot(canvas, color, dim=[640, 480], x=[-2.0, 1.0], y=[-1.5, 1.5]):
    w, h = dim

    xm, ym = prepare_mdb(x, y, dim)  # Make all possible x,y coords.

    image = PhotoImage(width=w, height=h)

    canvas.create_image((0, 0), image=image, state="normal", anchor=NW)
    canvas.image = image

    pixels = " ".join(("{" + " ".join(('#%02x%02x%02x' % mandel(i, j, color) for i in xm)) + "}" for j in ym))

    image.put(pixels)


if __name__ == '__main__':
    root = Tk()

    dim = [50, 50]
    w, h = dim

    # corners of  the mandelbrot plan to display
    x = [-2.0, 1.0]
    y = [-1.5, 1.5]

    # precalculated color table
    color = [int(255 * (i / 255) ** 12) for i in range(255, -1, -1)]
    xm, ym = prepare_mdb(x, y, dim)

    # Second method, with a function...
    window = Toplevel(master=root)
    canvas = Canvas(window, width=w, height=h, bg='#000000')

    display_mandelbrot(canvas, color, dim, x, y)

    canvas.pack()

    # Callbacks
    window.bind('<Up>', up_key)

    # Mainloop
    mainloop()

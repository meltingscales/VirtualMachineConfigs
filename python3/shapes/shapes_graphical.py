from tkinter import * 
from time import clock

def up_key(event):
  print("WHO PRESSED UP?")

def mandel(kx,ky):
  """ calculates the pixel color of the point of mandelbrot plane
      passed in the arguments """

  global clr
  maxIt = 256
  c = complex(kx, ky)
  z = complex(0.0, 0.0)
  for i in range(maxIt):
      z = z * z + c
      if abs(z) >= 2.0:
         return (255-clr[i],0,0)
  return(0,0,0)

def prepare_mdb(x,y,dim):
    """ pre-calculates coordinates of the mandelbrot plane required for each
      pixel in the screen"""
    xa, xb = x
    ya, yb = y
    w, h = dim

    xm=[xa + (xb - xa) * kx / w for kx in range(w)]
    ym=[ya + (yb - ya) * ky / h for ky in range(h)]

    return xm, ym

def display_mandelbrot():
    pass

w, h = [640, 480]

#corners of  the mandelbrot plan to display  
x = [-2.0, 1.0]
y = [-1.5, 1.5]

#precalculated color table
clr=[ int(255*((i/255)**12)) for i in range(255,-1,-1)]
xm, ym = prepare_mdb(x, y, (w, h))

#Tk 
window = Tk()
canvas = Canvas(window, width = w, height = h, bg = "#000000")

t1=clock()

img = PhotoImage(width = w, height = h)

canvas.create_image((0, 0), image = img, state = "normal", anchor = NW)

pixels=" ".join(("{"+" ".join(('#%02x%02x%02x' % mandel(i,j) for i in xm))+"}" for j in ym))

img.put(pixels)

window.bind('<Up>',up_key)

canvas.pack()

print(clock()-t1)

mainloop()

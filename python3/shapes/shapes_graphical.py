from tkinter import Tk, Canvas, PhotoImage,NW,mainloop 
from time import clock

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

def prepare_mdb(xa,xb,ya,yb):
    """ pre-calculates coordinates of the mandelbrot plane required for each
      pixel in the screen"""

    global x,y,xm,ym
    xm.clear
    ym.clear
    xm=[xa + (xb - xa) * kx /x  for kx in range(x)]
    ym=[ya + (yb - ya) * ky /y  for ky in range(y)]


x=640
y=480
#corners of  the mandelbrot plan to display  
xa = -2.0; xb = 1.0
ya = -1.5; yb = 1.5
#precalculated color table
clr=[ int(255*((i/255)**12)) for i in range(255,-1,-1)]
xm=[]
ym=[]
prepare_mdb(xa,xb,ya,yb)

#Tk 
window = Tk()
canvas = Canvas(window, width = x, height = y, bg = "#000000")
t1=clock()
img = PhotoImage(width = x, height = y)
canvas.create_image((0, 0), image = img, state = "normal", anchor = NW)
pixels=" ".join(("{"+" ".join(('#%02x%02x%02x' % mandel(i,j) for i in xm))+"}" for j in ym))
img.put(pixels)
canvas.pack()
print(clock()-t1)
mainloop()

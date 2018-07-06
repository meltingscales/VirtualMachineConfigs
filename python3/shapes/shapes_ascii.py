import sys

from asciimatics.effects import Cycle, Stars
from asciimatics.event import KeyboardEvent, MouseEvent
from asciimatics.exceptions import ResizeScreenError, StopApplication
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Frame, Layout, Divider, Label, Widget
from lib import *
from shapes import mandelbrot_set, mandel_to_text

KEY_UP = -204
KEY_DOWN = -206
KEY_LEFT = -203
KEY_RIGHT = -205
KEY_VECTORS = {
    KEY_UP: [0.0, 1.0, ],
    KEY_DOWN: [0.0, -1.0, ],
    KEY_LEFT: [-1.0, 0.0, ],
    KEY_RIGHT: [1.0, 0.0, ]
}

KEY_PLUS = 61
KEY_MINUS = 45
KEY_C = 99

"""

Arrow keys to move,

Plus/minus to zoom.

'C' to center.

"""


class BetterLabel(Label):

    def set_text_from_list(self, l: list):
        self.text = ''

        for item in l:
            self.new_line(item)

    def append(self, text):
        # print(self.__dict__)
        self.text = (self.text + text)

    def new_line(self, text, newl='\n'):
        self.append(text + newl)


class MandelDisplay(BetterLabel):

    def set_dim_from_termsize(self, pad=5):
        self.dim = (self.screen.width - pad,
                    self.screen.height - pad)
        """ How many units is big our graph?"""

    def reset_coords(self):

        self.x = [-1.0, 1.0]
        """The x coords to plot."""

        self.y = [-1.0, 1.0]
        """The y coords to plot."""

        self.set_dim_from_termsize()

        self.shading = (-1, 10)
        """How far low and high shall we shade?"""

        self.shaders = read_file_cached('scale1.txt')[0]
        """What chars to use for shading?"""

        self.maxiter = 100
        """How many mandelbrot iterations?"""

    def __init__(self, *args, **kwargs):
        self.screen = kwargs.pop('screen')  # For referring to the width and height later

        super(BetterLabel, self).__init__(*args, **kwargs)

        self.reset_coords()

    def generate_status(self) -> str:
        """Generate a status bar with coords, zoom, etc."""
        return "{} by {} from x={},y={}".format(
            self.dim[1],
            self.dim[0],
            self.x,
            self.y
        )

    def generate_mandelbrot(self, x=None, y=None, dim=None, shading=None, shaders=None, maxiter=None):
        """Given some parameters, update my view with a pretty fractal!"""

        x = x or self.x
        y = y or self.y
        dim = dim or self.dim
        shading = shading or self.shading
        shaders = shaders or self.shaders
        maxiter = maxiter or self.maxiter

        w, h, mandel_set = mandelbrot_set(x, y, dim, maxiter)  # Get list o' numbas
        mandel_text = mandel_to_text(mandel_set, shading, shaders)

        self.set_text_from_list(mandel_text)

    def direction(self, dim: list, ):
        """Move graph's boundaries by `dim`.

        Example:

            direction([1,1,])
            ->
            Window moves up and to the right by one unit.
            """
        x, y = dim

        mult = abs(self.x[0] - self.x[1]) / 10  # a tenth of screen width

        self.x[0] += (x * mult)
        self.x[1] += (x * mult)

        self.y[0] += -(y * mult)
        self.y[1] += -(y * mult)

    def zoombad(self, factor: float):
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

    def zoom(self, factor: float):
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


class MandelControls(Widget):
    pass


class Mandel(Frame):
    def __init__(self, screen: Screen):
        super(Mandel, self).__init__(
            screen, screen.height, screen.width, has_border=True, name="Mandelbrot_viewer"
        )

        # Create the (very simple) form layout...
        layout = Layout([screen.width], fill_frame=True)
        self.add_layout(layout)
        # self.root.add_widget(Button('OK', self._ok))
        self.status = BetterLabel('')

        self.mandelbrot = MandelDisplay('I AM FRACTAL',
                                        screen.width,
                                        screen=screen)

        layout.add_widget(self.status)
        layout.add_widget(Divider())
        layout.add_widget(self.mandelbrot)

        self.fix()

    def update_status(self):
        self.status.text = self.mandelbrot.generate_status()
        self.status.update(0)

    def process_event(self, event):
        # Do the key handling for this Frame.
        if isinstance(event, KeyboardEvent):

            print(event.key_code, Screen.ctrl(event.key_code))

            if event.key_code in [Screen.ctrl("c")]:
                raise StopApplication("User quit")

            if event.key_code == KEY_C:
                self.mandelbrot.reset_coords()

            if event.key_code == KEY_MINUS:
                self.mandelbrot.zoom(1.5)

            if event.key_code == KEY_PLUS:
                self.mandelbrot.zoom(-1.5)

            if event.key_code in KEY_VECTORS.keys():
                self.mandelbrot.direction(KEY_VECTORS[event.key_code])

            self.mandelbrot.set_dim_from_termsize()
            self.mandelbrot.generate_mandelbrot()
            self.update_status()

        elif isinstance(event, MouseEvent):
            pass

        # Now pass on to lower levels for normal handling of the event.
        return super(Mandel, self).process_event(event)


def demo(screen, old_scene):
    screen.play([Scene([Mandel(screen)], -1)], stop_on_resize=True, start_scene=old_scene)


def demo2(screen):
    effects = [
        Cycle(
            screen,
            FigletText("ASCIIMATICS", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("ROCKS!", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])


if __name__ == '__main__':

    last_scene = None
    while True:
        try:
            Screen.wrapper(demo, catch_interrupt=False, arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError as e:
            last_scene = e.scene

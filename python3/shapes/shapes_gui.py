import sys
from pprint import pprint

from asciimatics.effects import Cycle, Stars
from asciimatics.event import Event, KeyboardEvent, MouseEvent
from asciimatics.renderers import FigletText
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, Label, Button, TextBox, Widget, Canvas
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication

from lib import read_file_cached
from shapes import mandelbrot_set, mandel_to_text

KEY_UP = -204
KEY_DOWN = -206
KEY_LEFT = -203
KEY_RIGHT = -205
ARROW_KEYS = [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]


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

    def __init__(self, *args, **kwargs):
        super(BetterLabel, self).__init__(*args, **kwargs)
        self.x = [-1, 1]
        """The x coords to plot."""

        self.y = [-1, 1]
        """The y coords to plot."""

        self.dim = (30, 30)
        """ How many units is big our graph?"""

        self.shading = (-1, 10)
        """How far low and high shall we shade?"""

        self.shaders = read_file_cached('scale1.txt')[0]
        """What chars to use for shading?"""

        self.maxiter = 100
        """How many mandelbrot iterations?"""

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

    def direction(self, dim: list, mult: float = 0.1):
        """Move graph's boundaries by `dim`.

        Example:

            direction([1,1,])
            ->
            Window moves up and to the right by one unit.
            """
        x, y = dim

        self.x[0] += (x * mult)
        self.x[1] += (x * mult)

        self.y[0] += -(y * mult)
        self.y[1] += -(y * mult)


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
        layout.add_widget(Text('hi', 'there'))
        layout.add_widget(Divider())

        self.mandelbrot = MandelDisplay('I AM FRACTAL',
                                        screen.width,
                                        )
        layout.add_widget(self.mandelbrot)

        self.fix()

    def process_event(self, event):
        # Do the key handling for this Frame.
        if isinstance(event, KeyboardEvent):

            # print(event)
            # print(event.key_code)

            if event.key_code in [Screen.ctrl("c")]:
                raise StopApplication("User quit")

            if event.key_code in ARROW_KEYS:
                if event.key_code == KEY_UP:
                    self.mandelbrot.direction([0, 1, ])

                if event.key_code == KEY_DOWN:
                    self.mandelbrot.direction([0, -1, ])

                if event.key_code == KEY_LEFT:
                    self.mandelbrot.direction([-1, 0, ])

                if event.key_code == KEY_RIGHT:
                    self.mandelbrot.direction([1, 0, ])

                self.mandelbrot.generate_mandelbrot()

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

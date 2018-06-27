import sys

from asciimatics.effects import Cycle, Stars
from asciimatics.event import Event, KeyboardEvent, MouseEvent
from asciimatics.renderers import FigletText
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, Label, Button, TextBox, Widget, Canvas
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication

from lib import read_file_cached

from shapes import mandelbrot_set

KEY_UP = -204
KEY_DOWN = -206
KEY_LEFT = -203
KEY_RIGHT = -205
ARROW_KEYS = [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]


class BetterLabel(Label):
    update_by_default = True

    def set_text_from_list(self, l: list):
        for item in list:
            self.new_line(item)

    def append(self, text):
        # print(self.__dict__)
        self.text = self.text + text

    def new_line(self, text, newl='\n'):
        self.append(text + newl)


class MandelDisplay(BetterLabel):

    def __init__(self, *args, **kwargs):
        super(BetterLabel, self).__init__(*args, **kwargs)

    x = (-1, 1)
    """The x coords to plot."""

    y = (-1, 1)
    """The y coords to plot."""

    dim = (50, 50)
    """ How many units is big our graph?"""

    shading = (-1, 10)
    """How far low and high shall we shade?"""

    shaders = read_file_cached('scale1.txt')[0]
    """What chars to use for shading?"""

    iters = 100
    """How many mandelbrot iterations?"""

    def generate_mandelbrot(self, x=x, y=y, shading=shading, shaders=shaders, iters=iters):
        """Given some parameters, update my view with a pretty fractal!"""

        mandel_set = mandelbrot_set()
        pass


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
                    self.mandelbrot.new_line('UP')

                if event.key_code == KEY_DOWN:
                    self.mandelbrot.new_line('DOWN')

                if event.key_code == KEY_LEFT:
                    self.mandelbrot.new_line('LEFT')

                if event.key_code == KEY_RIGHT:
                    self.mandelbrot.new_line('RIGHT')

                self.update(0)

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

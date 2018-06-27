import sys

from asciimatics.effects import Cycle, Stars
from asciimatics.event import Event, KeyboardEvent, MouseEvent
from asciimatics.renderers import FigletText
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, Label, Button, TextBox, Widget, Canvas
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication

KEY_UP = -204
KEY_DOWN = -206
KEY_LEFT = -203
KEY_RIGHT = -205
ARROW_KEYS = [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]


class BetterLabel(Label):

    def set_text(self, text, update=False):
        self._text = text

        if update:
            self.update(0)

    def append(self, text, update=False):
        # print(self.__dict__)
        self.set_text(self._text + text, update)


class MandelDisplay(BetterLabel):
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
                    self.mandelbrot.append('UP')

                if event.key_code == KEY_DOWN:
                    self.mandelbrot.append('DOWN')

                if event.key_code == KEY_LEFT:
                    self.mandelbrot.append('LEFT')

                if event.key_code == KEY_RIGHT:
                    self.mandelbrot.append('RIGHT')
                    
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

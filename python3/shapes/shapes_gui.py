import sys

from asciimatics.effects import Cycle, Stars
from asciimatics.event import KeyboardEvent
from asciimatics.renderers import FigletText
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, Label, Button, TextBox, Widget
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication

KEY_UP = -204
KEY_DOWN = -206
KEY_LEFT = -203
KEY_RIGHT = -205
ARROW_KEYS = [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]

class MandelDisplay(TextBox):
    def append(self, text):
        return None

class Mandel(Frame):
    def __init__(self, screen: Screen):
        super(Mandel, self).__init__(
            screen, screen.height, screen.width, has_border=False, name="My Form"
        )

        # Create the (very simple) form layout...
        layout = Layout([1, 1, 1, 1], fill_frame=True)
        self.add_layout(layout)
        # self.root.add_widget(Button('OK', self._ok))
        layout.add_widget(Text('hi','there'))
        layout.add_widget(MandelDisplay(10,
                                        label='mandel',
                                        as_string=True))
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
                    pass
                if event.key_code == KEY_DOWN:
                    pass
                if event.key_code == KEY_LEFT:
                    pass
                if event.key_code == KEY_RIGHT:
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

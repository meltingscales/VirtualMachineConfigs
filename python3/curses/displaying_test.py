try:
    import curses
except Exception:
    print("You either are using Windows or don't have 'curses' installed.")
    print("If on windows, run `pip install windows-curses`.")
    print("If on Linux, run `pip install curses`")

from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 9):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)

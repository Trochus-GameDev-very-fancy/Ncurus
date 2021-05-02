# main.py

import curses

from src.layout import Layout
from src.pad import Dialogs, Gallery


def main(win):
    curses.curs_set(0)

    layout = Layout(win)
    gallery = Gallery(layout.create_top_win())
    dialogs = Dialogs(layout.create_bottom_win())

    layout.add_pad(gallery, dialogs)

    while 1:
       layout.routine()
       dialogs.char_by_char("test")


if __name__ == "__main__":
    curses.wrapper(main)

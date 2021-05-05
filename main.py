# main.py

import curses

from src.color import start_colors
from src.img import ANSI, ASCII
from src.layout import Layout
from src.pads import Dialogs, Gallery
from src.type import DialogScript


def main(win):
    curses.curs_set(0)
    start_colors()

    layout = Layout(win)
    top_win, bottom_win = layout.divide_window(4)
    gallery = Gallery(top_win)
    dialogs = Dialogs(bottom_win)

    dialogs.one = dialogs.box_factory("One")
    dialogs.two = dialogs.box_factory("Two")

    script: DialogScript = (
        (ANSI(["42", "0123456", "020"]),
         dialogs.one,
         {"text": "First test", "text_attr": curses.A_BOLD}),
        (...,
         dialogs.two,
         {"text": "Second test"}),
        (...,
         dialogs.one,
         {"text": "Third test"}),
        (ANSI(["36"]),
         dialogs.two,
         {"text": "Fourth test"})
    )

    dialogs.execute_script(script,
                           gallery,
                           before=layout.routine)


if __name__ == "__main__":
    curses.wrapper(main)

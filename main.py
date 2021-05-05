# main.py

import curses

from ncurus.img import ANSI, ASCII
from ncurus.layout import Layout
from ncurus.pads import Dialogs, DialogScript, Gallery
from ncurus.utils import startup


@startup
def main(win):
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

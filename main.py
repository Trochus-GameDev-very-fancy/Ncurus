# main.py

import curses

from src.color import start_colors
from src.img import ANSI, ASCII
from src.layout import Layout
from src.pads import Dialogs, Gallery
from src.type import DialogScript


script: DialogScript = (
    (ANSI(["42", "0123456", "020"]), "test"),
    (..., "second test"),
    (..., "third test"),
    (ANSI(["36"]), "third test")
)


def main(win):
    curses.curs_set(0)
    start_colors()

    layout = Layout(win)
    top_win, bottom_win = layout.divide_window(4)
    gallery = Gallery(top_win)
    dialogs = Dialogs(bottom_win)

    layout.add_pad(gallery, dialogs)

    for img, text in Dialogs.distributor(script):
        layout.routine()
        gallery.show(img)
        gallery.clear()

        dialogs.char_by_char(text)


if __name__ == "__main__":
    curses.wrapper(main)

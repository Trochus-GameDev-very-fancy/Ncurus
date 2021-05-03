# main.py

import curses

from src.color import start_colors
from src.img import ASCII, ANSI
from src.layout import Layout
from src.pads import Dialogs, Gallery


script = [
    (ANSI(["42", "0123456", "020"]), "test"),
]


def main(win):
    curses.curs_set(0)
    start_colors()

    layout = Layout(win)
    gallery = Gallery(layout.create_top_win())
    dialogs = Dialogs(layout.create_bottom_win())

    layout.add_pad(gallery, dialogs)

    for img, text in script:
        layout.routine()
        gallery.show(img)
        gallery.refresh()

        dialogs.char_by_char(text)


if __name__ == "__main__":
    curses.wrapper(main)

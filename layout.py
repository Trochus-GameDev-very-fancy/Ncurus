
import curses
from typing import NoReturn

from more_curses import CursesWin
from visualdialog import DialogBox


ConsoleEffect = NoReturn


class Pad:
    """Encapsulate a pad."""
    def __init__(self, win: CursesWin):
        self.win = win

    def box(self) -> ConsoleEffect:
        self.win.box()

    def clear(self) -> ConsoleEffect:
        self.win.clear()

    def refresh(self) -> ConsoleEffect:
        self.win.refresh()


class Gallery(Pad):
    def __init__(self, win: CursesWin):
        Pad.__init__(self, win)


class DialogZone(Pad):
    def __init__(self, win: CursesWin):
        max_y, max_x = win.getmaxyx()
        start_y =[0] // 2 + 1
        self.win = win.subwin(start_y, 1)


class Layout:

    def __init__(self, *pads: CursesWin):
        self.pads = pads

    def update(self) -> ConsoleEffect:
        for pad in self.pads:
            pad.clear()
            pad.box()
            pad.refresh()


def main(win):
    curses.curs_set(0)

    gallery = Gallery(win)
    dialogs = DialogZone(win)

    layout = Layout(gallery, dialogs)
    textbox = DialogBox(2, 2, 40, 6, "TextBox")

    while 1:
        textbox.char_by_char(dialogs.win, "test")
        layout.update()
        curses.napms(500)


if __name__ == "__main__":
    curses.wrapper(main)


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

    def update(self):
        ...


class Gallery(Pad):
    def __init__(self, win: CursesWin):
        self.win = win


class Dialogs(Pad):
    def __init__(self, win: CursesWin):
        self.win = win
        # self.win.bkgdset("o")

        self.textbox = DialogBox(0, 0, 20, 6, "TextBox")

    def update(self) -> ConsoleEffect:
        self.textbox.char_by_char(self.win, "test")


class Layout:
    """Encapsulate a layout to manage a set of windows more
    efficiently.
    """
    def __init__(self, win: CursesWin):
        side_borders_total_width = 2
        max_y, max_x = win.getmaxyx()

        self.stdscr = win  # Original win.
        self.win: CursesWin = win.subwin(max_y - side_borders_total_width,
                                         max_x - side_borders_total_width,
                                         1, 1)

        self.pads: list = []

    def add_pad(self, *pads: Pad) -> NoReturn:
        """Add given pads to list of pads managed by the layout."""
        for pad in pads:
            self.pads.append(pad)

    def create_bottom_win(self) -> CursesWin:
        max_y, max_x = self.win.getmaxyx()
        half_y = max_y // 2

        return self.win.subwin(half_y, 1)

    def update(self) -> ConsoleEffect:
        self.stdscr.clear()
        self.stdscr.box()
        self.stdscr.refresh()

    def routine(self) -> ConsoleEffect:
        if self.stdscr.is_wintouched():
            self.update()

        for pad in self.pads:
            pad.clear()
            pad.update()
            pad.refresh()


def main(win):
    curses.curs_set(0)

    layout = Layout(win)
    gallery = Gallery(layout.win)
    dialogs = Dialogs(layout.create_bottom_win())

    layout.add_pad(gallery, dialogs)

    while 1:
        layout.routine()


if __name__ == "__main__":
    curses.wrapper(main)

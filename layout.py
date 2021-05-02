
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
        # self.win.bkgdset("t")

    def update(self) -> ConsoleEffect:
        ...


class Dialogs(Pad):
    def __init__(self, win: CursesWin):
        self.win = win
        # self.win.bkgdset("b")

        self.textbox = DialogBox(0, 0, 20, 6, "TextBox")

    def update(self) -> ConsoleEffect:
        self.textbox.char_by_char(self.win, "test")


class Layout:
    """Encapsulate a layout to manage a set of windows more
    efficiently.
    """
    side_borders_total_width = 2

    def __init__(self, win: CursesWin):
        max_y, max_x = win.getmaxyx()

        self.stdscr = win  # Catch original win.
        self.win = win.subwin(max_y - Layout.side_borders_total_width,
                              max_x - Layout.side_borders_total_width,
                              1, 1)

        self.pads = []

    def add_pad(self, *pads: Pad) -> NoReturn:
        """Add given pads to list of pads managed by the layout."""
        for pad in pads:
            self.pads.append(pad)

    def create_top_win(self) -> CursesWin:
        return self.win.subwin(self.half_y,
                               self.max_x,
                               1, 1)

    def create_bottom_win(self) -> CursesWin:
        return self.win.subwin(self.half_y + 2,
                               1)

    @property
    def max_x(self) -> int:
        """Return number of column of windows."""
        return self.win.getmaxyx()[1]

    @property
    def max_y(self) -> int:
        """Return number of line of windows."""
        return self.win.getmaxyx()[0]

    @property
    def half_y(self) -> int:
        """Return half of the total height window."""
        return self.max_y // 2

    def draw_borders(self) -> ConsoleEffect:
        """Draw layout borders."""
        self.stdscr.clear()
        self.stdscr.box()

        # Separation line.
        self.stdscr.hline(self.half_y + 1, 1,
                          "-", self.max_x - 1)

        self.stdscr.refresh()

    def routine(self) -> ConsoleEffect:
        """Clear, call update method and refresh all pad."""
        if self.stdscr.is_wintouched():
            self.draw_borders()

        for pad in self.pads:
            pad.clear()
            pad.update()
            pad.refresh()


def main(win):
    curses.curs_set(0)

    layout = Layout(win)
    gallery = Gallery(layout.create_top_win())
    dialogs = Dialogs(layout.create_bottom_win())

    layout.add_pad(gallery, dialogs)

    while 1:
        layout.routine()


if __name__ == "__main__":
    curses.wrapper(main)

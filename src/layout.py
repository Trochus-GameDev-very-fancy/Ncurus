# layout.py

import curses
from typing import NoReturn

from .pads.pad import Pad
from .type import ConsoleEffect, CursesWin


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

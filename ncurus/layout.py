# layout.py

import curses
from typing import NoReturn, Tuple

from .pads.pad import Pad
from .type import ConsoleEffect, CursesWin


class Layout(Pad):
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

    @property
    def half_y(self) -> int:
        """Return half of the total height window."""
        return self.max_y // 2

    def add_pad(self, *pads: Pad) -> NoReturn:
        """Add given pads to list of pads managed by the layout."""
        for pad in pads:
            self.pads.append(pad)

    def divide_window(self,
                      offsetting_y: int = 0) -> Tuple[CursesWin, CursesWin]:
        """Divide into two halves self.win. Return two curses windows
        object: the first is top window and the second the bottom
        window.

        By default self.win was divided in twohalves of equal height.
        This can be ajustable with offesting_y parameter. A given
        positive integer will enlarge the top window and a negative
        integer will reduce it.
        """
        self.offsetting_y = offsetting_y

        top_win = self.win.subwin(self.half_y + offsetting_y,
                                  self.max_x,
                                  1, 1)
        bottom_win = self.win.subwin(self.half_y + 2 + offsetting_y,
                                     1)

        return top_win, bottom_win

    def draw_borders(self) -> ConsoleEffect:
        """Draw layout borders and separation between windows line."""
        self.stdscr.clear()
        self.stdscr.box()

        # Separation line.
        self.stdscr.hline(self.half_y + 1 + self.offsetting_y,
                          1,
                          "-",
                          self.max_x - 1)

        self.stdscr.refresh()

    def routine(self) -> ConsoleEffect:
        """Clear, call update method and refresh all pad."""
        if self.stdscr.is_wintouched():
            self.draw_borders()

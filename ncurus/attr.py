"""Contains classes related to ``curses`` text attributes management."""

__all__ = ["TextAttributes", "init_colors_pairs"]

import contextlib
from .type import CursesTextAttr, CursesWin


def init_color_pairs() -> None:
    """Initialize all available ``curses`` color pairs.
    
    The following table corresponds to:
    .. list-table:: Number and color correspondence table 
    :widths: 25 25 50
    :header-rows: 1

    * - Number
        - 1
        - 2
        - 3
        - 4
        - 5
        - 6
    * - Curses color
        - Blue
        - Cyan
        - Green
        - Magenta
        - Red
        - Yellow
    """
    curses.init_pair(1, curses.COLOR_BLUE, 0)
    curses.init_pair(2, curses.COLOR_CYAN, 0)
    curses.init_pair(3, curses.COLOR_GREEN, 0)
    curses.init_pair(4, curses.COLOR_MAGENTA, 0)
    curses.init_pair(5, curses.COLOR_RED, 0)
    curses.init_pair(6, curses.COLOR_YELLOW, 0)


class TextAttributes(contextlib.ContextDecorator):
    """A context manager to manage curses text attributes.
    
    :param win: ``curses`` window on which the attributes will be activated.
    :param attributes: ``curses`` text attributes to be activated.
    """
    def __init__(self, win: CursesWin, *attr: CursesTextAttr):
        self.win = win
        self.attributes = attr

    def __enter__(self):
        for attr in self.attributes:
            self.win.attron(attr)

    def __exit__(self, type, value, traceback):
        for attr in self.attributes:
            self.win.attroff(attr)

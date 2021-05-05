# utils.py

import curses
from typing import Callable, NoReturn


def init_color_pairs() -> NoReturn:
    """Initialize all available curses color pairs."""
    curses.init_pair(1, curses.COLOR_BLUE, 0)
    curses.init_pair(2, curses.COLOR_CYAN, 0)
    curses.init_pair(3, curses.COLOR_GREEN, 0)
    curses.init_pair(4, curses.COLOR_MAGENTA, 0)
    curses.init_pair(5, curses.COLOR_RED, 0)
    curses.init_pair(6, curses.COLOR_YELLOW, 0)


def startup(func: Callable, /, *args, **kwargs) -> Callable:
    """Make the cursors invisible and init curses color pairs."""
    def wrapper(*args, **kwargs):
        curses.curs_set(0)
        init_color_pairs()

        return func(*args, **kwargs)

    return wrapper

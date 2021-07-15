"""A curses game engine for my personnal usage."""

import curses
from curses import cbreak, echo, nocbreak, noecho
from typing import Callable, NoReturn

from core import process_scene


def init_color_pairs() -> NoReturn:
    """Initialize all available curses color pairs."""
    curses.init_pair(1, curses.COLOR_BLUE, 0)
    curses.init_pair(2, curses.COLOR_CYAN, 0)
    curses.init_pair(3, curses.COLOR_GREEN, 0)
    curses.init_pair(4, curses.COLOR_MAGENTA, 0)
    curses.init_pair(5, curses.COLOR_RED, 0)
    curses.init_pair(6, curses.COLOR_YELLOW, 0)


def startup(func: Callable) -> Callable:
    """Wrapper function that initializes curses and calls another
    function, restoring normal keyboard/screen behavior on error.
    The callable object 'func' is then passed the main window 'stdscr'
    as its first argument, followed by any other arguments passed to
    wrapper(). Also make cursors invisible and init curses color pairs.
    """
    def wrapper(*args, **kwargs):
        try:
            stdscr = curses.initscr()
            noecho()
            cbreak()
            stdscr.keypad(1)
            curses.curs_set(0)

            try:
                curses.start_color()
                init_color_pairs()
            except:
                pass

            return func(stdscr, *args, **kwargs)
        finally:
            if "stdscr" in locals():
                stdscr.keypad(0)
                echo()
                nocbreak()
                curses.endwin()

    return wrapper

"""A curses game engine for my personnal usage."""

import curses
import sys
from curses import cbreak, echo, nocbreak, noecho
from functools import wraps
from typing import Callable, NoReturn

from .attr import TextAttributes
from .core import process_scene
from .input import iterkey


def startup(smooth_crash: bool = False) -> Callable:
    """A decorator that initializes curses and calls another function,
    restoring normal keyboard/screen behavior on error.
    The callable object ``func`` is then passed the main window
    ``stdscr`` as its first argument, followed by any other arguments
    passed to wrapper().
    Also make cursors invisible and init curses color pairs.

    If smooth_crash is set to ``True``, ignore traceback related to
    ``KeyboardInterrupt``.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
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
            except KeyboardInterrupt:
                sys.exit(1)
            finally:
                if "stdscr" in locals():
                    stdscr.keypad(0)
                    echo()
                    nocbreak()
                    curses.endwin()

        return wrapper
    return decorator

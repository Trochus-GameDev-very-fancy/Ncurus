
import contextlib
from typing import Callable, Container, Iterator, Optional

from .type import CursesInputMethod, CursesKey, CursesTextAttr


def process_scene(scene: Callable) -> Callable:
    """Process scene function and return its result."""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Optional:
            return scene(*func(*args, **kwargs))

        return wrapper
    return decorator


def iterkey(win,
            *,
            exit_keys: Container[CursesKey] = (),
            predicate: Callable[[CursesKey], bool] = lambda key: True,
            method: CursesInputMethod = "getkey") -> Iterator[CursesKey]:
    """Yield key pressed as long as a key contained in exit_keys is not
    pressed.
    """
    yield

    input_method = getattr(win, method)

    while 1:
        key = input_method()

        if key in exit_keys and predicate(key):
            break
        else:
            yield key


class TextAttributes(contextlib.ContextDecorator):
    """A context manager to manage curses text attributes."""

    def __init__(self, win, *attr: CursesTextAttr):
        self.win = win
        self.attributes = attr

    def __enter__(self):
        for attr in self.attributes:
            self.win.attron(attr)

    def __exit__(self, type, value, traceback):
        for attr in self.attributes:
            self.win.attroff(attr)

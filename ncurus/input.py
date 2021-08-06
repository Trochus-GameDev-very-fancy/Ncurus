"""Contains functions related to input management."""

from typing import Callable, Container, Iterator

from .type import CursesInputMethod, CursesKey


def iterkey(win,
            *,
            exit_keys: Container[CursesKey] = (),
            predicate: Callable[[CursesKey], bool] = lambda key: True,
            method: CursesInputMethod = "getkey") -> Iterator[CursesKey]:
    """Yields key pressed as long as a key contained in ``exit_keys`` is not
    pressed.

    :param exit_keys: a container of ``CursesKey`` which ends the input
        detection.
    :param predicate: predicate to validate for the key to be yielded.
    :param method:

    :return: detected key.
    """
    yield

    input_method = getattr(win, method)

    while 1:
        key = input_method()

        if key in exit_keys and predicate(key):
            break
        else:
            yield key

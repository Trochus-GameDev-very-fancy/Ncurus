# type.py

from typing import Iterable, NoReturn, Tuple, Union

import _curses

from .img import BaseImage


CursesWin = _curses.window

CursesTextAttr = int
CursesKey = Union[int, str]

ConsoleEffect = NoReturn

#: A type annotation which represents a dialog : an image with its
#: associated text.
#: Ellispis represent the absence of image.
DialogScript = Iterable[Tuple[Union[BaseImage, Ellipsis], str]]

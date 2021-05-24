
from typing import Iterable, Mapping, NoReturn, Tuple, Union

import _curses
from visualdialog import DialogBox

from .img import BaseImage


CursesWin = _curses.window

CursesTextAttr = int
CursesKey = Union[int, str]

ConsoleEffect = NoReturn

# type.py

from typing import NoReturn, Union

import _curses


CursesWin = _curses.window

CursesTextAttr = int
CursesKey = Union[int, str]

ConsoleEffect = NoReturn

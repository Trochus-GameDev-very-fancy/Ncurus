
from curses import (COLOR_BLACK, COLOR_BLUE, COLOR_CYAN, COLOR_GREEN,
                    COLOR_MAGENTA, COLOR_RED, COLOR_WHITE, COLOR_YELLOW)
from typing import Iterable, Literal, Mapping, NoReturn, Protocol, Tuple, Union

import _curses
from visualdialog import DialogBox

CursesWin = _curses.window

CursesTextAttr = int
CursesKey = Union[int, str]
CursesColor = Literal[COLOR_BLACK,
                      COLOR_BLUE,
                      COLOR_CYAN,
                      COLOR_GREEN,
                      COLOR_MAGENTA,
                      COLOR_RED,
                      COLOR_WHITE,
                      COLOR_YELLOW]

ConsoleEffect = NoReturn

CursesInputMethod = Literal["getch", "getkey", "getwch"]


class WidgetProtocol(Protocol):
    win: CursesWin

    pos_x: int
    pos_y: int
    width: int
    heigth: int

    height_min: int
    width_min: int

    def routine(self) -> ConsoleEffect:
        ...

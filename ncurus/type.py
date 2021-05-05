# type.py

from typing import Iterable, Mapping, NoReturn, Tuple, Union

import _curses
from visualdialog import DialogBox

from .img import BaseImage


CursesWin = _curses.window

CursesTextAttr = int
CursesKey = Union[int, str]

ConsoleEffect = NoReturn

#: Type annotations which represents a dialog script.
#: A dialog always has the following form:
#: An iterable contains:
#: - Image displayed during scrolling of dialog (Ellispis can be passed
#:   and represent the absence of image).
#: - Dialog box object used.
#: - Sequence contains arguments to pass to given dialog box.
DialogLine = Tuple[BaseImage, DialogBox, Mapping]
DialogScript = Iterable[DialogLine]

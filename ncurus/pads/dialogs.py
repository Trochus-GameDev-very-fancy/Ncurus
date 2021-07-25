
from functools import partial

import visualdialog as vd

from ..img import BaseImage
from ..type import ConsoleEffect, CursesWin
from .gallery import Gallery
from .pad import Pad
from .textpad import TextPad


class Dialogs(Pad):
    """An object contains methods related to displaying text management."""

    def __init__(self, win: CursesWin):
        self.win = win

    def make_box(self, *args, **kwargs) -> vd.DialogBox:
        """Return a custom ``visualdialog.DialogBox`` instance. ``args``
        and ``kwargs`` are passed to ``visualdialog.DialogBox``
        constructor.
        """
        box = vd.DialogBox(0, 0,
                           20, 5,
                           global_win=self.win,
                           *args, **kwargs)
        box.cbc = partial(vd.DialogBox.char_by_char, box)

        return box

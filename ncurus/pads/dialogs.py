
from functools import partial

import visualdialog as vd

from ..img import BaseImage
from ..type import ConsoleEffect, CursesWin
from .gallery import Gallery
from .pad import Pad


class Dialogs(Pad):
    """An object contains methods related to DialogBox management."""

    def __init__(self, win: CursesWin):
        self.win = win

    def box_factory(self, *args, **kwargs) -> DialogBox:
        """Return a custom visualdialog.DialogBox instance. args and
        kwargs are passed to visualdialog.DialogBox constructor.
        """
        box = vd.DialogBox(0, 0,
                           20, 4,
                           *args,
                           **kwargs)
        box.cbc = partial(DialogBox.char_by_char,
                          box, win=self.win)

        return box

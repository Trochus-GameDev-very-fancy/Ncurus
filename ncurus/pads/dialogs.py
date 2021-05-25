
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

    def box_factory(self, *args, **kwargs) -> vd.DialogBox:
        """Return a custom visualdialog.DialogBox instance. args and
        kwargs are passed to visualdialog.DialogBox constructor.
        """
        box = vd.DialogBox(0, 0,
                           20, 4,
                           global_win=self.win,
                           *args,
                           **kwargs)
        box.cbc = partial(vd.DialogBox.char_by_char, box)

        return box

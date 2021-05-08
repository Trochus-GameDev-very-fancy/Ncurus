# dialogs.py

from functools import partial

from visualdialog import DialogBox

from ..img import BaseImage
from ..type import ConsoleEffect, CursesWin
from .gallery import Gallery
from .pad import Pad


class Dialogs(Pad):
    def __init__(self, win: CursesWin):
        self.win = win

    def box_factory(self, *args, **kwargs) -> DialogBox:
        """Return a custom DialogBox instance."""
        box = DialogBox(0, 0,
                        20, 4,
                        *args,
                        **kwargs)
        box.cbc = partial(DialogBox.char_by_char,
                          box, self.win)

        return box

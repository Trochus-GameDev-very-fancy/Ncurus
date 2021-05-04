# dialogs.py

from typing import Iterable; Tuple

from visualdialog import DialogBox

from ..img import BaseImage
from ..type import ConsoleEffect, CursesWin, DialogScript
from .pad import Pad


class Dialogs(Pad, DialogBox):
    def __init__(self, win: CursesWin):
        self.win = win
        self.win.bkgdset("b")

        self.textbox = DialogBox(0, 0, 20, 4, "TextBox")

    @staticmethod
    def distributor(script: DialogScript) -> Iterable[Tuple[BaseImage, str]]:
        """Yield a tuple contains an image and its associated text.
        If Ellipsis is given as the first element of a tuple instead of
        an image, the previous image which is not Ellispis is yielded.
        """
        for i, (img, text) in enumerate(script):
            index = i
            while img is Ellipsis:
                img = script[index - 1][0]
                index -= 1

            yield (img, text)

    def char_by_char(self, *args, **kwargs) -> ConsoleEffect:
        self.textbox.char_by_char(self.win, *args, **kwargs)

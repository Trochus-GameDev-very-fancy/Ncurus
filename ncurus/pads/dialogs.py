# dialogs.py

from functools import partial
from typing import Callable, Iterable, Mapping, Tuple

from visualdialog import DialogBox

from ..img import BaseImage
from .gallery import Gallery
from ..type import ConsoleEffect, CursesWin, DialogLine, DialogScript
from .pad import Pad


class Dialogs(Pad):
    def __init__(self, win: CursesWin):
        self.win = win

    def box_factory(self, *args, **kwargs) -> DialogBox:
        box = DialogBox(0, 0,
                        20, 4,
                        *args,
                        **kwargs)
        box.char_by_char = partial(DialogBox.char_by_char, box, self.win)

        return box

    @classmethod
    def distributor(cls,
                    script: DialogScript) -> DialogLine:
        """Yield a tuple contains an image and its associated text.
        If Ellipsis is given as the first element of a tuple instead of
        an image, the previous image which is not Ellispis is yielded.
        """
        img_index = 0
        for i, (img, box, kwargs) in enumerate(script):
            index = i
            while img is Ellipsis:
                img = script[index - 1][img_index]
                index -= 1

            yield (img, box, kwargs)

    def execute_script(self,
                       script: DialogScript,
                       gallery: Gallery,
                       before: Callable = lambda: None,
                       after: Callable = lambda: None) -> ConsoleEffect:
        """"Execute given script: showing image and scrolling text.
        Gallery is object where image are displayed.
        """
        for img, box, kwargs in self.distributor(script):
            before()

            gallery.show(img)
            gallery.clear()
            box.char_by_char(**kwargs)

            after()

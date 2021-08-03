
from curses import A_BOLD

from usage.images import fst_random, snd_random


def execute(gallery, *dialog_boxes):
    one, two, *_ = dialog_boxes

    gallery.show(fst_random)
    gallery.clear()

    one.cbc("First test", text_attr=A_BOLD)

    two < "Second test"

    one < "Third test"

    gallery.show(snd_random)
    gallery.clear()

    two < "Fourth test"

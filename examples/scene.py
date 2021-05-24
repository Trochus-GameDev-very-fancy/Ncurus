
from curses import A_BOLD

from examples.images import fst_random, snd_random


def execute(gallery, *dialog_boxes):
    one, two, *_ = dialog_boxes

    gallery.show(fst_random)
    gallery.clear()

    one.cbc("First test", text_attr=A_BOLD)

    two.cbc("Second test")

    one.cbc("Third test")

    gallery.show(snd_random)
    gallery.clear()

    two.cbc("Fourth test")

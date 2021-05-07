
from curses import A_BOLD

from examples.images import *


def execute(gallery, *dialog_boxes):
    one, two, *_ = dialog_boxes

    gallery.show(first_random)
    gallery.clear()

    one.cbc("one", text_attr=A_BOLD)

    two.cbc("Second test")

    one.cbc("Third test")

    gallery.show(second_random)
    gallery.clear()

    two.cbc("Fourth test")

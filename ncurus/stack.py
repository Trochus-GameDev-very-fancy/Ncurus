
import collections


def bound_check(func):
    """A decorator which raise an error if ``self.maxlen`` was exceeded."""
    def wrapper(self, *args, **kwargs):
        if len(self) == self.maxlen:
            raise IndexError
        else:
            return func(self, *args, **kwargs)

    return wrapper


class Stack(collections.deque):
    """Encapsulate a stack."""

    @bound_check
    def append(self, x):
        return super().append(x)

    @bound_check
    def appendleft(self, x):
        return super().appendleft(x)

"""This module contains implementation of a deque specialised in size
management.
"""

import collections
from typing import Any, Iterable, List, NoReturn, Tuple


class DequeOverflow(Exception):
    """An exception raised when a deque is full."""

    def __str__(self) -> str:
        return "the addition of given object causes exceed of deque size"


class Deque(collections.deque):
    """Encapsulate a deque.

    :param max_percent: An integer represents deque size (it's default
        ``100``).
    """

    def __init__(self, max_percent: int = 100):
        self.slots: List[Tuple[int, Any]] = []
        super().__init__(self.slots)

        self.max_percent = max_percent

    def bound_check(self, percent: int) -> NoReturn:
        """Raises an exception if given percent added don't exceed stack
        ``max_percent``.

        :raise StackOverflow: if addition of given percent exceed space of
            the stack.
        """
        if self.total_percent + percent > self.max_percent:
            raise DequeOverflow

    @property
    def total_percent(self) -> int:
        """Returns the occupied space of the stack."""
        return sum(percent for (percent, _) in self)

    def append(self, x: Any, percent: int) -> None:
        """Add ``x`` taking given percent of space to the right side of the
        deque.
        """
        self.bound_check(percent)
        return super().append((percent, x))

    def appendleft(self, x: Any, percent: int) -> None:
        """Add ``x`` taking given percent of space to the left side of the
        deque.
        """
        self.bound_check(percent)
        return super().appendleft((percent, x))

    def insert(self, i: int, x: object, percent: int) -> None:
        """Insert ``x`` taking given percent of space into the deque at position
        ``i``.
        """
        self.bound_check(percent)
        return super().insert(i, (percent, x))

    def extend(self, iterable: Iterable[Tuple[int, object]]) -> None:
        """Extend the right side of the deque by appending second element of
        the tuple from ``iterable`` taking first element of tuple space
        iterable argument.
        """
        for (percent, _) in iterable:
            self.bound_check(percent)

        return super().extend(iterable)

    def leftextend(self, iterable: Iterable[Tuple[int, object]]) -> None:
        """Extend the left side of the deque by appending second element of the
        tuple from ``iterable`` taking first element of tuple space. Note, the
        series of left appends results in reversing the order of elements in
        the iterable argument.
        """
        for (percent, _) in iterable:
            self.bound_check(percent)

        return super().extend(iterable)


d = Deque()
for i in range(10):
    d.append("ok", 10)
print(d)

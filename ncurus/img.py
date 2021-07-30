
from functools import partialmethod
from typing import (Any, Callable, Iterable, Literal, Protocol, TextIO, Tuple,
                    Union)


class BoolValue(Protocol):
    def __bool__(self) -> bool:
        ...


class BaseImage:
    """An interface for image.

    Initializator takes an iterable of strings or a text mode file in
    parameter.
    """
    sep: str = "---\n"

    def __init__(self, iterable: Union[Iterable[str], TextIO]):
        self.content = self.is_valid(iterable)

        self.width = max(iterable, key=len)
        self.height = len(iterable)

    def __iter__(self) -> Iterable[str]:
        return iter(self.content)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.content[key]
        else:
            return self.content[key.start:key.stop:key.step]

    def is_valid(self,
                 iterable: Iterable[str],
                 key: Callable[[str], BoolValue]) -> Tuple[str]:
        """Return a parsed iterable of string."""
        for index, line in enumerate(iterable):
            for position, char in enumerate(line):
                if not key(char):
                    raise ValueError(f"{char} is not a digit "
                                     f"(line {index}, position {position})")

        return tuple(iterable)

    @classmethod
    def from_path(cls, path: str) -> "BaseImage":
        """Return an image object from content of given file path."""
        content = open(path).read()

        try:
            content = content.split(cls.sep)[1]
        except ValueError:
            raise ValueError("Invalid image format")

        return cls(content.rstrip("\n").split("\n"))


class ANSI(BaseImage):
    """Encapsulate an ANSI image.

    Example of valid format
    -----------------------
    >>> ANSI(["525",
              "313",
              "525"])
    """
    is_valid = partialmethod(BaseImage.is_valid,
                             key=(lambda char: char in "0123456"))


class ASCII(BaseImage):
    """Encapsulate an ASCII image.

    Example of valid format
    -----------------------
    >>> ASCII(["-.-",
               " I ",
               "o o"])
    """
    is_valid = partialmethod(BaseImage.is_valid,
                             key=(lambda char: True))

from typing import TypeVar
from functools import reduce
from collections.abc import Iterable, Iterator, Callable

T = TypeVar("T")
U = TypeVar("U")


class Stream(Iterable[T]):
    """
    
    """


    def __init__(self, iterable: Iterable[T]) -> None:
        self.it = iterable

    def __iter__(self) -> Iterator[T]:
        return iter(self.it)

    def map(self, fn: Callable[[T], U]) -> "Stream[U]":
        """
        >>> Stream([1, 2, 3]).map(lambda x: x + 1).to(list)
        [2, 3, 4]
        """
        return Stream(map(fn, self.it))

    def filter(self, fn: Callable[[T], bool]) -> "Stream[T]":
        """
        >>> Stream([1, 2, 3, 4]).filter(lambda x: x % 2).to(list)
        [1, 3]
        """
        return Stream(filter(fn, self.it))

    def reduce(self, fn: Callable[[U, T], U], initial: U = None) -> T:
        """
        >>> Stream([1, 2, 3]).reduce(lambda x, y: x + y)
        6
        >>> Stream([1, 2, 3]).reduce(lambda x, y: x - y, initial=6)
        0
        """
        if initial is not None:
            return reduce(fn, self.it, initial)
        else:
            return reduce(fn, self.it)

    def foreach(self, fn: Callable[[T], None]) -> None:
        """
        >>> Stream([1, 2, 3]).foreach(print)
        1
        2
        3
        """
        for i in self.it:
            fn(i)

    def to(self, collector: Callable[[Iterable], T]) -> T:
        """
        >>> Stream(range(3)).to(list)
        [0, 1, 2]
        """
        return collector(self.it)

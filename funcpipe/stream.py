from typing import TypeVar
from functools import reduce
from collections.abc import Iterable, Iterator, Callable

T = TypeVar("T")
U = TypeVar("U")


class Stream(Iterable[T]):
    """
    The `Stream` class allows you to chain the functional programming functions together in a "piped" way,
    so that you can write

    ```python
    (Stream(iterable)
        .map(func0)
        .filter(func1)
        .to(list))
    ```

    instead of

    ```python
    list(
        filter(
            func1,
            map(func0, iterable)
        )
    )
    ```
    """

    def __init__(self, iterable: Iterable[T]) -> None:
        self.it = iterable
        """ The internal iterator object"""

    def __iter__(self) -> Iterator[T]:
        """
        Return the iterator of the iterable

        >>> s = Stream([1, 2, 3])
        >>> it = iter(s)
        >>> for i in it:
        ...     print(i)
        1
        2
        3
        """
        return iter(self.it)

    def map(self, fn: Callable[[T], U]) -> "Stream[U]":
        """
        Equivalent to `map(fn, iterable)`

        >>> Stream([1, 2, 3]).map(lambda x: x + 1).to(list)
        [2, 3, 4]
        """
        return Stream(map(fn, self.it))

    def filter(self, fn: Callable[[T], bool]) -> "Stream[T]":
        """
        Equivalent to `filter(fn, iterable)`

        >>> Stream([1, 2, 3, 4]).filter(lambda x: x % 2).to(list)
        [1, 3]
        """
        return Stream(filter(fn, self.it))

    def reduce(self, fn: Callable[[U, T], U], initial: U = None) -> T:
        """
        Equivalent to `functools.reduce(fn, iterable, initial)`

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
        Equivalent to `for i in iterable: fn(i)`

        >>> Stream([1, 2, 3]).foreach(print)
        1
        2
        3
        """
        for i in self.it:
            fn(i)

    def to(self, collector: Callable[[Iterable], T]) -> T:
        """
        Equivalent to `collector(iterable)`

        >>> Stream(range(3)).to(list)
        [0, 1, 2]
        """
        return collector(self.it)

    def zip(self, *others: Iterable[U]) -> "Stream[tuple[T, U]]":
        """
        Equivalent to `zip(iterable, *others)`

        >>> Stream([1, 2, 3]).zip([2, 3, 4]).to(list)
        [(1, 2), (2, 3), (3, 4)]

        >>> Stream([1, 2]).zip([3, 4], [5, 6]).to(list)
        [(1, 3, 5), (2, 4, 6)]
        """
        return Stream(zip(self.it, *others))

    @property
    def star(self):
        """
        The `StarStream` of this iterable, which will unpack the iterable when calling
        `map`, `filter` and `foreach`

        >>> Stream([(1, 2), (3, 4)]).star.map(lambda x, y: x + y).to(list)
        [3, 7]

        This is commonly used for use cases that involves `zip`, for example

        >>> Stream([1, 2]).zip([3, 4]).star.map(lambda x, y: x + y).to(list)
        [4, 6]

        >>> Stream([1, 2]).zip([3, 4]).star.filter(lambda x, y: x + y > 5).to(list)
        [(2, 4)]
        """

        return StarStream(self.it)


class StarStream(Stream[Iterable[T]]):
    """
    A `Stream` that will attempt to unpack each value in the iterable, when applied to a function
    including `map`, `filter` and `foreach`, and returns an original `Stream` after those operations
    """

    def map(self, fn: Callable[[tuple[T, ...]], U]) -> "Stream[U]":
        """
        Equivalent to `map(lambda x: fn(*x), iterable)`,
        or `itertools.starmap(fn, iterable)`

        >>> StarStream([(1, 2), (3, 4)]).map(lambda x, y: x + y).to(list)
        [3, 7]
        """
        return Stream(map(lambda x: fn(*x), self.it))

    def filter(self, fn: Callable[[tuple[T, ...]], bool]) -> "Stream[T]":
        """
        Equivalent to `filter(lambdax: fn(*x), iteable)`

        >>> StarStream([(1, 2), (3, 4)]).filter(lambda x, y: x + y > 5).to(list)
        [(3, 4)]
        """
        return Stream(filter(lambda x: fn(*x), self.it))

    def foreach(self, fn: Callable[[tuple[T, ...]], None]) -> None:
        """
        Equivalent to (following is pseudo code)

        ```python
        for x, y, ... in iterable:
            fn(x, y, ...)
        ```
        """
        Stream(self.it).foreach(lambda x: fn(*x))

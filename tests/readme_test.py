def readme_usage_test():
    """
    >>> from funcpipe import Stream as s
    >>> s([1, 2, 3]).map(lambda x: x + 1).to(list)
    [2, 3, 4]

    >>> s([1, 2, 3]).map(lambda x: x + 1).filter(lambda x: x % 2).to(list)
    [3]

    >>> s([1, 2, 3]).map(lambda x: x + 1).to(set)
    {2, 3, 4}

    >>> (s([1, 2, 3])
    ...     .map(lambda x: x + 1)            # [2, 3, 4]
    ...     .filter(lambda x: x % 2 == 0)    # [2, 4]
    ...     .reduce(lambda x, y: x + y))     # 2 + 4 = 6
    6

    >>> s([1, 2, 3]).foreach(print)
    1
    2
    3
    """

    pass


def readme_star_test():
    """
    >>> from funcpipe import Stream as s

    >>> s([1, 2]).zip([3, 4]).to(list)
    [(1, 3), (2, 4)]

    >>> s([1, 2]).zip([3, 4]).star.foreach(lambda x, y: print(f"{x} + {y}"))
    1 + 3
    2 + 4

    >>> s([1, 2]).zip([3, 4]).star.map(lambda x, y: x + y).to(list)
    [4, 6]

    >>> s([1, 2]).zip([3, 4]).map(lambda x: x[0] + x[1]).to(list)
    [4, 6]
    """


def readme_reusability_test():
    """
    >>> from funcpipe import Stream as s

    >>> obj = [1, 2, 3]
    >>> stream = s(obj)

    >>> stream.map(lambda x: x + 1).to(list)
    [2, 3, 4]

    >>> stream.map(lambda x: x + 1).to(list)
    [2, 3, 4]

    >>> obj = iter(range(1, 4))
    >>> stream = s(obj)

    >>> stream.map(lambda x: x + 1).to(list)
    [2, 3, 4]

    >>> stream.map(lambda x: x + 1).to(list)
    []
    """

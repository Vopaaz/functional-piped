def doctest_helper():
    """
    >>> from dotmap import Stream as s
    >>> s([1, 2, 3]).map(lambda x: x + 1).to(list)
    [2, 3, 4]

    >>> s([1, 2, 3]).map(lambda x: x + 1).filter(lambda x: x % 2).to(list)
    [3]

    >>> s([1, 2, 3]).map(lambda x: x + 1).to(set)
    {2, 3, 4}

    >>> # [1, 2, 3]  ->    [2, 3, 4]        ->          [2, 4]           ->        2 + 4 = 6
    >>> s([1, 2, 3]).map(lambda x: x + 1).filter(lambda x: x % 2 == 0).reduce(lambda x, y: x + y)
    6

    >>> s([1, 2, 3]).foreach(print)
    1
    2
    3
    """

    pass


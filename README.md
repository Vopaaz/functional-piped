# functional-piped

Python has native support for some functional programming functions such as `map` and `filter`.
This library allows you to use them in a "piped" way,
i.e. `s(iterable).map(func)` instead of `map(func, iterable)`,
because in any slightly more complex scenarios, the former is much more readable.

For example,

```python
(s(iterable)
    .map(func0)
    .filter(func1)
    .to(list))
```

makes much more sense than

```python
list(
    filter(
        func1,
        map(func0, iterable)
    )
)
```

## Installation

`pip install functional-piped`

## Usage

```python
>>> from funcpipe import Stream as s
```

Then you can use `.map`, `.filter`, `.reduce`, and `.foreach`
to manipulate your iterable in a functional programming way.
If the result is still an iterable, you can use `.to()` to collect it into any data type

```python
>>> s([1, 2, 3]).map(lambda x: x + 1).to(list)
[2, 3, 4]

>>> s([1, 2, 3]).map(lambda x: x + 1).filter(lambda x: x % 2).to(list)
[2]

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
```

## Iterable Reusability

`s(obj)` behaves exactly the same as `obj` in terms of "reusability" when calling iterator/iterable
related methods.

If `obj` is an iterable, not iterator:

```python
>>> obj = [1, 2, 3]
>>> stream = s(obj)

>>> stream.map(lambda x: x + 1).to(list)
[2, 3, 4]

>>> stream.map(lambda x: x + 1).to(list)
[2, 3, 4]
```

If `obj` is an iterator:

```python
>>> obj = range(1, 4)
>>> stream = s(obj)

>>> stream.map(lambda x: x + 1).to(list)
[2, 3, 4]

>>> stream.map(lambda x: x + 1).to(list)
[]
```





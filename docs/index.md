# functional-piped

![Codecov](https://img.shields.io/codecov/c/github/Vopaaz/functional-piped?style=for-the-badge&token=gOatZaMQ9U)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/functional-piped?style=for-the-badge&)
![PyPI](https://img.shields.io/pypi/v/functional-piped?style=for-the-badge&)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/Vopaaz/functional-piped/CI-master.yml?branch=master&style=for-the-badge)

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

Then you can use `.map`, `.filter`, `.reduce`, `.foreach`, and `.zip`
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


### Using `.zip` and `.star`

One common use case in Python is

```python
a_list = [...]
b_list = [...]

for a, b in zip(a_list, b_list):
    ...
```

To write equivalent code, you can use `s(a_list).zip(b_list)` to zip the two lists together,
and use the `.star` attribute to apply `.foreach` to the unpacked zipped values

```python
>>> s([1, 2]).zip([3, 4]).to(list)
[(1, 3), (2, 4)]

>>> s([1, 2]).zip([3, 4]).star.foreach(lambda x, y: print(f"{x} + {y}"))
1 + 3
2 + 4
```

The same thing applies to map and filter:

```python
>>> s([1, 2]).zip([3, 4]).star.map(lambda x, y: x + y).to(list)
[4, 6]
```

If you don't use `.star`, the callback of each function will receive a tuple:

```python
>>> s([1, 2]).zip([3, 4]).map(lambda x: x[0] + x[1]).to(list)
[4, 6]
```

Naming of `.star` comes from the `itertools.starmap`, but this concept also
applies to `.filter` and `.foreach`, so instead of creating a `.starmap` method for `Stream`, we use the above mentioned syntax there.


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
>>> obj = iter(range(1, 4))
>>> stream = s(obj)

>>> stream.map(lambda x: x + 1).to(list)
[2, 3, 4]

>>> stream.map(lambda x: x + 1).to(list)
[]
```





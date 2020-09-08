"""
Problem Statement:

Given a two dimensional array (a matrix) of distinct integers and a
target integer, return the precise index for which this target lies; otherwise return the array:

```
[-1, 1]
```
"""

from collections.abc import Sequence
from typing import Any, Callable, List


def search_in_sorted_matrix(matrix: List[List[int]], target: int) -> List[int]:
    """Complexity:

        Time -> O(n + m)
        Space -> O(1)
    """
    i, j = 0, len(matrix[0]) - 1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == target:
            return [i, j]

        if target < matrix[i][j]:
            j -= 1
            continue

        i += 1

    return [-1, -1]


# Primitives
Y = lambda le: (lambda f: f(f))(lambda f: le(lambda x: f(f)(x)))
rlen = lambda f: lambda x: 1 + f(x[1:]) if x else 0  # recursive length
head = lambda x: x[0]
tail = lambda x: x[1:]
cons = lambda a: lambda b: [a] + [b]
is_atom = lambda x: not (isinstance(x, Sequence) and not isinstance(x, str))


def napply(n: int, f: Callable, x: Any) -> Any:
    if n == 0:
        return x

    return f(napply(n - 1, f, x))


def coltail(x: List[List[int]]) -> List[List[int]]:
    if len(x) == 0:
        return []

    if not is_atom(head(x)):
        return cons(coltail(head(x)))(coltail(tail(x)))

    if not tail(x):
        return []

    return cons(head(x))(coltail(tail(x)))


def search_in_sorted_matrix_recursive(
    matrix: List[List[int]], target: int
) -> List[int]:
    """
    Complexity:

        T -> O(n^2 + m)  <n^2 due to ``rlen``>
        S -> O(n + m)
    """
    # no multiline lambda in python :(
    def fn(matrix: List[List[int]], i: int, target: int) -> List[int]:
        if len(matrix) == 0:
            return cons(-1)([-1])

        # apply tail ``len(head(matrix)) - 1`` times, and then head
        if head(napply(Y(rlen)(head(matrix)) - 1, tail, head(matrix))) == target:  # NOQA
            return cons(i)([Y(rlen)(head(matrix)) - 1])

        if head(napply(Y(rlen)(head(matrix)) - 1, tail, head(matrix))) > target:  # NOQA
            return fn(
                coltail(matrix), i, target,
            )

        return fn(
            tail(matrix), i+1, target,
        )
    return Y(
        lambda f: lambda x, i, target: fn(matrix, 0, target)
    )(matrix, 0, target)

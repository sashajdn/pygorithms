"""
Problem Statement:

Given a two dimensional array (a matrix) of distinct integers and a
target integer, return the precise index for which this target lies;
otherwise return the array:

```
[-1, 1]
```
"""


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


Y = lambda le: (lambda f: f(f))(lambda f: le(lambda x: f(f)(x)))
rlen = lambda f: lambda x: 1 + f(x[1:]) if x else 0  # recursive length
head = lambda x: x[0]
tail = lambda x: x[1:]
# TODO : make recursive
coltail = lambda x: list(zip(*list(zip(*x))[:-1]))  # column tail
cons = lambda a: lambda b: [a] + [b]


def napply(n: int, f: Callable, x: Any) -> Any:
    # TODO: curry args & use ``Y`` to recurse
    if n == 0:
        return x

    return f(napply(n - 1, f, x))


def search_in_sorted_matrix_recursive(
    matrix: List[List[int]], target: int
) -> List[int]:
    """
    Complexity:

        T -> bad
        S -> bad
    """
    # no multiline lambda in python :(
    def fn(matrix: List[List[int]], i: int, target: int) -> List[int]:
        if len(matrix) == 0:
            return cons(-1)(-1)

        if head(napply(Y(rlen)(head(matrix)) - 1, tail, head(matrix))) == target:  # NOQA
            return cons(i)(Y(rlen)(head(matrix)) - 1)

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

from typing import Union


Int = Union[int, str]


def add(x: str, y: str) -> str:
    """Recursively adds two strings ``x`` & ``y``.

    Complexity:
        Time -> O(max(len(x), len(y))
        Space -> O(max(len(x), len(y))
    """
    if len(y) > len(x):
        return add(y, x)

    if len(x) != len(y):
        return add(x, f"{'0' * (len(x) - len(y))}{y}")

    if len(x) == 1:
        return str(int(x) + int(y))

    if int(x[-1]) + int(y[-1]) > 10:
        return (
            add(str(int(x[:-1]) + 1), y[:-1]) +
            str(((int(x[-1]) + int(y[-1])) % 10))
        )

    return (
        add(
            add(x[:-1], y[:-1]),
            str(int(x[-1]) + int(y[-1]))
        )
    )


def karatsuba(x: Int, y: Int) -> int:
    """ Takes in two integers and multiplies them.

    Assumes len(x) == len(y), and len(x) % 2 == 0

    Complexity:
        Time -> O(x)
        Space -> O(x)
    """
    if isinstance(x, int):
        return karatsuba(str(x), y)

    if isinstance(y, int):
        return karatsuba(x, str(y))

    if len(y) > len(x):
        return karatsuba(y, x)

    if len(x) != len(y):
        # attempt algorithm, will most likely fail
        return karatsuba(x, f"{'0' * (len(x) - len(y))}{y}")

    if len(x) == 1:
        return int(x) * int(y)

    a, b = x[:int(len(x) / 2)], x[int(len(x) / 2):]
    c, d = y[:int(len(y) / 2)], y[int(len(y) / 2):]

    p, q = add(a, b), add(c, d)
    ac, bd, pq = karatsuba(a, c), karatsuba(b, d), karatsuba(p, q)
    adbc = pq - ac - bd

    return int((pow(10, len(x)) * ac) + (pow(10, len(x) / 2) * adbc) + bd)

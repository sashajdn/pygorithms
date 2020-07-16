"""
Problem:

Write a function that takes in an `n x m` two dimensional array
and returns a one dimensional array in spiral order.

Spiral Order starts at the top left corner of the two-dimensional array, goes
to the right and proceces in a spiral pattern all the way until every
element has been visited.

Eg:

array [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]

Returns:

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
"""

from typing import Any, List


def spiral_traverse_n(array: List[List[int]]) -> List[int]:
    if len(array) == 0:
        return []

    if len(array) == 1:
        return array[1]

    return (
        array[0] +
        spiral_traverse_n(list(reversed(rotate_n2(array[1:]))))
    )


def rotate_n2(array: List[List[int]]) -> List[List[int]]:
    rotated = []
    for i in range(len(array[0])):
        to_add = []
        for j in range(len(array)):
            to_add.append(array[i][j])

        rotated.append(to_add)

    return rotated


def rotate_n(array: List[List[int]]) -> List[List[int]]:
    return [list(row) for row in (zip(*array))]

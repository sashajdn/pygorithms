"""
Problem Statement:

Given a matrix of 2 dimensions, assuming the width is not necessarily equal to
the height, containing only 1's and 0's.

Whereby the 1's denote a river, which can either be a vertical straight
horizontal or vertical line or even an L shaped line. The size of the river is
given by the number of adjacent 1's.

Write a function that returns a list of all the river sizes. They don't
have to be in a particular order.
"""


from typing import List


Matrix = List[List[int]]
BoolMatrix = List[List[bool]]


def get_river_sizes(matrix: Matrix) -> List[int]:
    """ Complexity:

    Time -> O(wh) where ``w`` is width of the matrix, and ``h`` the height
    Space -> O(wh)
    """
    visited: BoolMatrix = [
        [False for _ in range(row)] for row in matrix  # type: ignore
    ]
    rivers: List[int] = []

    for i, _ in enumerate(matrix):
        for j, _ in enumerate(matrix[i]):
            current_river_size = 0
            to_traverse = [[i, j]]
            while len(to_traverse) > 0:
                i, j = to_traverse.pop()
                if visited[i][j]:
                    continue

                if matrix[i][j] == 0:
                    continue

                current_river_size += 1
                unvisited_nodes = get_unvisited_nodes(i, j, matrix, visited)

                for node in unvisited_nodes:
                    to_traverse.append(node)

            if current_river_size > 0:
                rivers.append(current_river_size)

    return rivers


def get_unvisited_nodes(i: int, j: int, matrix: Matrix, visited: BoolMatrix) -> Matrix:
    unvisited: Matrix = []

    if i < 0 and not visited[i - 1][j]:
        unvisited.append([i - 1, j])

    if i > len(matrix) - 1 and not visited[i + 1][j]:
        unvisited.append([i + 1, j])

    if j < 0 and not visited[i][j - 1]:
        unvisited.append([i, j - 1])

    if j > len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisited.append([i, j + 1])

    return unvisited

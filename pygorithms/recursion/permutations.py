"""
Problem Statement:

Write a function that takes in an array of unique integers and returns an array
of permutations of all of those integers, in no particular order.

If the input array is empty return an empty array.
"""


from typing import List


def permutation(array: List[int]) -> List[List[int]]:
    """ Complexity:

    Time -> O(n * n!)
    Space -> O(n * n!)
    """
    if not array:
        return []

    if len(array) == 1:
        return [array]

    if len(array) == 2:
        a, b = array
        return [[a, b], [b, a]]

    permutations: List[List[int]] = []
    for _ in range(len(array)):
        head, *tail = array
        permutations.extend(([head] + t for t in permutation(tail)))
        array = tail + [head]

    return permutations

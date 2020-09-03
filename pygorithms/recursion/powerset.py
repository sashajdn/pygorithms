"""
Problem Statement:

Write a function that takes in an array of unique integers and returns
the powerset.

The powerset of P(x) is the set of all subsets of ``x``.

Ordering does not matter.
"""


from typing import List


def powerset(array: List[int]) -> List[List[int]]:
    """ Complexity:

    Time -> O(n * 2^n)
    Space -> O(n * 2^n)
    """
    ps: List[List[int]] = [[]]

    for i in array:
        for j in range(len(ps)):
            ps.append(ps[j] + [i])

    return ps

"""
Problem:

Given an array of distinct positive integers, representing coin denominations,
and a single non-negative integer ``n`` representing a target amount. Write a function
that returns the number of ways to make change for that target amount, using
the given coin denominations.

NOTE: An unlimited amount of coins can be used.
"""

from typing import List


def number_of_ways_to_make_change(denominations: List, n: int) -> int:
    """
    Complexity:

    Time: O(nd)  - where n is the target amount, d the number of denominations
    Space: O(n)
    """
    ways = [1] + [0 for _ in range(n)]

    for denomination in denominations:
        for amount in range(1, n + 1):
            if denomination <= amount:
                ways[amount] += ways[amount-denomination]

    return ways[n]

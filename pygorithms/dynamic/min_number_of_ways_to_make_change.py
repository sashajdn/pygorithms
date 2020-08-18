"""
Problem Statement:

Given an array of positive integers representing coin denominations and a single
non-negative integer `n` representing a target amount of money, write a function
that returns the smallest number of coins needed to make change for the
target amount.

If it's impossible to make change return -1
"""
from typing import List, Union


def min_number_of_coins_to_make_change(n: int, denoms: List[int]) -> int:
    """Complexity:
    Time:
        O(n): nd

    Space:
        O(n): n
    """
    arr = [0] + [float("inf")] * n
    for d in denoms:
        for i in range(len(arr)):
            if i >= d:
                arr[i] = min(arr[i], arr[i - d] + 1)

    return arr[n] if arr[n] != float("inf") else -1

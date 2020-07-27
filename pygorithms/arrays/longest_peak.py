"""
Problem:

Write a function that takes in an array of integers an returns the length of the
longest peak.

A peak must be at least length 3, and a peak is defined as:

Adjacent integers that are strictly increasing until they reach a tip, at which
point they become strictly decreasing.

eg
[1, 4, 4, 2] is not a peak, but
[1, 4, 2, 1] is a peak
"""

from typing import List


def longest_peak(array: List) -> int:
    """
    Complexity:

    Time:  O(n)
    Space: O(1)
    """
    longest_so_far = 0
    i = 1
    while i <  len(array):
        lidx, ridx = i - 1, i + 1
        if not (array[lidx] < array[i] and array[ridx] < array[i]):
            i += 1
            continue

        # peak
        while lidx >= 0 and array[lidx - 1] < array[lidx]:
            lidx -= 1

        while ridx < len(array) - 1 and array[ridx + 1] < array[ridx]:
            ridx += 1

        longest_so_far = max(longest_so_far, ridx - lidx + 1)
        i = ridx

    return longest_so_far

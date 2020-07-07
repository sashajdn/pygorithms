"""
Problem: Validate Subsequences.

Given two non-empty arrays of integers, write a function that determines
whether the second array is a subsequence of the first.

The definition of a subsquence is, if the array contains the subsequence
in order, but not necessarily consecutively.

Example:

array = [ 1, 6, 7, -1, 12, 14]
sequence = [ 1, -1, 14]

This returns `True`
"""


def is_validate_subsequence(array, sequence) -> bool:
    """
    Complexity:

    Time: O(n)
    Space: O(n) since adding `n` recursive stack calls
    """
    if len(sequence) == 0:
        return True

    if len(array) == 0:
        return False

    if array[0] == sequence[0]:
        return is_validate_subsequence(array[1:], sequence[1:])

    return is_validate_subsequence(array[1:], sequence)

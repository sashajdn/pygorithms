"""Problem Statement:

Palidrome Check:

Write a function that takes in an non-empty string and that returns a boolean representing
whether the string is a Palidrome or not.
"""


def is_palindrome(string):
    """Is palidrome check."""

    def check(lidx, ridx):
        if lidx < 0 or ridx > len(string):
            return True

        if string[lidx] != string[ridx]:
            return False

        return check(lidx-1, ridx+1)

    mid = len(string) // 2
    if len(string) % 2 == 0:
        return check(mid-1, mid)

    return check(mid-1, mid+1)

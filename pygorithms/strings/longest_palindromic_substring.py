"""
Problem Statement:

Write a function to find the longest palindrominc substring.
"""


from typing import List


def longest_palindromic_substring(string: str) -> str:
    current_longest: List[int] = [0, 1]
    check = lambda x: x[1] - x[0]  # NOQA

    for i in range(len(string)):
        odd = get_longest_palindrome(string=string, left=i-1, right=i+1)
        even = get_longest_palindrome(string=string, left=i-1, right=i)

        current_longest = max(
            odd,
            even,
            current_longest,
            key=check
        )

    return string[current_longest[0]:current_longest[1]]


def get_longest_palindrome(
    string: str, left: int, right: int
) -> List[int]:

    while left >= 0 and right <= len(string):
        if string[left] != string[right]:
            break

        left -= 1
        right += 1

    return [left - 1, right]

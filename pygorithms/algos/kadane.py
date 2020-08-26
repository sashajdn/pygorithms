"""
Problem Statement:

Write a function that takes in a non-empty array of integers and returns the max
sum that can be obtained by summing up all of the integers in a non-empty array.

A subarray must only contain adjacent numbers.
"""


from typing import List, Union


Int = Union[int, float]  # Int since impossible to return float


def kadanes_algorithm(array: List[int]) -> Int:
    sum_so_far = 0
    max_so_far: Int = float("-inf")

    for n in array:
        sum_so_far = max(
            sum_so_far + n,
            n,
        )
        max_so_far = max(
            sum_so_far,
            max_so_far,
        )

    return max_so_far

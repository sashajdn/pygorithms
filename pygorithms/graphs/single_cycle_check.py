"""
Problem Statement:

Given an array of integers where each integer represents a jump of it's value in the
array. Where 2 represents a jump of `2` steps forwards and `-2` represents a 2 steps
backwards.

If a jump spills past the bounds of an array; then the jump wraps around the array.

Write a function that returns a boolean value representing whether or not the jumps
in the array form a single cycle.

A single cycle occurs if, starting at any index in the array and following the jumps,
every element in the arra is visited exactly once before landing back on the
starting index.
"""


from typing import List, Set


def has_single_cycle(array: List[int]) -> bool:  # type: ignore
    """ Complexity:

    Time:
        O(n)

    Space:
        O(1)
    """
    counter, start_index, current_index = 0, 0, 0

    while counter < len(array) + 1:
        if 0 < counter < len(array) and current_index == 0:
            return False

        if counter == len(array):
            return current_index == start_index

        counter += 1
        to_jump = array[current_index]
        to_jump_idx = (current_index + to_jump) % len(array)
        current_index = to_jump_idx
        continue

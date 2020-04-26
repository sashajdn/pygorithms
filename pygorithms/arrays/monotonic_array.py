"""
Problem Statement:

Write a function that takes in an array of integers and returns a boolean
representing whether the array is monotonic.

An array is said to be monotonic iff it's elements from right to left are
entirely non-increasing or entirely non-decreasing
"""


import operator


head = lambda x: x[0]
tail = lambda x: x[1:]
is_null = lambda x: len(x) == 0


def is_monotonic(array):
    if len(array) < 2:
        return True

    if operator.eq(head(array), head(tail(array))):
        return is_monotonic(tail(array))

    def compute(array, _operator):
        if is_null(tail(array)):
            return True

        return (
            _operator(head(array), head(tail(array))) and
            compute(tail(array), _operator)
        )

    if operator.le(head(array), head(tail(array))):
        return compute(tail(array), operator.le)

    return compute(array, operator.ge)

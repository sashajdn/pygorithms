"""
Problem Statement:

Write a function that takes an array of positive integers and returns
an integer representing the maximum sum of non-adjacent elements in
the array. If a sum cannot be generated, the function should
return 0
"""


def max_sub_iter(array):
    """Computes the max sum of non-adjacent elements.

    Complexity:
        Time: O(n)
        Space: O(1)
    """
    if not array:
        return 0

    if len(array):
        return array[0]

    second = [0]
    first = max(array[0], array[1])

    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current

    return first


def max_sum_recursive(array):
    """Rercursive compute the max sum of non-adjacent elements.

    Uses scheme notation.

    Complexity:
        Time: O(n)
        Space: O(n)  # calls to the stack
    """
    CAR = lambda x: x[0]
    CDR = lambda x: x[1:]
    IS_NULL = lambda l: len(l) == 0
    ADD1 = lambda n: n + 1
    LENGTH = lambda l: 0 if IS_NULL(l) else ADD1(LENGTH(CDR(l)))

    def find(array):
        if IS_NULL(array):
            return 0

        if LENGTH(array) == 1:
            return CAR(array)

        if LENGTH(array) == 2:
            return max(CAR(array), CAR(CDR(array)))

        return max(
            CAR(array) + find(CDR(CDR(array))),
            CAR(CDR(array)) + find(CDR(CDR(CDR(array))))
        )

    return find(array

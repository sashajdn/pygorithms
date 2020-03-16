"""Problem Statement:

Write a function that takes in a sorted array of integers as well as a target integer.
The function should use binary search to find if the target number is in
the array and return it's index, else return -1.
"""


def binary_search_iter(arrary, target):
    """Binary Search algo.

    Complexity:
       Time: O(logn)
       Space: O(1)
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle

        if array[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1


def binary_search_recursively(arrary, target):
    """Binary Search algo.

    Complexity:
       Time: O(logn)
       Space: O(logn)  ## Since logn recursive applications to the stack
    """

    def search(array, target, left, right):
        """Searches the `array` for `target`."""
        if left >= right:
            return -1

        middle = (right + left) // 2
        if array[middle] == target:
            return middle

        if array[middle] <= target:
            return search(array, target, middle + 1, right)

        return search(array, target, left, middle-1)

    return search(array, target, 0 , (len(array) - 1))

"""Problem Statement:

Write a function to perform the insertion sort algorithm on an array.

Process:
    Iterate through the array. Check if the current item is less than the
    previous item, if true enter another loop and keep swapping until the
    this is false or the loop reaches the beginning of the the array.
"""


def swap_with_prev(idx, array):
    """Swaps element at index: `idx` with `idx-1` for the `array`."""
    array[idx], array[idx-1] = array[idx-1], array[idx]


def insertion_sort(array):
    """Insertion Sort algorithm.

    Complexity:
        Time: O(n^2)
        Space: O(1)  ## inplace
    """
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap_with_prev(j, array)
            j -= 1

    return array

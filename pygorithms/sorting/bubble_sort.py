"""Problem Statement:

Implement the `Bubble Sort` Algorithm.

Process:
Iterate through the list, check if i and i + 1 are sorted.
"""


def swap(idx, arr):
    """Swaps the idxth and idxth + 1 element of `arr`.

    Complexity:
       Time: O(1)
       Space: O(1)
    """
    arr[idx], arr[idx+1] = arr[idx+1] , arr[idx]


def bubble_sort_iter(array):
    """Bubble sort.

    Complexity:
       Time: O(n^2)  Worst & Average
       Space: O(1)
    """
    _sorted = False
    counter = 0
    while not _sorted:
        _sorted = True
        counter += 1

        for idx in range(len(arr) - 1 - counter):
            if arr[idx] <= arr[idx+1]:
                continue

            swap(idx, array)
            _sorted = False

    return array


def bubble_sort_recursive(array):
    """Recursive bubble sort.

    Complexity:
       Time: O(n^2)  Worst & Average
       Space: O(1)
    """
    for idx in range(len(arr) - 1):
        if arr[idx] <= arr[idx+1]:
            continue

        swap(idx, array)
        bubble_sort_recursive(array)

    return array

"""Problem Statment:

Write a function that takes an array of integers and returns a sorted array of the
three largest integers in the input array. Note that the function should return
duplicate integers if necessary; for example, it should return  [10, 10, 12]
for an input array of [10, 10, 12].
"""


def find_three_largest_numbers(array):
    """Finds the three largest numbers.

    Complexity:
       Time: O(n)
       Space: O(1)
    """
    max_arr = [float("-inf")]*3

    for val in array:
        if val > max_arr[0]:
            insert_and_sort(val, max_arr)

    return max_arr


def insert_and_sort(value, arr):
    """Assumes that the value is greater that the first element of `arr`."""
    arr[0] = value
    for idx in range(len(arr) - 1):
        if arr[idx] > arr[idx + 1]:
            tmp = arr[idx + 1]
            arr[idx + 1] = arr[idx]
            arr[idx] = tmp

    return arr


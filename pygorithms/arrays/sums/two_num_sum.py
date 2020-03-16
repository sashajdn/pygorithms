"""Problem Statement:

Write a function that takes a non-empty array of distinct integers and an integer
representing a target sum. If any two numbers in the input array sum up to the
target array, return them in an array. Else return an empty array.
Assume there will be at most one pair of numbers summing up to the
target array.
"""


def two_num_sum_intersection(arr,  target):
    """Returns the 2 num sum, (if + arri arrj) == `target`.

    Uses the intersection the difference of the target with arr(i) and arr

    Complexity:
        T: O(N)
        S: O(N)
    """
    return list({(target - num) for num in arr} & set(arr)})



def two_num_sum_sorted(arr, target):
    """Returns the 2 num sum, (if + arri arrj) == `target`.

    Sorts the array and uses Binary search to find a potential match.

    Complexity:
        T: O(nlogn)
        S: O(1)
    """
    arr.sort()  # bad python,  be we want O(1) Space.
    def _find(arr, target):
        if len(arr) == 0:
            return arr

        curr = arr[0] + arr[-1]
        if curr == target:
            return [arr[0], arr[-1]]

        if curr < target:
            return _find(arr[1:], target)

        return _find(arr[:-1], target)

    return _find(arr, target)

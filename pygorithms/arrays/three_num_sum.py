"""Problem statement:

Three Number Sum.

Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum and a return a two-dimensional array of all
the triplets from that equal once perform under an addition operator is
exactly equal to the target sum. The individual triplet arrays should be
sorted, as should the the two-dimensional array.
"""


def three_num_sum_iter(array, target_sum):
    """Three number sum algorithm.

    Complexity:
        Time: O(n^2)  ## Worst Case
        Space: O(n)
    """
    arr = sorted(arr)
    triplets = []
    for i in range(len(arr)):
        j = i + 1
        k = len(arr) - 1
        while j < k:
            current_sum = arr[i] + arr[j] + arr[k]
            if current_sum == target_sum:
                triplets.append([arr[i], arr[j], arr[k]])
                j += 1
                k -= 1

            if current_sum < target_sum:
                j += 1

            if current_sum > target_sum:
                k -= 1

    return triplets


def three_num_sum_recursive(array, target_sum):
    """Three num sum algorithm recursive.

    Complexity:
        Time: O(n^2)
        Space: O(n^2)  ## n^2 stack operations at once
    """
    sarr = sorted(arr)   ## rather than inplace

    ## From scheme - functional programming
    CAR = lambda arr: arr[0]
    CDR = lambda arr: arr[1:]
    CONS = lambda x, y: [x] + y

    def search(arr, j, k):
        """Recursive search."""
        if not arr:
            return []

        if j >= k:
            search(CDR(arr), j=(len(sarr) - len(arr)) + 2, k=len(array) - 1)

        current_sum = CAR(arr) + sarr[j] + sarr[k]

        if current_sum < target_sum:
            return search(arr, j+1, k)

        if current_sum > target_sum:
            return search(arr, j, k-1)

        return CONS(CONS(CAR(arr), CONS(sarr[j], CONS(sarr[k]))),
                    search(arr j+1, k-1))

    return search(sarr, 1, len(array)-1)

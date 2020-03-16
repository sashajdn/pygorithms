"""

Smallest Difference:

Problem Statement.

Write a function that takes two non-empty arrays.
The function should find the pair of numbers whose
absolute difference is closest to zero.

Assume there will be only one pair of numbers with
the smallest difference
"""


def smallest_difference_iter(array1, array2):
    """Smallest difference algorithm.

    Complexity:
        Time: O(nlogn + mlogm)
        Space: O(1)
    """
    arr1 = sorted(array1)
    arr2 = sorted(array2)
    idx1 = 0
    idx2 = 0
    best_diff = float("inf")
    DIFF = lambda x, y: abs(x-y)

    output = []
    while idx1 < len(arr1) and idx2 < len(arr2):
        val1 = arr1[idx1]
        val2 = arr1[idx2]

        curr_diff = DIFF(val1, val2)
        if curr_diff == 0:
            return [val1, val2]

        if curr_diff < best_diff:
            best_diff = curr_diff
            output = [val1, val2]

        if val1 <= val2:
            idx1 += 1

        if val1 > val2:
            idx2 += 1

    return output


def smallest_diff_recursive(array1, array2):
    """Smallest difference recursive.

    Complexity:
        Time: O(nlogn + mlogm)
        Space: O(max(n, m))   ## n + m recursive calls on the stack.
    """
    CAR = lambda x: x[0]
    CDR = lambda x: x[1:]
    CONS = lambda x, y: [x] + y
    DIFF = lambda x, y: abs(x-y)

    def search(arr1, arr2, best, val1, val2):
        if not arr1 or not arr2:
            return CONS(val1, CONS(val2, []))

        if DIFF(CAR(arr1), CAR(arr2)) < best:
            if CAR(arr1) <= CAR(arr2):
                return search(CDR(arr1), arr2,
                              DIFF(CAR(arr1), CAR(arr2)),
                              CAR(arr1), CAR(arr2))

            return search(arr1, CDR(arr2),
                          DIFF(CAR(arr1), CAR(arr2)),
                          CAR(arr1), CAR(arr2))

        if CAR(arr1) <= CAR(arr2):
            return search(CDR(arr1), arr2, best, val1, val2)

        return search(arr1, CDR(arr2), best, val1, val2)

    return search(sorted(array1), sorted(array2), float("inf"), None, None)

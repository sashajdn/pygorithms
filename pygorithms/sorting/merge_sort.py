from typing import List


def merge_sort(array: List[int]) -> List[int]:
    """ Complexity:

    Time -> O(nlogn)
    Space -> O(nlogn)
    """
    if len(array) < 2:
        return array

    return (
        merge(
            merge_sort(array[:len(array) // 2]),
            merge_sort(array[len(array) // 2:])
        )
    )


def merge(a: List[int], b: List[int]) -> List[int]:
    """ Complexity:

    Time -> O(n)
    Space -> O(nlogn)
    """
    if len(b) == 0:
        return a

    if len(a) == 0:
        return b

    if a[0] < b[0]:
        return a[0:1] + merge(a[1:], b)

    return b[0:1] + merge(a, b[1:])

"""Problem statement:

Move element to end.

You are given an array of integers and an integer. Write a function that moves all
instances of that integer in the array to the end of the array. The function should perform
this is in place and does not need to maintain the order of the other integers
"""


def move_element_to_end_iter(array, to_move):
    """Iterative.

    Complexity:
        Time: O(n)
        Space: O(1)
    """
    i, j = 0, len(array) - 1

    while i < j:
        while i < j and array[j] == to_move:
            j -= 1

        array[i], array[j] = array[j], array[i]
        i += 1

    return array


def move_element_to_end_iter(array, to_move):
    """Recursive.

    Complexity:
        Time: O(n)
        Space: O(n)  ## not in place and ``n`` calls on the stack
    """

    CONS = lambda x, y: [x] + y
    CAR = lambda x: x[0]
    CDR = lambda x: x[1:]

    def move(array, hit, col):
        """Recursive move.

        Collector:
        ''col'' is the collector function, it collects
        both ``hits`` and ``misses`` into separate lists
        The initial `collector` func `decides` what to do
        with the two lists once the array is empty
        """

        if not array:
            return col([], [])

        if CAR(array) == hit:
            return move(CDR(array), hit,
                        lambda misses, hits:
                        col(misses, CONS(CAR(array), hits)))

        return move(CDR(array), hit,
                    lambda misses, hits:
                    col(CONS(CAR(array), misses),
                        hits))

    return move(array, to_move, lambda x, y: x+y)


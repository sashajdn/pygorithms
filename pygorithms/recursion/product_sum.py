"""Problem Statement:

Write a function that takes in a special array and returns it's product sum.
A "special" array is a non-empty array that contains either integers or
other "special" arrays.

The product sum of a "special" array is the sum of it's elements, where special
arrays inside should be multiplied be multiplied by their depth.

E.G: [x, [y, z]]  --> x + 2y + 2z
"""


def product_sum_iter(array, multiplier=1):
    """Calcs product sum iteratively.

    Complexity:
        Time: O(n)
        Space: O(d)  **Where `d` is the max `depth`
    """
    _sum = 0
    for element in array:
        if type(element) is list:
            _sum += product_sum_iter(element, multiplier+1)
        else:
            _sum += element

    return _sum * multiplier


def product_sum_recursive(array):
    """Calcs the product sum.

    Complexity:
       Time: O(n+d)  **Where `d` is the largest `depth`.
       Space: O(1)
    """
    CAR = lambda x: x[0]
    CDR = lambda x: x[1:]
    ADD = lambda x, y: x + y   # Could use recursive add & mult here
    MULT = lambda x, y: x * y

    def calc(array, depth):
        """Recursive algorithm to calc the product sum."""
        if not array:
            return 0

        if isinstance(CAR(array), int):
            return ADD(CAR(array),  calc(CDR(array), depth))

        return ADD(MULT(depth+1, calc(CAR(array), depth+1))), calc(CDR(array), depth))

    return calc(array, depth=1)

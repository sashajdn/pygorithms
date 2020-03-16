"""Problem Statement:

Write a function that takes in a BT and returns a list of branch sums (ordered from the left most ->
right most).
A branch sum is the sum of all values in a BT branch. A branch is path of nodes in a tree
that starts at the root and ends up at a leaf node.
"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sum_brute(tree):
    """Branch sum func."""

    sums = []

    def calc(node, running_sum, sums):
        """calculates the branch sum."""
        if node is None:
            return

        new_sum = running_sum + node.value
        if node.left is None and node.right is None:
            sums.append(new_sum)
            return

        calc(node.left, new_sum, sums)
        calc(node.right, new_sum, sums)

    calc(tree, 0,  sums)
    return sums


def branch_sum_recursive(tree):
    """Branch sum recursive."""
    ADD = lambda x, y: x + y
    CONS = lambda x, y: [x] + y

    def calc(node, run_sum):
        """Calculates the branch sum.

        This returns in the format [[[[a], b], c], d]
        TODO: Figure how to flatten the list.
        """
        if node is None:
            return run_sum

        if node.left is not None and node.right is not None:
            return CONS(calc(node.left, ADD(node.value, run_sum)),
                        calc(node.right, ADD(node.value, run_sum)))

        if node.left is None:
            return calc(node.right, ADD(node.value, run_sum))

        if node.right is None:
            return calc(node.right, ADD(node.value, run_sum))

    return calc(tree, run_sum=0)

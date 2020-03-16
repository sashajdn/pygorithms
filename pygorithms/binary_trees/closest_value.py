"""Problem Statement:

Find the closest value in a BST.

Given  a Binary Search Tree data structure consisting of BST Nodes. Each BST node has an integer value stored
in a property named `value` and left and right child stored in `left` and `right` respectively.
Assume the BST adheres to the BST property: it's values are strictly greater that those to the left of itself
whilst smaller than those to the left.

Given a target value, find the closest value.
"""


class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """Inserts value into BST structure."""
        if value < self.value:
            if self.left is None:
                self.left = self._build_node(value)
                return self.left

            return self.left.insert(value=value)

        if self.right is None:
            self.right = self._build_node(value)
            return self.right

        return self.right.insert(value=value)

    def _build(self, value):
        """Builds a node."""
        return self.__class__(value=value)


def find_closest_value_brute(tree,  target):
    """Find the closest value."""
    head = tree
    DIFF = lambda x, y: abs(x - y)

    def _find(curr_node, prev_diff, prev_node, target):
        if current_node is None or prev_diff == 0:
            return prev_node, prev_diff

        curr_diff = DIFF(curr_node.value, target)
        if curr_diff > prev_diff:
            return prev_node, prev_diff

        if target < curr_node.value:
            return _find(curr_node.left, curr_diff, curr_node,  target)

        return _find(curr_node.right, curr_diff, curr_node, target)

    return _find(head, DIFF(head.value, target), head, target)

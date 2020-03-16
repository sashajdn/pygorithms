"""Problem Statement.

Validate BST:

You are given a Binary Tree data structure consisting of Binary Tree
Nodes. Each Binary Tree node has an interger value stored in a
property called "value" anc two children nodes stored in properties:
"left", "right", respectively. Children nodes can either be Binary Tree
nodes themselves or the None (null) value.

Write a function that returns a boolean representiung whether or not
it is a valid BST.

A node is said to be a BST node iff (if and only if) it satifies the
BST property: it's value is strictly greater that the values of every
nodes to the left and greater or equal to every node to the right.
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """Insert `value` into BST.
        """
        if value < self.value:
            if self.left is None:
                self.left = self.__class__(value=value)
                return self.left

            return self.left.insert(value=value)

        if self.right is None:
            self.right = self.__class__(value=value)
            return self.right

        return self.right.insert(value=value)


def validate_bst(tree):
    """Validate BST, return False if not, else True.
    """

    AND = lambda a, b: a and b

    def validate(tree, mx, mn):
        if tree is None:
            return True

        if tree.value >= mx or tree.value < mn:
            return False

        return AND(validate(tree.left, tree.value, mn),
                   validate(tree.right, mx, tree.value))

    return validate(tree, float("inf"), float("-inf"))

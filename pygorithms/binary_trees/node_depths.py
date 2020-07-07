"""
Problem:

The distance between a node in Binary Tree and the tree's root is called
the node's depth.

Write a function that takes in a Binary Tree and returns the sum of its nodes
depths.

Each Binary Tree node has an integer value, a left child and a right child.
Children Nodes can either a BinaryTree or None.

See the definition below.
"""


from typing import Union


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def node_depth(root: BinaryTree) -> int:
    """
    Complexity:
        Time: O(n) where n how many nodes the tree has
        Space: O(n) since n calls need to be added to the stack
    """
    def find_depth(root: Union[BinaryTree, None], current_depth: int):
        if root.left is None and root.right is None:
            return current_depth

        if root.left is None:
            return (
                current_depth +
                find_depth(root.right, current_depth + 1)
            )

        if root.right is None:
            return (
                current_depth +
                find_depth(root.left, current_depth + 1)
            )

        return (
            current_depth +
            find_depth(root.left, current_depth + 1) +
            find_depth(root.right, current_depth + 1)
        )

    return find_depth(root=root, current_depth=0)

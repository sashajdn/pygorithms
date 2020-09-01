"""
Problem Statement:

Given three inputs, all which are instances of an Ancestral Tree class that
has an `ancestor` property pointing to the youngest ancestor.

The first input is the top ancestor in the tree, and the second and third
a given node in the tree.

Write a function that finds the youngest common ancestor of the two nodes.
"""


class AncestralNode:
    def __init__(self, name):
        self.name: str = name
        self.ancestor: 'AncestralNode' = None


def get_youngest_common_ancestor(
        top_ancestor: AncestralNode, a: AncestralNode, b: AncestralNode
) -> AncestralNode:
    """
    Complexity:
        Time -> O(d) where is the depth of the tree
        Space -> O(1)
    """

    depth_a = find_depth(top_ancestor, a)
    depth_b = find_depth(top_ancestor, b)

    if depth_b > depth_a:
        return back_traversal(a, b, depth_b - depth_a)

    return back_traversal(b, a, depth_a - depth_b)


def find_depth(top_ancestor: AncestralNode, node: AncestralNode) -> int:
    if node == top_ancestor:
        return 0

    return 1 + find_depth(top_ancestor, node.ancestor)


def back_traversal(
        lower_node: AncestralNode, higher_node: AncestralNode, diff: int
) -> AncestralNode:

    if diff > 0:
        return back_traversal(lower_node.ancestor, higher_node, diff - 1)

    if lower_node != higher_node:
        return back_traversal(lower_node.ancestor, higher_node.ancestor, 0)

    return lower_node

"""
Problem:

Write a function that takes in a non-empty sorted array of distinct elements,
constructs a binary sort tree from the integers and returns the root of the BST.

The function should aim to minimize the BST.
"""

from typing import List


class BST:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value: int):
        if value < self.value:
            if self.left is None:
                self.left = self.__class__(value=value)
                return self.left

            return self.left.insert(value=value)

        if self.right is None:
            self.right = self.__class__(value=value)
            return self.right

        return self.left.insert(value=value)


def min_height_bst(array: List) -> int:
    if len(array) == 0:
        return None

    mididx = len(array) // 2

    bst = BST(value=array[mididx])
    bst.left = min_height_bst(array=array[0:mididx])
    bst.right = min_height_bst(array=array[mididx+1:len(array)])
    return bst

"""
Problem Statement:

Write a function that takes in the head of a singly linked list, and removes
the kth node from the end.

The removal should be done in place.

The head should stay in place, even if it's the kth element to be removed.
Meaning it's value should be mutated with the kth + 1 element, along with
the next pointer.

The function doens't need to return anything.

It's safe to assume that the linked list will have at least k nodes.
"""

from typing import Optional


class LinkedListNode:
    def __init__(self, value: int):
        self.value: int = value
        self.next: Optional["LinkedListNode"] = None


def remove_kth_node_from_end(head: LinkedListNode, k: int) -> None:
    current_node = head
    kth_node_from_end = head
    current_position = 1

    while current_position <= k:
        current_node = current_node.next
        current_position += 1

    if current_node is None:
        head.value = head.next.value
        head.next = head.next.next
        return

    while current_node.next is not None:
        current_node = current_node.next
        kth_node_from_end = kth_node_from_end.next

    kth_node_from_end.next = kth_node_from_end.next.next

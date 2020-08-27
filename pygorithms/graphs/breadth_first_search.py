"""
Problem Statement:

Given a `Node` that contains the state -> name: str, children: List[Node].
Write a method that performs a breadth first search on the nodes, return a
list of the names of the nodes in this order.
"""

from collections import deque
from typing import Deque, List


class Node():
    """
    Complexity:

    Time -> O(v + e) where, v is the vertices and e the edges
    Space -> O(v) where, v is the vertices and e the edges
    """
    def __init__(self, name: str, children: List['Node']):
        self.name = name
        self.children = children

    def bfs(self, array: List[str]) -> List[str]:
        q: Deque['Node'] = deque()
        q.appendleft(self)

        while len(q) > 0:
            current = q.pop()
            array.append(current.name)
            for child in current.children:
                q.appendleft(child)

        return array

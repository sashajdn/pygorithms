"""
Problem Statement:

Build a Min Heap Data Structure with the following operations:

- heapify: build a min heap from an array
- insert: insert a new element into the min heap
- remove: remove the minimum value from the min heap
- peek: peak at the minimum value

The internal structure that represents the min heap should be an array.
"""


import abc
from typing import List, Optional


class IHeap(abc.ABC):
    @abc.abstractmethod
    def heapify(self, array: List[int]) -> List[int]:
        pass

    @abc.abstractmethod
    def insert(self, value: int) -> None:
        pass

    @abc.abstractmethod
    def remove(self) -> int:
        pass

    @abc.abstractmethod
    def peak(self) -> int:
        pass


class MinHeap(IHeap):
    def __init__(self, array: Optional[List[int]] = None, /):
        self._heap = self.heapify(array) if array else []

    def heapify(self, array):
        def recurse(starting_idx, heap):
            if starting_idx < 0:
                return heap

            self._sift_down(starting_idx, heap)
            return recurse(starting_idx - 1, heap)

        return recurse((len(array) - 2) // 2, array)

    @staticmethod
    def _get_children(*, idx: int, heap: List[int]) -> List[int]:
        if len(heap) - 1 >= idx * 2 + 2:
            return heap[idx * 2 + 1: idx * 2 + 3]  # 3 since range (2 + 1)

        if len(heap) - 1 >= idx * 2 + 1:
            return [heap[idx * 2 + 1]]

        return []

    def _sift_up(self, current_idx: int, heap: List[int]) -> None:
        if current_idx > 0:
            if heap[current_idx] < heap[(current_idx - 1) // 2]:
                self._swap(current_idx, (current_idx - 1) // 2, heap)
                return self._sift_up((current_idx - 1) // 2, heap)

        return

    def _sift_down(self, current_idx: int, heap: List[int]) -> None:
        if current_idx < len(heap):
            children = self._get_children(idx=current_idx, heap=heap)
            if not children:
                return None

            if min(heap[current_idx], *children) == heap[current_idx]:
                return None

            if len(children) == 1:
                self._swap(current_idx, current_idx * 2 + 1, heap)
                return self._sift_down(current_idx * 2 + 1, heap)

            if heap[current_idx * 2 + 1] > heap[current_idx * 2 + 2]:
                self._swap(current_idx, current_idx * 2 + 1, heap)
                return self._sift_down(current_idx * 2 + 1, heap)

            self._swap(current_idx, current_idx * 2 + 2, heap)
            return self._sift_down(current_idx * 2 + 2, heap)

    def peak(self) -> int:
        return self._heap[0]

    def insert(self, value: int) -> None:
        self._heap.append(value)
        self._sift_up(len(self._heap) - 1, self._heap)

    def remove(self) -> int:
        self._swap(self._heap[0], len(self._heap) - 1, self._heap)
        to_return = self._heap.pop()
        self._sift_down(0, self._heap)
        return to_return

    @staticmethod
    def _swap(i: int, j: int, heap: List[int]) -> None:
        heap[i], heap[j] = heap[j], heap[i]

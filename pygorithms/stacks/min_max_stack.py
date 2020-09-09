from typing import List


class MinMaxStack:
    def __init__(self):
        self._min: List[int] = []
        self._max: List[int] = []
        self._stack: List[int] = []

    def peak(self) -> int:
        """T -> O(1), S -> O(1)."""
        return self._stack[-1]

    def pop(self) -> int:
        """T -> O(1), S -> O(1)."""
        return self._stack.pop()

    def push(self, value: int) -> None:
        """T -> O(1), S -> O(1)."""
        if not self._stack:
            self._min.append(value)
            self._max.append(value)
        else:
            self._min.append(min(value, self._min[-1]))
            self._max.append(max(value, self._max[-1]))

        self._stack.append(value)

    def min(self) -> int:
        """T -> O(1), S -> O(1)."""
        return self._min[-1]

    def max(self) -> int:
        """T -> O(1), S -> O(1)."""
        return self._max[-1]

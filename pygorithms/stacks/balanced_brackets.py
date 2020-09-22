"""
Problem Statement:

Write a function that checks that brackets are indeed balanced.
"""


from typing import List


def balanced_brackets(string: str):
    """
    Complexity:
        Time -> O(n)
        Space -> O(n)
    """
    stack: List[str] = []
    open_brackets = {"(", "[", "{"}
    closed_brackets = {")", "]", "}"}

    closed_to_open = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    for char in string:
        if char in open_brackets:
            stack.append(char)

        if char in closed_brackets:
            if len(stack) == 0:
                return False

            if not stack.pop() == closed_to_open[char]:
                return False

        continue

    return len(stack) == 0

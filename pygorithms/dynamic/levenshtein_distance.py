"""
Problem Statement:

Given two strings, find the minimum number of edits to apply to one of the
strings in order for them to match, whereby the possible edits are as follows:

- Insert new char
- Alter char
- Delete char
"""


def levenshtein_distance_simple(str1: str, str2: str) -> int:
    """
    Complexity:
    Time:
        O(nm)
    Space:
        O(nm)
    """
    m, n = len(str1) + 1, len(str2) + 1
    edits = [[x for x in range(m)] for _ in range(n)]

    for i in range(n):
        edits[i][0] = i

    for i in range(1, n):
        for j in range(1, m):
            if str2[i - 1] == str1[j - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][j] = 1 + min(
                    edits[i - 1][j - 1],
                    edits[i][j - 1],
                    edits[i - 1][j],
                )

    return edits[-1][-1]

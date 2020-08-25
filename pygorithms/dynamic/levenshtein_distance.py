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


def levenshtein_distance(str1: str, str2: str) -> int:
    """
    Complexity:
    Time:
        O(nm)
    Space:
        O(min(m, n))
    """
    small, big = sorted((str1, str2), key=len)

    even_edits = [x for x in range(len(small) + 1)]
    odd_edits = [None for _ in range(len(small) + 1)]

    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            prev = even_edits
            curr = odd_edits
        else:
            prev = odd_edits
            curr = even_edits

        curr[0] = i

        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(
                    prev[j - 1],
                    prev[j],
                    curr[j - 1],
                )

    return even_edits[-1] if len(big) % 2 == 0 else odd_edits[-1]

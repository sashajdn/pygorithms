"""
Problem Statement:

Write a function that takes in an array of strings and
groups anagrams together.
"""


import collections
from typing import Dict, List


def group_anagrams(words: List[str]) -> List[List[str]]:
    anagrams: Dict[str, List[str]] = collections.defaultdict(list)

    for word in words:
        anagrams[''.join(sorted(word))].append(word)

    return [
        group for group in anagrams.values()
    ]

"""
Author: Resul Emre AYGAN
"""

from collections import Counter


class Solution:
    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

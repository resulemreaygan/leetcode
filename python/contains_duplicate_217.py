"""
Author: Resul Emre AYGAN
"""

from typing import List


class Solution:
    @staticmethod
    def contains_duplicate(nums: List[int]) -> bool:
        number_list = set()

        for number in nums:
            if number in number_list:
                return True

            number_list.add(number)
        return False

"""
Author: Resul Emre AYGAN
"""

from typing import List


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        index_dict = {}

        for index, number in enumerate(nums):
            temp_number = target - number

            if temp_number in index_dict:
                return [index_dict[temp_number], index]

            index_dict[number] = index

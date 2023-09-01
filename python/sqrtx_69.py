"""
Author: Resul Emre AYGAN
"""


class Solution:
    @staticmethod
    def my_sqrt(x: int) -> int:
        # Binary Search

        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            if mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right

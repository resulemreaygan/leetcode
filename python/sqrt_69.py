"""
Author: Resul Emre AYGAN
"""


class Solution:
    @staticmethod
    def my_sqrt(x: int) -> int:
        # Newton-Raphson method

        epsilon_number = 1e-6  # epsilon parameter that specifies the desired level of precision

        temp_number = x / 2.0

        while abs(temp_number * temp_number - x) > epsilon_number:
            temp_number = (temp_number + x / temp_number) / 2.0

        return int(temp_number)

"""

89. Gray Code
Medium
"""

from typing import List


class Solution:

    def generateGrayCode(self, n: int, seed: int) -> List[int]:
        bit = 1 << (n-1)

        if n == 1: return [seed, seed ^ bit]

        gray_codes = list()
        gray_codes.extend(self.generateGrayCode(n-1, seed))
        gray_codes.extend(self.generateGrayCode(n-1, bit ^ gray_codes[-1]))

        return gray_codes

    def grayCode(self, n: int) -> List[int]:
        if n == 0: return [0]
        return self.generateGrayCode(n, seed=0)

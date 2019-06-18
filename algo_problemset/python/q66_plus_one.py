"""

66. Plus One
Easy
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1

        carry, n = 0, len(digits)
        for i in reversed(range(n)):
            digits[i] += carry

            carry = digits[i] // 10
            digits[i] = digits[i] % 10

            if carry == 0: break

        if (i == 0) and (carry > 0):
            digits.insert(0, carry)
        return digits

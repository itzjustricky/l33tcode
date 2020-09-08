from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # need this due to the strange way in which in how
        # negative integers are handled in python
        negativeCntMod3 = 0

        # store all bits that show up mod 3 = 0 times
        bitsMod3Eq0 = (1 << 32) - 1
        # store all bits that show up mod 3 = 1 times
        bitsMod3Eq1 = 0
        # store all bits that show up mod 3 = 2 times
        bitsMod3Eq2 = 0

        for num in nums:
            isNegative = num < 0
            if isNegative:
                num *= -1   # switch to positive
                negativeCntMod3 = (negativeCntMod3 + 1) % 3

            prevEq0, prevEq1, prevEq2 = bitsMod3Eq0, bitsMod3Eq1, bitsMod3Eq2

            bitsMod3Eq0 ^= (prevEq0 & num)  # flip out bits appearing mod 3 == 1 times
            bitsMod3Eq0 ^= (prevEq2 & num)  # flip in bits appearing mod 3 == 0 times

            bitsMod3Eq1 ^= (prevEq1 & num)  # flip out bits
            bitsMod3Eq1 ^= (prevEq0 & num)  # flip in bits

            bitsMod3Eq2 ^= (prevEq2 & num)  # flip out bits
            bitsMod3Eq2 ^= (prevEq1 & num)  # flip in bits

        return bitsMod3Eq1 * (-1 if negativeCntMod3 == 1 else 1)

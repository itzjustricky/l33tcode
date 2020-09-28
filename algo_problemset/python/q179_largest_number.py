from functools import cmp_to_key

from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all((x == 0 for x in nums)):
            return '0'
        return ''.join(
            sorted(map(str, nums), key=cmp_to_key(numComp)))


def numComp(num1: str, num2: str):

    if num1 + num2 < num2 + num1:
        return 1
    elif num1 + num2 > num2 + num1:
        return -1
    else:
        return 0

"""
27. Remove Element
Easy
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        for i in reversed(range(0, n)):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)

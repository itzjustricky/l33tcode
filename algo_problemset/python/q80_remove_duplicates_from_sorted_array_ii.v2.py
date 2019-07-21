"""

80. Remove Duplicates from Sorted Array II
Medium
"""

from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if i < 2 or num > nums[i-2]:
                nums[i] = num
                i += 1
        return i

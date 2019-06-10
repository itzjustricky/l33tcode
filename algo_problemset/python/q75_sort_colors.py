"""

75. Sort Colors
Medium
"""

from typing import List


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0: red, 1: white, and 2: blue

        # the start variables represent where the sorted section of
        # the list where the 1 (white) and 2 (blue) numbers will start
        # 0 (red) numbers will naturally start at index 0
        w_start, b_start = 0, 0

        for i, x in enumerate(nums):

            if x == 0:
                # swap to start of 2s and right after end of 1s
                nums[i], nums[b_start] = nums[b_start], nums[i]
                # swap to start of 1s and right after end of 0s
                nums[w_start], nums[b_start] = nums[b_start], nums[w_start]
                w_start += 1; b_start += 1
            elif x == 1:
                # swap to start of 2s and right after end of 1s
                nums[i], nums[b_start] = nums[b_start], nums[i]
                b_start += 1
            else:   # x == 2
                # don't need to do anything, the number will
                # be at the tail of the 2 numbers
                pass

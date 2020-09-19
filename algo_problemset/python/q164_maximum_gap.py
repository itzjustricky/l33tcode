from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0

        nums.sort()

        return max(
            nums[i]-nums[i-1]
            for i in range(1, len(nums)))

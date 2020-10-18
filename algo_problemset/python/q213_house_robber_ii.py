from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]

        self.cache = dict()

        return max(
            nums[0] + self.recursiveRob(2, True, nums),
            self.recursiveRob(1, False, nums))

    def recursiveRob(self, start: int, robbedFirst: bool, nums: List[int]) -> int:
        n = len(nums)
        if start == (n-1):
            return 0 if robbedFirst else nums[n-1]
        if start >= n:
            return 0

        if (start, robbedFirst) in self.cache:
            return self.cache[(start, robbedFirst)]

        self.cache[(start, robbedFirst)] = max(
            nums[start] + self.recursiveRob(start + 2, robbedFirst, nums),
            self.recursiveRob(start + 1, robbedFirst, nums))
        return self.cache[(start, robbedFirst)]

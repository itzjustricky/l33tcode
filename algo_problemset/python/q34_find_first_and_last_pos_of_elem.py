"""

34. Find First and Last Position of Element in Sorted Array
Medium
"""

import operator
from typing import List


class Solution:

    def binarySearch(self, nums: List[int], target: int, op) -> int:
        n = len(nums)

        l, r = 0, n-1
        while (r - l) > 1:
            mid = (l + r) // 2
            if op(nums[mid], target):
                l = mid
            else:
                r = mid
        return l, r

    def binarySearchLeft(self, nums: List[int], target: int) -> int:
        l, r = self.binarySearch(nums, target, op=operator.lt)
        if nums[l] == target: return l
        elif nums[r] == target: return r
        else: return -1

    def binarySearchRight(self, nums: List[int], target: int) -> int:
        l, r = self.binarySearch(nums, target, op=operator.le)
        if nums[r] == target: return r
        elif nums[l] == target: return l
        else: return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        left_range = self.binarySearchLeft(nums, target)
        if left_range == -1:
            return [-1, -1]
        else:
            return [
                left_range,
                self.binarySearchRight(nums, target)]

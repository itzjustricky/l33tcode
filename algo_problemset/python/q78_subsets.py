"""

78. Subsets
Medium

    Given a set of distinct integers, nums, return all possible subsets (the power set).

    Note: The solution set must not contain duplicate subsets.

    Example:
    Input: nums = [1,2,3]
    Output:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
"""

from typing import List


class Solution:

    def subsetGenerator(self, start_index: int, nums: List[int]) -> List[List[int]]:
        if start_index == (len(nums)-1):
            return [[], [nums[start_index]]]

        subsets = self.subsetGenerator(start_index+1, nums)
        num = nums[start_index]
        subsets.extend([[num] + subset for subset in subsets])
        return subsets

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subsetGenerator(0, nums)

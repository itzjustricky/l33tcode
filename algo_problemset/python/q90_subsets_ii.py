"""

90. Subsets II
Medium
"""

# import itertools
from typing import List


class Solution:

    def findNextNumberIndex(self, start: int, nums: List[int]):
        """ Find the index of the next number not equal to the located at start """
        N, num = len(nums), nums[start]
        for ind in range(start+1, N):
            if nums[ind] != num: return ind

        # reached end of list
        return N

    def recursiveGenerateSubsets(self, start: int, nums: List[int]) -> List[List[int]]:
        """ Generate all subsets that start with the number located in start index """
        N = len(nums)
        if start >= N: return [[]]
        if start in self._subset_hash:
            return self._subset_hash[start]

        next_ind = self.findNextNumberIndex(start, nums)

        subsets = [[]] + [nums[start:end] for end in range(start+1, next_ind+1)]
        later_subsets = self.recursiveGenerateSubsets(next_ind, nums)

        subsets = [x + y
                   for y in later_subsets
                   for x in subsets]

        self._subset_hash[start] = subsets
        return subsets

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self._subset_hash = dict()

        nums = sorted(nums)
        return self.recursiveGenerateSubsets(0, nums)

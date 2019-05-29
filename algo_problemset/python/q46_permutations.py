"""

46. Permutations
Medium
"""

from typing import List


class Solution:

    def recursivePermute(self, nums: List[int], allowed_inds: List[int]):
        n_allowed_inds = len(allowed_inds)

        if n_allowed_inds == 2:
            return [
                [nums[i] for i in allowed_inds],
                [nums[i] for i in reversed(allowed_inds)],
            ]

        permutations = []
        for i, allowed_ind in enumerate(allowed_inds):
            _allowed_inds = allowed_inds[:i] + allowed_inds[(i+1):]
            permutations.extend([
                [nums[allowed_ind]] + perm
                for perm in self.recursivePermute(nums, _allowed_inds)])
        return permutations

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        if n <= 1:
            return [nums]

        allowed_inds = list(range(n))
        return self.recursivePermute(nums, allowed_inds)

"""

47. Permutations II
Medium
"""

from typing import List


class Solution:

    def recursivePermute(self, nums: List[int], allowed_inds: List[int]):
        n_allowed_inds = len(allowed_inds)

        if n_allowed_inds == 2:
            x1, x2 = nums[allowed_inds[0]], nums[allowed_inds[1]]
            if x1 == x2:
                return [[x1, x2]]
            else:
                return [[x1, x2], [x2, x1]]

        prev_x = None
        permutations = []
        for i, allowed_ind in enumerate(allowed_inds):
            _allowed_inds = allowed_inds[:i] + allowed_inds[(i+1):]

            x = nums[allowed_ind]
            if x == prev_x: continue

            permutations.extend([
                [x] + perm
                for perm in self.recursivePermute(nums, _allowed_inds)])
            prev_x = x
        return permutations

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        if n <= 1:
            return [nums]

        nums = sorted(nums)
        allowed_inds = list(range(n))
        return self.recursivePermute(nums, allowed_inds)

"""

18. 4Sum
Medium
"""

from typing import List
from typing import Tuple
from typing import Union


class Solution:

    def twoSum(self, target: int, bounds: Tuple[int, int], nums: List[int]):
        lbnd, rbnd = bounds
        if (rbnd - lbnd) <= 0:
            return []

        good_pairs = []

        lptr, rptr = lbnd, rbnd
        while lptr < rptr:
            s = nums[lptr] + nums[rptr]
            if s == target:
                good_pairs.append([nums[lptr], nums[rptr]])
                # avoid duplicates
                while (lptr < rbnd) and (nums[lptr] == nums[lptr+1]): lptr += 1
                lptr += 1
            elif s < target:
                lptr += 1
            else:   # s > target
                rptr -= 1

        return good_pairs

    def recursiveFindSum(
            self,
            target: int, bounds: Tuple[int, int], nums: List[int],
            N: int, numbers_used: List[int]) -> Union[None, List[List[int]]]:

        lbnd, rbnd = bounds
        if ((rbnd - lbnd) < N-1):
            return None

        if N == 2:
            found_sums = [numbers_used + pair
                          for pair in self.twoSum(target, bounds, nums)]
            return found_sums if len(found_sums) > 0 else None
        else:
            all_found_sums = []
            prev_used = None
            for i in range(lbnd, rbnd+1):
                if (nums[i] == prev_used):
                    continue

                found_sums = self.recursiveFindSum(
                    target-nums[i], (i+1, rbnd), nums, N-1, numbers_used+[nums[i]])
                if found_sums is not None:
                    all_found_sums.extend(found_sums)

                prev_used = nums[i]
            return all_found_sums if len(all_found_sums) > 0 else None

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n_nums = len(nums)

        found_sums = self.recursiveFindSum(
            target, (0, n_nums-1), nums, 4, [])
        return found_sums if found_sums is not None else []

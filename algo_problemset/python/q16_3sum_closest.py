"""

16. 3Sum Closest
Medium
"""

import math
from typing import List


class Solution:

    @staticmethod
    def twoSumClosest(nums: List[int], target: int, start_index: int) -> int:

        n = len(nums)
        lbnd, rbnd = start_index, n-1

        num_sum = nums[lbnd] + nums[rbnd]
        closest_num_sum = num_sum

        while (rbnd - lbnd) > 1:
            if num_sum == target:
                return num_sum
            elif num_sum > target:
                rbnd -= 1
            else:   # num_sum < target
                lbnd += 1

            num_sum = nums[lbnd] + nums[rbnd]
            if abs(target-num_sum) < abs(target-closest_num_sum):
                closest_num_sum = num_sum

        return closest_num_sum

    def threeSumClosest(self, nums: List[int], target: int) -> int:

        n = len(nums)
        nums = sorted(nums)

        if n < 3:
            raise ValueError("There are not enough numbers in nums for a 3Sum.")

        closest_num_sum = math.inf

        for i in range(0, n-2):
            _target = target-nums[i]

            num_sum = self.twoSumClosest(nums, _target, i+1)
            if abs(_target-num_sum) < abs(target-closest_num_sum):
                closest_num_sum = num_sum + nums[i]

                # early return
                if closest_num_sum == target:
                    return closest_num_sum

        return closest_num_sum


if __name__ == "__main__":
    sol = Solution()

    print(sol.threeSumClosest([-1,2,1,-4,10,23,18,6,3,7,2], 12))    # noqa

"""

81. Search in Rotated Sorted Array II
Medium
"""

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0: return False

        lbound, rbound = 0, len(nums)-1

        while (rbound - lbound) > 1:
            mid = (rbound + lbound) // 2

            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                if (nums[mid] > nums[rbound]) and (target <= nums[rbound]):
                    lbound = mid
                else:
                    rbound = mid
            else:   # target > nums[mid]
                if (nums[mid] < nums[lbound]) and (target >= nums[lbound]):
                    rbound = mid
                else:
                    lbound = mid

        return (nums[lbound] == target) or (nums[rbound] == target)

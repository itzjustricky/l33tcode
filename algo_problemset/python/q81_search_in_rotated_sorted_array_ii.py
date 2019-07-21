"""

81. Search in Rotated Sorted Array II
Medium
"""

from typing import List


class Solution:

    def binarySearch(self, nums: List[int], target: int,
                     start: int, end: int) -> bool:
        lbound, rbound = start, end

        while (rbound - lbound) > 1:
            mid = (rbound + lbound) // 2

            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                # if this is the scenario it can be on either side
                if (nums[mid] == nums[rbound]):
                    return self.binarySearch(nums, target, lbound, mid-1) or \
                        self.binarySearch(nums, target, mid+1, rbound)
                if (nums[mid] > nums[rbound]) and (target <= nums[rbound]):
                    lbound = mid
                else:
                    rbound = mid
            else:   # target > nums[mid]
                if (nums[mid] == nums[lbound]):
                    return self.binarySearch(nums, target, lbound, mid-1) or \
                        self.binarySearch(nums, target, mid+1, rbound)
                if (nums[mid] < nums[lbound]) and (target >= nums[lbound]):
                    rbound = mid
                else:
                    lbound = mid

        return (nums[lbound] == target) or (nums[rbound] == target)

    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0: return False

        return self.binarySearch(nums, target, 0, len(nums)-1)

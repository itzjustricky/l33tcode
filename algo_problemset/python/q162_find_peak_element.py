import math
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        leftInd, rightInd = 0, len(nums)-1

        while (rightInd - leftInd) > 1:
            mid = (rightInd + leftInd) // 2

            if self.isPeak(leftInd, nums):
                return leftInd
            if self.isPeak(rightInd, nums):
                return rightInd
            if self.isPeak(mid, nums):
                return mid

            if nums[leftInd] >= nums[mid]:
                rightInd = mid
            elif nums[rightInd] >= nums[mid]:
                leftInd = mid
            # at this point, mid is greater than both left and right
            #   at least one of mid's neighbors is greater than mid since it is not a peak
            # note: also neighbor numbers cannot be equal
            elif nums[mid] < nums[mid-1]:
                rightInd = mid
            else:
                leftInd = mid

        # at this point, either the leftInd or rightInd should be a peak
        if self.isPeak(leftInd, nums):
            return leftInd
        else:
            return rightInd

    def isPeak(self, ind: int, nums: List[int]) -> bool:
        leftNum = nums[ind-1] if (ind-1) >= 0 else -math.inf
        rightNum = nums[ind+1] if (ind+1) < len(nums) else -math.inf

        return (leftNum < nums[ind]) and (nums[ind] > rightNum)


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.findPeakElement([1,2,3,1])  # noqa
    )

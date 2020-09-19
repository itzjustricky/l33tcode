from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        leftInd, rightInd = 0, len(nums)-1

        # make sure that the min value is always
        # in between (inclusive) leftInd & rightInd
        while (rightInd - leftInd) > 1:
            mid = (leftInd + rightInd) // 2

            if nums[leftInd] > nums[rightInd]:
                if nums[mid] < nums[leftInd]:
                    rightInd = mid
                else:
                    leftInd = mid
            # the range betwen leftInd and rightInd is actually in order
            else:
                return nums[leftInd]

        return min(nums[leftInd], nums[rightInd])

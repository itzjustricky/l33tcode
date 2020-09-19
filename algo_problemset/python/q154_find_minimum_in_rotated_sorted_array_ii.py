from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.recursiveFindMin(0, len(nums)-1, nums)

    def recursiveFindMin(self, startInd: int, endInd: int, nums: List[int]) -> int:
        leftInd, rightInd = startInd, endInd

        # make sure that the min value is always
        # in between (inclusive) leftInd & rightInd
        while (rightInd - leftInd) > 1:
            mid = (leftInd + rightInd) // 2

            # the rotation pivot is in between the leftInd & rightInd
            if nums[leftInd] > nums[rightInd]:
                if nums[leftInd] <= nums[mid]:
                    leftInd = mid
                # mid is after the rotation pivot point
                else:
                    rightInd = mid
            # the value at leftInd & rightInd are equal
            # but there might be a dip in between
            elif nums[leftInd] == nums[rightInd]:
                return min(
                    self.recursiveFindMin(leftInd, mid, nums),
                    self.recursiveFindMin(mid+1, rightInd, nums))
            # the range between leftInd and rightInd is in order
            else:
                return nums[leftInd]

        return min(nums[leftInd], nums[rightInd])

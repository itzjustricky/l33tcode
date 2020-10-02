import math
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0

        leftInd, rightInd = 0, 1
        subSumLeft, subSumRight = 0, nums[0]

        minLengthTracker = math.inf
        while rightInd < n:

            # move the right boundary up until it goes above the target
            while (rightInd < n) and (subSumRight - subSumLeft) < s:
                subSumRight += nums[rightInd]
                rightInd += 1

            # move the left boundary up to right BEFORE it goes below the target
            while (leftInd < rightInd) and (subSumRight - subSumLeft - nums[leftInd]) >= s:
                subSumLeft += nums[leftInd]
                leftInd += 1

            if (subSumRight - subSumLeft) >= s:
                minLengthTracker = min(minLengthTracker, rightInd - leftInd)

            # move left boundary right one so that right boundary can move
            # to satisfy condition of >= target
            subSumLeft += nums[leftInd]; leftInd += 1

        return 0 if minLengthTracker == math.inf else minLengthTracker

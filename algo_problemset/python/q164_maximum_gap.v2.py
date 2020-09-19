import math
from typing import List


class GapBucket:
    def __init__(self):
        self.minValue = math.inf
        self.maxValue = -math.inf
        self.isEmpty = True


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0

        # find the min and max
        minNum, maxNum = math.inf, -math.inf
        for num in nums:
            minNum, maxNum = min(minNum, num), max(maxNum, num)

        maxMinDiff = maxNum - minNum
        # all the numbers are the same
        rangeSize = maxMinDiff // (n - 1)

        # if rangeSize==0 the numbers are likely clustered together
        # (possibly all the numbers are equal)
        if rangeSize == 0: rangeSize = 1

        # bucket the numbers them into the n ranges of size rangeSize
        # ranging from the Min. Value to the Max Value
        #       if num is in the i-th bucket then it is within
        #       [MinValue + RangeSize * i, MinValue + RangeSize * (i+1))
        buckets = [GapBucket() for i in range(maxMinDiff // rangeSize + 1)]
        for num in nums:
            bucketForNum = buckets[(num - minNum) // rangeSize]
            bucketForNum.minValue = min(bucketForNum.minValue, num)
            bucketForNum.maxValue = max(bucketForNum.maxValue, num)
            bucketForNum.isEmpty = False

        maxGap, prevBucket = 0, buckets[0]
        for ind in range(1, len(buckets)):
            if prevBucket.isEmpty:
                prevBucket = buckets[ind]
                continue
            if buckets[ind].isEmpty:
                continue

            maxGap = max(maxGap, buckets[ind].minValue - prevBucket.maxValue)
            prevBucket = buckets[ind]

        return maxGap


if __name__ == "__main__":
    sol = Solution()
    sol.maximumGap([3,6,9,1])   # noqa

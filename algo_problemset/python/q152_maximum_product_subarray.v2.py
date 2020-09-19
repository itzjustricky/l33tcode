from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            raise ValueError("Invalid argument: empty nums list")

        # maxSub tracks the maximum contiguous subarray product that includes
        #       the current visited num
        # minSub tracks the minimum contiguous subarray product that includes
        #       the current visited num
        maxSub, minSub = nums[0], nums[0]
        maxProdTracker = maxSub

        for num in nums[1:]:

            # if the last number was zero, then both maxSub & minSub are zero
            # note minSub has tracked min (most negative) # including last visited num
            # note maxSub has tracked max (most positive) # including last visited num
            if num < 0:
                # flip them in prepaparation of sign flip below
                maxSub, minSub = minSub, maxSub

            maxSub = max(maxSub * num, num)
            minSub = min(minSub * num, num)
            maxProdTracker = max(maxProdTracker, maxSub)

        return maxProdTracker

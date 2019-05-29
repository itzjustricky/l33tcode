"""

53. Maximum Subarray
Easy
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 0:
            raise ValueError("Passed nums list must have length > 0.")

        # Note: subarray must at least contain one element
        cum_sum, min_cum_sum, max_subarray_sum = nums[0], min(0, nums[0]), nums[0]
        for x in nums[1:]:
            cum_sum += x
            if cum_sum - min_cum_sum > max_subarray_sum:
                max_subarray_sum = cum_sum - min_cum_sum
            if cum_sum < min_cum_sum:
                min_cum_sum = cum_sum

        return max_subarray_sum

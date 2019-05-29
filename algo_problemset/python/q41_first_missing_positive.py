"""

41. First Missing Positive
Hard
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # first part, put all the numbers at their associated index
        # if the number found is larger than the length of the
        # list or negative then ignore it
        for i in range(n):
            x = nums[i]
            while True:
                if (x > n) or (x <= 0) or (nums[x-1] == x):
                    break
                else:
                    stored_val = nums[x-1]
                    nums[x-1] = x
                    x = stored_val

        # second part, do a scan over the transformed array
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1

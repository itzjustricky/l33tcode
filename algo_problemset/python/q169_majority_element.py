"""

169. Majority Element
Easy
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_num, num_cnt = nums[0], 1

        for num in nums[1:]:
            if num == curr_num:
                num_cnt += 1
            elif num_cnt == 0:
                curr_num, num_cnt = num, 1
            else:
                num_cnt -= 1
        return curr_num

"""

229. Majority Element II
Medium
"""

from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ctr = Counter()
        for n in nums:
            ctr[n] += 1
            if len(ctr) == 3:
                ctr -= Counter(set(ctr))

        n_over_3 = len(nums) // 3
        ctr = Counter(num for num in nums if num in ctr)
        return [num for num, cnt in ctr.items() if cnt > n_over_3]

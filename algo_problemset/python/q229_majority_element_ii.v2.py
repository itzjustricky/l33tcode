"""

229. Majority Element II
Medium
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2 = None, None
        cnt1, cnt2 = 0, 0

        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1, cnt1 = num, 1
            elif cnt2 == 0:
                cand2, cnt2 = num, 1
            else:
                cnt1, cnt2 = cnt1-1, cnt2-1

        n_over_3 = len(nums) // 3
        return [num for num in (cand1, cand2)
                if nums.count(num) > n_over_3]


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3,3,4]))    # noqa

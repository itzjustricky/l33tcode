"""

45. Jump Game II
Hard
"""

from typing import List


class Solution:

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        n_jumps, prev_max_jump, curr_max_jump = 0, 0, 0

        for ind in range(n-1):
            # assumption is you can always reach the last index
            # which means you can always jump to the the current index
            curr_max_jump = max(curr_max_jump, ind + nums[ind])

            if prev_max_jump <= ind:
                prev_max_jump = curr_max_jump
                n_jumps += 1

        return n_jumps

if __name__ == "__main__":

    sol = Solution()
    nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(sol.jump(nums))

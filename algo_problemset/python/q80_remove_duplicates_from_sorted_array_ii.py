"""

80. Remove Duplicates from Sorted Array II
Medium
"""

from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:

        cnt, prev_num = 0, None
        slow_ptr, fast_ptr = 0, 0

        nums_length, curr_length = len(nums), len(nums)

        while fast_ptr < nums_length:

            if nums[fast_ptr] == prev_num: cnt += 1
            else: cnt = 0

            # move the fast pointer to a new number if a number
            # duplicates more than twice
            while cnt >= 2:
                curr_length -= 1
                prev_num = nums[fast_ptr]
                fast_ptr += 1

                if fast_ptr >= nums_length: return curr_length

                if nums[fast_ptr] == prev_num: cnt += 1
                else: cnt = 0

            prev_num = nums[fast_ptr]

            nums[slow_ptr] = nums[fast_ptr]
            slow_ptr += 1; fast_ptr += 1

        return curr_length


if __name__ == "__main__":
    sol = Solution()
    nums = [0,0,1,1,1,1,2,3,3]  # noqa [E231]

    new_length = sol.removeDuplicates(nums)
    print(nums[:new_length])

    nums = [0,0,0,1,1,2,2,2,2,2,2]  # noqa [E231]
    new_length = sol.removeDuplicates(nums)
    print(nums[:new_length])

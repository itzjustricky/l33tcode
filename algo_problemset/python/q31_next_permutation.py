"""
31. Next Permutation
Medium
"""

from typing import List


class Solution:

    @staticmethod
    def findSmallestGreaterThan(nums: List[int], start: int, target: int):
        """ This finds the smallest number in the sublist nums[start:]
            that is greater than the passed target. Assumes the sublist
            nums[start:] to the end should be sorted in descending order.
        """
        n = len(nums)

        for ind in reversed(range(start, n)):
            if nums[ind] > target:
                return ind

        raise ValueError("There was no value > {} found in the sublist. "
                         "This should not be the case.")

    @staticmethod
    def reverseListTailInplace(nums: List[int], start: int):
        """ Reverse the list in-place from the start index until
            the end of the list
        """
        n = len(nums)

        n_swaps = (n - start) // 2
        for i in range(start, start+n_swaps):
            swap_ind = n-i+start-1
            nums[i], nums[swap_ind] = nums[swap_ind], nums[i]

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        # look from the back until we find number that is in order
        ind = n-1
        while (ind > 0) and (nums[ind-1] >= nums[ind]):
            ind -= 1

        # the whole list is in reversed order
        if ind == 0:
            self.reverseListTailInplace(nums, 0)
        else:
            smallest_ind = self.findSmallestGreaterThan(nums, ind, nums[ind-1])
            # swap the found number and the number right before the reversed tail
            nums[ind-1], nums[smallest_ind] = nums[smallest_ind], nums[ind-1]
            self.reverseListTailInplace(nums, ind)

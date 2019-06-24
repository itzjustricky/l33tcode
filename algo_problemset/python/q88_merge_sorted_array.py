"""

88. Merge Sorted Array
Easy
"""

from typing import List


class Solution:

    def insert(self, l: List[int], ind: int, m: int, num: int):
        swap_num = num
        for i in range(ind, m):
            swap_num, l[i] = l[i], swap_num
        l[m] = swap_num

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2 = 0, 0

        while (i1 < m) and (i2 < n):

            if nums1[i1] <= nums2[i2]:
                i1 += 1
            else:
                self.insert(nums1, i1, m, nums2[i2])
                i2 += 1; i1 += 1; m += 1

        if i2 < n:
            for ind in range(i2, n):
                nums1[i1+ind-i2] = nums2[ind]

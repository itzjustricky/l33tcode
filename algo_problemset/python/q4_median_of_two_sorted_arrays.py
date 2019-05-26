"""
    4. Median of Two Sorted Arrays.
    Hard

    There are two sorted arrays nums1 and nums2 of size
    m and n respectively.  Find the median of the two sorted arrays.
    The overall run time complexity should be O(log (m+n)).
    You may assume nums1 and nums2 cannot be both empty.

    Example 1:
    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0

    Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5
"""

from typing import List


def is_even(x: int) -> bool:
    return (x % 2) == 0


class Solution:

    def find_median_of_one(self, l: List[int]):
        n = len(l)
        if is_even(n):
            return (l[n//2-1] + l[n//2]) / 2
        else:
            return l[n//2]

    def binary_search_median(self, nums1: List[int], nums2: List[int]):
        """ This finds an important index (of the smaller list) to find the median

        :param nums1: the list of smaller size
        :param nums2: the list of bigger size
        """

        n1, n2 = len(nums1), len(nums2)
        lbound, rbound = 0, n1-1

        m1 = lbound + rbound
        m2 = (n1 + n2) // 2 - m1 - 1

        while (rbound - lbound) > 1:
            if nums1[m1] <= nums2[m2]:
                lbound = m1
            else:
                rbound = m1
            m1 = lbound + rbound
            m2 = (n1 + n2) // 2 - m1 - 1

        if (lbound == rbound):
            return m1

        if nums1[lbound] < nums2[(n1 + n2)//2 - lbound - 1]:
            m2 = (n1 + n2)//2 - lbound - 1
            if nums2[m2] <= nums1[rbound]:
                return lbound
            else:
                return rbound
        else:
            m2 = (n1 + n2)//2 - rbound - 1
            if nums1[rbound] <= nums2[m2]:
                return rbound
            else:
                return lbound

    def _decide_median(self, m1: int, nums1: List[int], nums2: List[int]) -> int:
        """ Helper function to help determine what is the
            median after binary search is done
        """

        n1, n2 = len(nums1), len(nums2)
        m2 = (n1 + n2) // 2 - m1 - 1

        if nums1[m1] >= nums2[m2]:
            if is_even(n1 + n2):
                # this is to find the next smallest number
                candidates = [nums1[m2]]
                if m1 > 0: candidates.append(nums1[m1-1])
                return (nums1[m1] + min(candidates)) / 2
            else:
                return nums1[m1]

        # nums1[m1] < nums2[m2]
        else:
            if is_even(n1 + n2):
                # this is to find the next smallest number
                candidates = [nums1[m1]]
                if m2 > 0: candidates.append(nums2[m2-1])
                return (nums2[m2] + min(candidates)) / 2
            else:
                return nums2[m2]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)

        if (n1 == 0) or (n2 == 0):
            if (n1 == 0) and (n2 == 0):
                return None
            elif (n1 == 0):
                return self.find_median_of_one(nums2)
            else:
                return self.find_median_of_one(nums1)

        if n1 <= n2:
            m1 = self.binary_search_median(nums1, nums2)
            return self._decide_median(m1, nums1, nums2)
        else:
            m1 = self.binary_search_median(nums2, nums1)
            return self._decide_median(m1, nums2, nums1)


if __name__ == "__main__":

    sol = Solution()
    # print("Found median: {}".format(sol.findMedianSortedArrays([1, 2], [3, 4])))
    print("Found median: {}".format(sol.findMedianSortedArrays([1, 3, 5, 8, 9], [2])))

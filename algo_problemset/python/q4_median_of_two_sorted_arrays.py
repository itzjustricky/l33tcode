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


class Solution:

    @staticmethod
    def find_median_of_one(l: List[int]):
        n = len(l)
        if is_even(n):
            return (l[n//2-1] + l[n//2]) / 2
        else:
            return l[n//2]

    @staticmethod
    def binary_search_median(nums1: List[int], nums2: List[int]):
        """ This finds an important index (of the smaller list) to find the median

        :param nums1: the list of smaller size
        :param nums2: the list of bigger size
        """
        n1, n2 = len(nums1), len(nums2)
        lbound, rbound = 0, n1

        # m1 acts as a separator for List nums1, separate into:
        # 0, ..., m1-1 | m1, ..., n1-1, n1
        m1 = (lbound + rbound) // 2
        # m2 acts as a separator for List nums2, separate into:
        # 0, ..., m2-1 | m2, ..., n1-1, n1
        m2 = (n1 + n2) // 2 - m1

        while (rbound - lbound) > 1:

            if all_left_are_lte(m1, nums1, get_element_or_none(m2, nums2)):
                # if this condition is also satisfied, we have found our index
                if all_left_are_lte(m2, nums2, get_element_or_none(m1, nums1)):
                    return m1
                lbound = m1

            else:
                rbound = m1
            m1 = (lbound + rbound) // 2
            m2 = (n1 + n2) // 2 - m1

        if (lbound == rbound):
            return m1
        elif satisfy_median_condition(lbound, nums1, nums2):
            return lbound
        elif satisfy_median_condition(rbound, nums1, nums2):
            return rbound
        else:
            raise ValueError(
                "Both boundaries do not satisfy the conditions. "
                "Something assumptions are wrong, lists are possibly not sorted.")

    @staticmethod
    def _decide_median(m1: int, nums1: List[int], nums2: List[int]):
        n1, n2 = len(nums1), len(nums2)
        m2 = (n1 + n2) // 2 - m1

        right_side_elements = list()
        if m1 < n1: right_side_elements.append(nums1[m1])
        if m2 < n2: right_side_elements.append(nums2[m2])

        if is_even(n1 + n2):
            left_side_elements = list()
            if m1 > 0: left_side_elements.append(nums1[m1-1])
            if m2 > 0: left_side_elements.append(nums2[m2-1])
            return (max(left_side_elements) + min(right_side_elements)) / 2
        else:
            return min(right_side_elements)

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
            return float(self._decide_median(m1, nums1, nums2))
        else:
            m1 = self.binary_search_median(nums2, nums1)
            return float(self._decide_median(m1, nums2, nums1))


def satisfy_median_condition(m1: int, nums1: List[int], nums2: List[int]) -> bool:
    """ Test if a found median index for the smaller list satisfies the conditions """
    n1, n2 = len(nums1), len(nums2)
    m2 = (n1 + n2) // 2 - m1

    return \
        all_left_are_lte(m1, nums1, get_element_or_none(m2, nums2)) and \
        all_left_are_lte(m2, nums2, get_element_or_none(m1, nums1))


def get_element_or_none(i: int, l: List[int]):
    n = len(l)
    if (i < 0) or (i >= n):
        return None
    else:
        return l[i]


def all_left_are_lte(i: int, l: List[int], target: int) -> bool:
    """ Get the left most element, strictly right of index 'i'.
        If there are no elements left of index 'i', will return None.

    :param i: index to separate all elements left of list <l>;
        elements left of <l> DO NOT INCLUDE the element l[i]
    :param l: a sorted list
    """
    if i <= 0:
        return True
    else:
        # this is when the target accessed is out of bounds
        # in which case all the elements left of i should
        # are lte the elements in the empty set
        if target is None:
            return True
        else:
            return l[i-1] <= target


def is_even(x: int) -> bool:
    return (x % 2) == 0


if __name__ == "__main__":

    sol = Solution()

    print("Found median: {}"
          .format(sol.findMedianSortedArrays([1,3,5,8,9], [2])))    # noqa [E231]

    print("Found median: {}"
          .format(sol.findMedianSortedArrays([1,2,3], [4,5,6])))    # noqa [E231]

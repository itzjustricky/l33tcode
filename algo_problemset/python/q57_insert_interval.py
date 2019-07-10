"""

57. Insert Interval
Hard
"""

import math

from typing import List
from typing import Tuple


class Solution:

    @staticmethod
    def binarySearchTarget(
            target: int, intervals: List[List[int]],
            lbnd: int, rbnd: int,
            *,
            right_inclusive: bool = False) -> int:
        """
        Binary search for the index for which the passed target is
        left of all the intervals to the inclusive right of the index.
        """
        mid = (rbnd + lbnd) // 2

        while (rbnd - lbnd) > 1:
            # if the target is within current interval then return it
            if intervals[mid][0] <= target <= intervals[mid][1]:
                return mid+1 if right_inclusive else mid
            elif target > intervals[mid][1]:
                lbnd = mid
            else:   # target < intervals[mid][0]
                rbnd = mid
            mid = (rbnd + lbnd) // 2

        # inside the left interval
        if intervals[lbnd][0] <= target <= intervals[lbnd][1]:
            return lbnd+1 if right_inclusive else lbnd
        # inside the right interval
        elif intervals[rbnd][0] <= target <= intervals[rbnd][1]:
            return rbnd+1 if right_inclusive else rbnd
        # left of the left interval
        elif target < intervals[lbnd][0]:
            return lbnd
        # right of the right interval
        elif target > intervals[rbnd][1]:
            return rbnd+1
        # between the end of the left interval and beginning of the right interval
        else:
            return rbnd

    def binarySearchInterval(
            self,
            interval: List[int],
            intervals: List[List[int]]) -> Tuple[int, int]:
        """
        Find where to insert the passed interval into intervals. If the returned
        tuples span more than one index then it means to merge the intervals.
        """
        n = len(intervals)
        lbnd = self.binarySearchTarget(interval[0], intervals, 0, n-1)
        if lbnd >= n: return n, n

        rbnd = self.binarySearchTarget(interval[1], intervals, lbnd, n-1,
                                       right_inclusive=True)
        return lbnd, rbnd

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0: return [newInterval]

        lbnd, rbnd = self.binarySearchInterval(newInterval, intervals)
        newInterval = [
            min(newInterval[0], intervals[lbnd][0] if lbnd < n else math.inf),
            max(newInterval[1], intervals[rbnd-1][1] if rbnd > 0 else -math.inf)]
        intervals = intervals[:lbnd] + [newInterval] + intervals[rbnd:]
        return intervals

"""

33. Search in Rotated Sorted Array
Medium
"""

from enum import Enum
from typing import List


class MidScenario(Enum):

    # scenario in which the middle index lies in
    # the tail end part of the array increasing to end at the middle of the list
    # e.g. the number '1' in the array [4,5,6,7,0,1,2]
    S1 = 0
    # scenario in which the middle index lies in
    # head part of the array increasing to end at the end of the list
    # e.g. the number '6' in the array [4,5,6,7,0,1,2]
    S2 = 1
    # the scenario of where the middle index lies in a sorted list
    # e.g. any number in the array [0,1,2,4,5,6,7]
    S3 = 2


class Solution:

    @staticmethod
    def identify_scenario(mid_val: int, left_val: int, right_val: int) -> MidScenario:
        if mid_val <= right_val:
            if mid_val <= left_val: return MidScenario.S1
            else: return MidScenario.S3
        else:
            if mid_val >= left_val: return MidScenario.S2
            else:
                raise ValueError(
                    "This situation should not be possible for a sorted array.")

    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return -1

        lbound, rbound = 0, len(nums)-1

        while (rbound - lbound) > 1:
            mid = (rbound + lbound) // 2
            scenario = self.identify_scenario(
                nums[mid], nums[lbound], nums[rbound])

            if scenario == MidScenario.S1:
                if (nums[mid] <= target <= nums[rbound]):
                    return binary_search(nums, target, mid, rbound)
                else:
                    rbound = mid
            elif scenario == MidScenario.S2:
                if (nums[lbound] <= target <= nums[mid]):
                    return binary_search(nums, target, lbound, mid)
                else:
                    lbound = mid
            # this is the scenario in which we can solve by binary search
            else:
                return binary_search(nums, target, lbound, rbound)

        if nums[lbound] == target:
            return lbound
        elif nums[rbound] == target:
            return rbound
        else:
            return -1


def binary_search(nums: List[int], target: int, start: int, end: int):
    lbound, rbound = start, end

    while (rbound - lbound) > 1:
        mid = (rbound + lbound) // 2
        if target <= nums[mid]:
            rbound = mid
        else:
            lbound = mid

    if nums[lbound] == target:
        return lbound
    elif nums[rbound] == target:
        return rbound
    else:
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.search([1,3,5], 1))  # noqa [E231]

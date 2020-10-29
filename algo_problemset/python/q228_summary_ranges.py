from typing import List


class Solution:

    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0: return []
        if n == 1: return [str(nums[0])]

        ranges = list()

        range_start, prev = nums[0], nums[0]
        for i in range(1, n):
            # not contiguous
            if nums[i] - prev > 1:
                range_string = str(range_start) if range_start == prev \
                    else "{}->{}".format(range_start, prev)
                ranges.append(range_string)
                range_start = nums[i]
            prev = nums[i]

        range_string = str(range_start) if range_start == prev \
            else "{}->{}".format(range_start, prev)
        ranges.append(range_string)

        return ranges

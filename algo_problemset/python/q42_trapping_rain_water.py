"""

42. Trapping Rain Water
"""

from typing import List


class Solution:

    def trap(self, height: List[int]) -> int:

        n = len(height)

        left_ind, right_ind = 0, n-1
        left_max, right_max = 0, 0

        trapped_water = 0

        while left_ind <= right_ind:
            if height[left_ind] < height[right_ind]:
                if height[left_ind] > left_max:
                    left_max = height[left_ind]
                else:
                    trapped_water += left_max - height[left_ind]
                left_ind += 1

            else:
                if height[right_ind] > right_max:
                    right_max = height[right_ind]
                else:
                    trapped_water += right_max - height[right_ind]
                right_ind -= 1

        return trapped_water

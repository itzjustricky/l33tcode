"""

70. Climbing Stairs
Easy
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1

        # simply a Fibonacci sequence
        prev_x, curr_x = 1, 2
        for i in range(n-2):
            curr_x, prev_x = curr_x+prev_x, curr_x
        return curr_x

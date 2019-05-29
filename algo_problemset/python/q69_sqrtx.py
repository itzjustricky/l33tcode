"""
69. Sqrt(x)
Easy
"""


class Solution:

    @staticmethod
    def sqrtBinarySearch(x: int) -> int:
        lbnd, rbnd = 0, x

        while (rbnd - lbnd) > 1:
            mid = (lbnd + rbnd) // 2
            mid_squared = mid**2

            if mid_squared == x:
                return mid
            elif mid_squared < x:
                lbnd = mid
            elif mid_squared > x:
                rbnd = mid

        if rbnd**2 > x:
            return lbnd
        else:
            return rbnd

    def mySqrt(self, x: int) -> int:
        return self.sqrtBinarySearch(x)

"""

50. Pow(x, n)
Medium
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            n = abs(n)
            init_multiplier = 1 / x
        else:
            init_multiplier = x

        x_pow_n = 1

        inc, multiplier = 1, init_multiplier
        while n > 0:

            # if increments are too large, restart
            if inc > n:
                inc, multiplier = 1, init_multiplier
            else:
                n -= inc
                x_pow_n *= multiplier

                # try a larger multiplier
                multiplier *= multiplier
                inc += inc

        return x_pow_n


if __name__ == "__main__":

    sol = Solution()
    print(sol.myPow(2.1, 3))
    print(sol.myPow(2.0, -2))

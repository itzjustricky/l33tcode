"""
29. Divide Two Integers
"""

import operator


class Solution:

    MIN = -2**31
    MAX = 2**31 - 1

    def will_overflow(self, a: int, b: int, *, inc_op) -> bool:
        if inc_op == operator.sub:
            return (self.MIN + b) >= a
        else:   # inc_op == operator.add
            return (self.MAX - b) <= a

    def divide(self, dividend: int, divisor: int) -> int:

        # the numbers are of different signs
        if is_non_negative(dividend) ^ is_non_negative(divisor):
            op, inc_op = operator.add, operator.sub
            is_positive = False
        else:
            op, inc_op = operator.sub, operator.add
            is_positive = True

        if is_non_negative(dividend):
            cont_condition = lambda x: x >= 0    # noqa [E731]
        else:
            cont_condition = lambda x: x <= 0    # noqa [E731]

        quotient = 0
        subtractor, quotient_inc = divisor, 1

        while cont_condition(op(dividend, divisor)):
            x = op(dividend, subtractor)

            # try again with smaller subtractor (i.e. subtractor = divisor)
            if not cont_condition(x):
                subtractor = divisor
                quotient_inc = 1
            else:
                dividend = x
                if self.will_overflow(quotient, quotient_inc, inc_op=inc_op):
                    return self.MAX if is_positive else self.MIN
                quotient = inc_op(quotient, quotient_inc)
                # try a subtractor and quotient-increment of double the size
                subtractor += subtractor; quotient_inc += quotient_inc

        return quotient


def is_non_negative(x: int) -> bool:
    return x >= 0


if __name__ == "__main__":
    sol = Solution()

    # print(sol.divide(10, 3))
    print(sol.divide(23942, 2))

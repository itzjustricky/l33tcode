import re
import operator
from itertools import product

from typing import List
from typing import Callable


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        # parse the input into numbers and operations
        # the first and last element of re.split(...) output are empty strings
        parsedInput = re.split("([0-9]+)", input)[1:-1]
        nums = list(map(int, parsedInput[::2]))
        ops = list(map(mapOperators, parsedInput[1::2]))

        return self.recursiveDiffWaysToCompute(nums, ops)

    def recursiveDiffWaysToCompute(self, nums: List[int], operations: List[Callable]) -> List[int]:
        # where len(nums) is n, len(operations) should be n-1
        n = len(nums)

        if n == 0: return []
        if n == 1: return [nums[0]]
        if n == 2: return [operations[0](nums[0], nums[1])]

        waysToCompute = list()
        for i in range(n-1):
            # split on i-th operation
            op = operations[i]
            left = self.recursiveDiffWaysToCompute(nums[:i+1], operations[:i])
            right = self.recursiveDiffWaysToCompute(nums[i+1:], operations[i+1:])

            waysToCompute.extend(
                op(x, y)
                for x, y in product(left, right))

        return waysToCompute


def mapOperators(op: str):
    return {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul
    }[op]


if __name__ == "__main__":
    print(Solution().diffWaysToCompute("2*3-4*5"))

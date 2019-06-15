"""

60. Permutation Sequence
Medium
"""

import math


class Solution:

    @staticmethod
    def generatePermutationChars(n: int, k: int):
        numbers = list(map(str, range(1, n+1)))
        fact = math.factorial(n-1)

        for x in reversed(range(1, n)):
            ind = math.ceil(k / fact) - 1
            yield numbers.pop(ind)

            k %= fact
            fact /= x
        yield numbers[0]

    def getPermutation(self, n: int, k: int) -> str:
        if k <= 0:
            raise ValueError("An invalid value of k was passed.")

        permutation = ''.join(self.generatePermutationChars(n, k))
        return permutation


if __name__ == "__main__":
    sol = Solution()
    print(sol.getPermutation(3, 3))
    print(sol.getPermutation(4, 9))

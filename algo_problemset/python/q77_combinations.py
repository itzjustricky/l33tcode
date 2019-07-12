"""

77. Combinations
Medium
"""

from typing import List


class Solution:

    def recursiveCombine(self, start: int, end: int, k: int) -> List[int]:
        if k == 0: return [[]]

        if (end - start) == k:
            return [list(range(start, end))]

        combinations = list()
        for x in range(start, end+1-k):
            combinations.extend([
                [x] + comb
                for comb in self.recursiveCombine(x+1, end, k-1)])
        return combinations

    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.recursiveCombine(1, n+1, k)

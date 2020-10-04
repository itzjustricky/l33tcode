import math
from typing import List
from typing import Tuple


class Solution:
    def minCut(self, s: str) -> int:
        self.cache = dict()

        # for each (i, j) entry in the matrix stores if the
        # substring s[i:j] is a palindrome
        self.palindromeCache = self.createPalindromeCacheMatrix(s)
        return self.recursiveMinCut(0, s)

    def recursiveMinCut(self, startInd: int, s: str) -> int:
        if startInd in self.cache: return self.cache[startInd]

        n = len(s)
        if startInd == n: return -1

        minCutCnt = math.inf
        for i in range(startInd, n):
            if self.palindromeCache[startInd][i]:
                # make a cut right after index i
                minCutCnt = min(minCutCnt, 1 + self.recursiveMinCut(i+1, s))

        self.cache[startInd] = minCutCnt
        return minCutCnt

    def createPalindromeCacheMatrix(self, s: str) -> List[List[bool]]:
        n = len(s)
        palinMatrix = [[False] * n for i in range(n)]

        for i in range(n):
            self.expandFromCenterAndUpdate((i, i), s, palinMatrix)
            self.expandFromCenterAndUpdate((i, i+1), s, palinMatrix)
        return palinMatrix

    def expandFromCenterAndUpdate(
            self,
            indTuple: Tuple[int, int],
            s: str, matrix: List[List[bool]]):
        leftInd, rightInd = indTuple

        n = len(s)
        while (leftInd >= 0) and (rightInd < n) and (s[leftInd] == s[rightInd]):
            matrix[leftInd][rightInd] = True
            leftInd -= 1; rightInd += 1

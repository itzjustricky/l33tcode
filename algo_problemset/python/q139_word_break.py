from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.cache = dict()
        self.wordDictSet = set(wordDict)
        return self.recursiveWordBreak(0, s)

    def recursiveWordBreak(self, startInd: int, s: str) -> bool:
        if startInd in self.cache: return self.cache[startInd]

        n = len(s)
        if (n - startInd) == 0: return True

        isBreakable = False
        for ind in range(startInd, n):
            if (s[startInd:(ind+1)] in self.wordDictSet) and \
                    self.recursiveWordBreak(ind+1, s):
                isBreakable = True

        self.cache[startInd] = isBreakable
        return isBreakable

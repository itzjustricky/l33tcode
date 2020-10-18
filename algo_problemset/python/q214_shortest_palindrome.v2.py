from typing import List


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s

        reversedString = s[::-1]
        lpsArray = computeLpsArray("#".join((s, reversedString)))

        return reversedString[:-lpsArray[-1]] + s


# compute the longest prefix-suffix array
def computeLpsArray(s: str) -> List[int]:
    n = len(s)
    lpsArray = [0 for i in range(n)]

    prefixEnd = 0
    for ind in range(1, n):
        while (prefixEnd > 0) and s[prefixEnd] != s[ind]:
            prefixEnd = lpsArray[prefixEnd-1]

        if s[prefixEnd] == s[ind]:
            lpsArray[ind] = prefixEnd + 1
            prefixEnd += 1

    return lpsArray

from typing import Tuple
from collections import deque


class Solution:
    def reverseWords(self, s: str) -> str:
        n, startIndex = len(s), 0
        reversedWords = deque()

        while startIndex < n:
            startIndex = self.findNextWordStart(startIndex, s)
            wordStart, wordEnd = self.grabNextWord(startIndex, s)
            # this only happens when we reach the end of the string
            if (wordEnd - wordStart) == 0: break
            reversedWords.appendleft(s[wordStart:wordEnd])

            startIndex = wordEnd
        return ' '.join(reversedWords)

    def grabNextWord(self, startIndex: int, s: str) -> Tuple[int, int]:
        ind, n = startIndex, len(s)
        while (ind < n) and (s[ind] != ' '):
            ind += 1
        return startIndex, ind

    def findNextWordStart(self, startIndex: int, s: str) -> int:
        ind, n = startIndex, len(s)
        while (ind < n) and (s[ind] == ' '):
            ind += 1
        return ind

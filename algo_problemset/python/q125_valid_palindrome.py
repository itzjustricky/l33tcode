class Solution:

    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n == 0: return True

        leftIndex, rightIndex = 0, len(s)-1
        while leftIndex < rightIndex:
            while (leftIndex < n) and (not s[leftIndex].isalnum()):
                leftIndex += 1
            while (rightIndex >= 0) and (not s[rightIndex].isalnum()):
                rightIndex -= 1

            if leftIndex >= rightIndex: return True
            if s[leftIndex].lower() != s[rightIndex].lower(): return False

            leftIndex += 1; rightIndex -= 1

        return True

"""
This solution fails with Time Exceeded
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # problem is equivalent to finding the largest
        # substring palindrome which starts from the first character

        n = len(s)
        if n == 0: return ''

        maxLength = 1
        for ind in reversed(range(n)):
            if self.isPalindrome(0, ind, s):
                maxLength = ind + 1
                break

        return s[maxLength:][::-1] + s

    def isPalindrome(self, left: int, right: int, s: str) -> bool:
        while (left < right):
            if s[left] != s[right]: return False
            left += 1; right -= 1

        return True


if __name__ == "__main__":
    print(
        Solution().shortestPalindrome("abcd")
    )

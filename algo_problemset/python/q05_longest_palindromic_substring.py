"""
    Question 5: Longest Palindromic Substring
    Medium

    Given a string s, find the longest palindromic substring in s.
    You may assume that the maximum length of s is 1000.

    Example 1:
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

    Example 2:
    Input: "cbbd"
    Output: "bb"
"""


class Solution:

    def longestPalindrome(self, s: str) -> str:

        longest_substring = ""

        s_length = len(s)
        if (s_length == 1): return s

        # for index i: longest_cache will store the length of
        # the longest palindrome starting from i
        longest_cache = [1 for i in range(s_length)]
        for i in reversed(range(s_length-1)):

            x = longest_cache[i+1]
            if ((i+x+1) < s_length) and (s[i+x+1] == s[i]):
                longest_cache[i] = x + 2
            elif ((i+2) < s_length) and (s[i] == s[i+2]):
                longest_cache[i] = 3
            elif (s[i] == s[i+1]):
                longest_cache[i] = 2

            if longest_cache[i] > len(longest_substring):
                longest_substring = s[i:(i+longest_cache[i])]

        return longest_substring


if __name__ == "__main__":
    sol = Solution()

    example1 = "babad"
    print("For example: {} got answer {}".format(example1, sol.longestPalindrome(example1)))

    example2 = "fdlbfbfbfbfbdbbdf"
    print("For example: {} got answer {}".format(example2, sol.longestPalindrome(example2)))

    example3 = "aaaa"
    print("For example: {} got answer {}".format(example3, sol.longestPalindrome(example3)))

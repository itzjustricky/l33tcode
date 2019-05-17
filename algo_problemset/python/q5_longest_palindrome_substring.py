"""
    5. Longest Palindrome Substring
    Medium

    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

    Example 1:
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

    Example 2:
    Input: "cbbd"
    Output: "bb"
"""

from typing import Tuple


class Solution:

    def get_longest_palindrome_on_center(
            self, center: int, s: str) -> Tuple[int, int]:
        """ Return the start and end index of a palindrome centered on
            the passed center index. The center index needs to be adjusted
            to represent an index on the actual string 's'.
        """
        if (center % 2) == 0:
            left_ind, right_ind = center // 2 - 1, center // 2 + 1
        else:
            left_ind, right_ind = center // 2, center // 2 + 1

        while (s[left_ind] == s[right_ind]):
            left_ind -= 1
            right_ind += 1

        return left_ind+1, right_ind-1

    def get_bounds(self, center, left, right):
        """ Convert bounds to the index of the tracker """
        if (center % 2) == 0:
            return center - left*2, center + right*2
        else:
            return center - left*2 + 1, center + right*2 - 1

    def get_mirror(self, center: int, i: int) -> int:
        dist = i - center
        return center - dist

    def longestPalindrome(self, s: str) -> str:
        s_length = len(s)
        longest_palindrome = ''
        if len(s) == 1: return s

        center_ind, left_bound, right_bound = 0, 0, 0
        # odd index indicates the center starts from between 2 characters
        # even index indicates the center revolves around an actual character
        palindrome_tracker = [1 for i in range(2*s_length - 1)]

        for i in range(1, 2*s_length - 1):
            if center_ind + s[left_bound]
            # if

        return longest_palindrome

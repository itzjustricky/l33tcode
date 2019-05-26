"""

Question 17. Letter Combinations of a Phone Number
"""

import itertools

from typing import List


class Solution:

    _number_map = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        letter_combos = self._number_map[digits[0]]
        for digit in digits[1:]:
            letter_combos = [
                pre+post
                for (pre, post) in itertools.product(letter_combos, self._number_map[digit])]

        return letter_combos

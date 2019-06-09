"""

58. Length of Last Word
Easy
"""


class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)

        start, word_length = 0, 0
        for i, char in enumerate(s):
            if char == ' ':
                _word_length = i - start
                # to handle cases where there are consecutive white-spaces
                word_length = _word_length if _word_length > 0 else word_length
                start = i+1

        # if the last character is not a whitespace
        if start != n: word_length = n - start
        return word_length

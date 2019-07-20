"""

68. Text Justification
Hard
"""

from typing import List


class Solution:

    def distributeSpaces(
            self, line_length: int, n_words: int, maxWidth: int) -> List[int]:
        """ Function to distribute spaces among the words """
        if n_words == 1:
            return [maxWidth - line_length]

        space_left = maxWidth - line_length
        per_word = space_left // (n_words - 1)
        extra_space = space_left - (per_word * (n_words-1))

        spaces = [
            per_word + (ind <= extra_space)
            for ind in range(1, n_words)]
        return spaces + [0]

    def distributeSpacesForLastLine(
            self, line_length: int, n_words: int, maxWidth: int) -> List[int]:
        """ Function to distribute spaces among the words """
        space_left = maxWidth - line_length
        spaces = [1 for i in range(1, n_words)] + \
                 [space_left - (n_words-1)]
        return spaces

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        text_justified_words = list()

        line_length = 0
        total_n_words = len(words)
        word_start, word_end = 0, 1

        for ind, word in enumerate(words):
            word_end = ind + 1
            line_length += len(word)

            # this is to capture the spacing between words
            n_words = word_end - word_start
            if (line_length + n_words - 1) >= maxWidth:

                # the words gathered won't fit on one line, this
                # one line will not include the current word
                if (line_length + n_words - 1) > maxWidth:
                    word_end = ind
                    n_words = word_end - word_start
                    line_length -= len(word)

                # last line is left justified
                if word_end == total_n_words:
                    spaces = self.distributeSpacesForLastLine(
                        line_length, n_words, maxWidth)
                else:
                    spaces = self.distributeSpaces(
                        line_length, n_words, maxWidth)

                text_justified_words.append(
                    ''.join(
                        words[j] + (' ' * spaces[i])
                        for i, j in enumerate(range(word_start, word_end))))

                word_start = word_end
                word_end = word_start + 1
                # include length of current word if new line starts at current word
                line_length = len(word) if (word_start == ind) else 0

        if word_start != total_n_words:
            n_words = word_end - word_start
            spaces = self.distributeSpacesForLastLine(
                line_length, n_words, maxWidth)
            text_justified_words.append(
                ''.join(
                    words[j] + (' ' * spaces[i])
                    for i, j in enumerate(range(word_start, word_end))))

        return text_justified_words


if __name__ == "__main__":

    sol = Solution()

    # Example 1:
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    expected = [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]
    answer = sol.fullJustify(words, maxWidth)
    assert answer == expected

    # Example 2:
    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth = 16
    expected = [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ]
    assert sol.fullJustify(words, maxWidth) == expected

    # Example 3:
    words = [
        "Science", "is", "what", "we", "understand", "well", "enough",
        "to", "explain", "to", "a", "computer.", "Art", "is", "everything",
        "else", "we", "do"]
    maxWidth = 20
    expected = [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  "
    ]
    assert sol.fullJustify(words, maxWidth) == expected

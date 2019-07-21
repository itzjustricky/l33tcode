"""

76. Minimum Window Substring
Hard
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # 'need' keeps count of the # of additional
        # letters needed for the letter
        n_letters_missing, need = len(t), Counter(t)
        start, end = 0, 0

        i = 0
        for j, let in enumerate(s, 1):
            if need[let] > 0:
                n_letters_missing -= 1

            need[let] -= 1

            if n_letters_missing == 0:
                # find the optimal starting point for this end point
                while (i < j) and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1

                if (end == 0) or ((j-i) < (end-start)):
                    start, end = i, j

                # optimal end was found for starting at 'i'
                # a more optimal window can only be found by
                # finding a new letter located at 'i'
                n_letters_missing += 1; need[s[i]] += 1; i += 1

        return s[start:end]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))

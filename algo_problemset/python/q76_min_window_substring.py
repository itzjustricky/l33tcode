"""

76. Minimum Window Substring
Hard
"""

from collections import deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_length = len(t)
        # mapping from <l> => Tuple[<# of letter allowed for used>, <deque>]
        # the deque is used to store the index of the letter when used
        char_dict = dict()
        for let in t:
            char_dict.setdefault(let, [0, deque()])
            char_dict[let][0] += 1

        min_window = None

        # Python deque implementation does not allow
        # O(1) node removal with reference to node
        used_letters_deque = deque()

        n_letters_used = 0
        for ind, let in enumerate(s):

            if let in char_dict:
                allowed_use, let_deque = char_dict[let]

                # replacing an already used character
                if len(let_deque) >= allowed_use:
                    # use list to hold the index, so can label as deleted (with None)
                    letter_ind = let_deque.popleft()
                    letter_ind[0] = None
                # unused spot for a character is being used
                else:
                    n_letters_used += 1

                used_letters_deque.append([ind])
                let_deque.append(used_letters_deque[-1])

                if n_letters_used >= t_length:
                    while used_letters_deque[0][0] is None:
                        used_letters_deque.popleft()

                    start, end = used_letters_deque[0][0], used_letters_deque[-1][0]
                    if min_window is None:
                        min_window = s[start:(end+1)]
                    elif (end - start + 1) < len(min_window):
                        min_window = s[start:(end+1)]

        return '' if min_window is None else min_window


if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))

"""

32. Longest Valid Parentheses
Hard
"""

from typing import List


class Solution:

    @staticmethod
    def findLongest(matching_parens: List[int]):
        s_length = len(matching_parens)

        prev_ind = 0
        length, max_length = 0, 0

        while prev_ind < s_length:
            ind = matching_parens[prev_ind]
            if ind == -1:
                prev_ind += 1
                length = 0
            else:
                length += ind - prev_ind + 1
                max_length = max(max_length, length)
                prev_ind = ind + 1
        return max_length

    def longestValidParentheses(self, s: str) -> int:
        s_length = len(s)

        num_stack = []
        matching_parens = [-1 for i in range(s_length)]

        for i, c in enumerate(s):
            if c == '(':
                num_stack.append(i)
            elif c == ')':
                if len(num_stack) > 0:
                    j = num_stack.pop()
                    matching_parens[j] = i
            else:
                raise ValueError(
                    "Invalid char '{}' was in passed string; should only "
                    "have '(' or ')'.".format(c))

        return self.findLongest(matching_parens)


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestValidParentheses("(()"))
    print(sol.longestValidParentheses(")()())"))
    print(sol.longestValidParentheses("()(()"))

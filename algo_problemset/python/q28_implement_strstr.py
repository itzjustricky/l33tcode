"""

28. Implement strStr
"""


class Solution:

    # this function assumes that starting from start_index until the end of
    # the <haystack> string, there are enough characters to match <needle>
    @staticmethod
    def matches(haystack: str, needle: str, start_index: int):
        needle_len = len(needle)

        haystack_ind = start_index
        for i in range(0, needle_len):
            if needle[i] != haystack[haystack_ind]:
                return False
            haystack_ind += 1

        return True

    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)

        if len(needle) == 0:
            return 0

        haystack_len = len(haystack)
        for i in range(0, haystack_len-needle_len+1):
            if self.matches(haystack, needle, i):
                return i

        return -1

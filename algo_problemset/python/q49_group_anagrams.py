"""

49. Group Anagrams
Medium
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = dict()
        for word in strs:
            group_dict.setdefault(tuple(sorted(word)), []).append(word)
        return list(group_dict.values())

"""

40. Combination Sum II
Medium
"""

from typing import List


class Solution:

    def recursiveFind(self, start_index: int, candidates: List[int], target: int):
        if (start_index, target) in self.hash:
            return self.hash[(start_index, target)]

        n_candidates = len(candidates)
        if start_index >= n_candidates:
            return []
        elif start_index == (n_candidates-1):
            combinations = \
                [[candidates[start_index]]] \
                if (candidates[start_index] == target) else []
            self.hash[(start_index, target)] = combinations
            return combinations

        prev_x = None
        combinations = list()
        for ind, x in enumerate(candidates[start_index:], start_index):
            if x == prev_x: continue
            # if all the remaining candidates are greater, can stop early
            if x > target: break

            if x == target: combinations.append([x])
            tmp_comb = self.recursiveFind(ind+1, candidates, target-x)
            if len(tmp_comb) > 0:
                combinations.extend([
                    [x] + y for y in tmp_comb])
            prev_x = x

        self.hash[(start_index, target)] = combinations
        return combinations

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # mapping from (start-index, target) => <list of combinations>
        self.hash = dict()
        candidates = sorted(candidates)
        return self.recursiveFind(0, candidates, target)

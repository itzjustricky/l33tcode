"""
    39. Combination Sum
    Medium

    Given a set of candidate numbers (candidates) (without duplicates) and
    a target number (target), find all unique combinations in candidates where
    the candidate numbers sums to target.

    The same repeated number may be chosen from candidates unlimited number of times.

    Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

    Example 1:
    Input: candidates = [2,3,6,7], target = 7,
    A solution set is:
    [
      [7],
      [2,2,3]
    ]

    Example 2:
    Input: candidates = [2,3,5], target = 8,
    A solution set is:
    [
      [2,2,2,2],
      [2,3,3],
      [3,5]
    ]
"""

from typing import List


class Solution:

    def recursiveSum(
            self,
            candidates: List[int], target: int,
            start_index: int) -> List[List[int]]:
        """
        Recursively find the combinations that sum to the target.

        :param start_index: indicates from which candidate we are allowed to use
        """
        if (target, start_index) in self._combo_hash:
            return self._combo_hash[(target, start_index)]

        all_found_sums = []
        for cand_ind, x in enumerate(candidates[start_index:], 1):

            # use this loop to try different multiples of x
            for ind in range(1, target//x + 1):
                x_mult = x * ind

                if x_mult == target:
                    all_found_sums.append([x] * ind)
                elif x_mult < target:
                    found_sums = self.recursiveSum(
                        candidates, target-x_mult, start_index+cand_ind)
                    if len(found_sums) > 0:
                        all_found_sums.extend(
                            [ind*[x] + combo for combo in found_sums])
                else:
                    break

        self._combo_hash[(target, start_index)] = all_found_sums
        return all_found_sums

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self._combo_hash = dict()

        candidates = sorted(candidates)
        combos = self.recursiveSum(candidates, target, 0)
        return combos


if __name__ == "__main__":
    sol = Solution()

    sum_combos = sol.combinationSum([1,2], 4)   # noqa [E231]
    print(sum_combos)

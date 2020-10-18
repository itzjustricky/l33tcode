from typing import List

from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        numIndexDict = defaultdict(list)
        # for each number gather the indices in which that number appears
        for ind, num in enumerate(nums):
            numIndexDict[num].append(ind)

        for num, indexList in numIndexDict.items():
            for i, j in zip(indexList[:-1], indexList[1:]):
                if (j - i) <= k:
                    return True

        return False

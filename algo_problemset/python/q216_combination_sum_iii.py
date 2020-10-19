from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # this is the max number 1-9 can sum up to
        if n > 45: return []

        if k == 9:
            if n == 45: return [list(range(1, 10))]
            else: return []

        # mapping of (bitmap, k) -> list of combinations
        self.cache = dict()
        # use an integer as a bit map, if the 'k'-th bit is 1 then it
        # means the number 'k' is taken
        takenBitMap = 0
        return self.recursiveCombinationSum3(k, n, 1, takenBitMap)

    def recursiveCombinationSum3(self, k: int, n: int, startNum: int, takenBitMap: int) -> List[List[int]]:
        if (takenBitMap, k) in self.cache:
            return self.cache[(takenBitMap, k)]

        # there should be no valid list for this because base case is k=1
        if n == 0:
            return []

        if k == 1:
            if (startNum <= n < 10) and isAvailable(n, takenBitMap):
                self.cache[(takenBitMap, k)] = [[n]]
                return self.cache[(takenBitMap, k)]
            else:
                return []

        combinations = []
        for ind in range(startNum, min(10, n+1)):
            if isAvailable(ind, takenBitMap):
                partialCombs = self.recursiveCombinationSum3(
                    k-1, n-ind, ind+1, takeBit(ind, takenBitMap))
                if len(partialCombs) > 0:
                    combinations.extend([[ind] + c for c in partialCombs])

        self.cache[(takenBitMap, k)] = combinations
        return combinations


def isAvailable(k: int, takenBitMap: int) -> bool:
    kthBit = (takenBitMap >> k) & 1
    return kthBit == 0


def takeBit(k: int, bitMap: int) -> int:
    return bitMap | (1 << k)

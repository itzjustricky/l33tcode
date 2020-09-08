from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        self.hasLooped = False

        surplusArray = [g-c for g, c in zip(gas, cost)]

        firstNonNegativeIndex = 0
        # look for positive index
        for ind, surplus in enumerate(surplusArray):
            if surplus >= 0:
                firstNonNegativeIndex = ind
                break

        gasStored = surplusArray[firstNonNegativeIndex]
        startPoint, ind = firstNonNegativeIndex, self.iterate(firstNonNegativeIndex, n)
        while True:
            gasStored += surplusArray[ind]

            # unable to go to next station
            if gasStored < 0:
                # current station has negative surplus, so start at next point
                startPoint, gasStored = self.iterate(ind, n), 0
                ind = startPoint

                # if new start point loops over 'firstNonNegativeIndex'
                # then there is no solution
                if (startPoint >= firstNonNegativeIndex) and self.hasLooped:
                    return -1

            else:
                ind = self.iterate(ind, n)
                if ind == startPoint:
                    return startPoint

    def iterate(self, ind: int, n: int):
        """ Use this function to iterate to wraparound when reaching end """
        if ind == n-1:
            self.hasLooped = True
            return 0
        else:
            return ind+1

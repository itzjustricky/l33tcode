"""

This is a O(n^2) solution that leads to time limit exceeded.
"""

import math

from typing import List
from typing import Tuple

from collections import deque


class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        self.cache = dict()
        return self.recursiveMaxProduct(0, nums)

    def recursiveMaxProduct(self, startIndex: int, nums: List[int]) -> int:
        if startIndex in self.cache:
            return self.cache[startIndex]

        n = len(nums)
        if (n - startIndex) == 1: return nums[0]

        maxProductTracker = -math.inf

        negativeInds, zeroInds = deque(), deque()
        # find all the negative numbers and zeros
        for ind, num in enumerate(nums[startIndex:], startIndex):
            if num < 0:
                negativeInds.append(ind)
            elif num == 0:
                zeroInds.append(ind)

        if len(zeroInds) > 0: maxProductTracker = 0

        currInd = startIndex
        # contiguous product tracker, will always be kept positive
        prodTracker = 1
        while (len(zeroInds) > 0) and (len(negativeInds) > 0):
            # if zero is closer than next negative number
            if zeroInds[0] < negativeInds[0]:
                zeroInd = zeroInds.popleft()

                prodTracker *= self.prodOverRange((currInd, zeroInd), nums)
                maxProductTracker = max(maxProductTracker, prodTracker)

                prodTracker, currInd = 1, zeroInd + 1
                if currInd in self.cache:
                    self.cache[startIndex] = max(maxProductTracker, self.cache[currInd])
                    return self.cache[startIndex]
            # the next two negative numbers are closer than the next zero
            elif (len(negativeInds) > 1) and (negativeInds[1] < zeroInds[0]):
                firstNeg = negativeInds.popleft()
                secondNeg = negativeInds.popleft()
                # consider case of starting on second negative index
                maxProductTracker = max(
                    maxProductTracker,
                    self.recursiveMaxProduct(firstNeg+1, nums))

                prodTracker *= self.prodOverRange((currInd, secondNeg+1), nums)
                maxProductTracker = max(maxProductTracker, prodTracker)
                currInd = secondNeg + 1
            # the next zero is between the next two negative numbers
            # or there is only one negative number left and zero is after it
            else:
                nextZero, nextNegative = zeroInds.popleft(), negativeInds.popleft()

                # consider the range tracked by prodTracker and also up until the next negative
                maxProductTracker = max(
                    maxProductTracker,
                    prodTracker * self.prodOverRange((currInd, nextNegative), nums))
                # consider the range between the negative and the zero
                maxProductTracker = max(
                    maxProductTracker,
                    self.prodOverRange((nextNegative+1, nextZero), nums))

                prodTracker, currInd = 1, nextZero + 1
                if currInd in self.cache:
                    self.cache[startIndex] = max(maxProductTracker, self.cache[currInd])
                    return self.cache[startIndex]

        # there's only negative #s or only zeros left (not both)

        # handle remaining negatives
        while len(negativeInds) > 0:
            if len(negativeInds) > 1:
                firstNeg = negativeInds.popleft()
                secondNeg = negativeInds.popleft()
                prodTracker *= self.prodOverRange((currInd, secondNeg+1), nums)

                # consider case of starting on second negative index
                maxProductTracker = max(
                    maxProductTracker,
                    self.recursiveMaxProduct(firstNeg+1, nums))

                maxProductTracker = max(maxProductTracker, prodTracker)
                currInd = secondNeg + 1
            # there's only one negative # left
            else:
                negInd = negativeInds.popleft()
                prodTracker *= self.prodOverRange((currInd, negInd), nums)

                maxProductTracker = max(maxProductTracker, prodTracker)
                prodTracker, currInd = 1, negInd + 1

        # handle remaining zeros
        while len(zeroInds) > 0:
            nextZero = zeroInds.popleft()
            prodTracker *= self.prodOverRange((currInd, nextZero), nums)
            maxProductTracker = max(maxProductTracker, prodTracker)

            prodTracker, currInd = 1, nextZero + 1

        # only positives left
        maxProductTracker = max(
            maxProductTracker,
            prodTracker * self.prodOverRange((currInd, n), nums))

        self.cache[startIndex] = maxProductTracker
        return maxProductTracker

    def prodOverRange(self, numRange: Tuple[int, int], nums: List[int]) -> int:
        start, end = numRange
        if (end - start) <= 0: return -math.inf

        prod = 1
        for num in nums[start:end]:
            prod *= num
        return prod


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.maxProduct([1,0,-1,2,3,-5,-2])  # noqa
    )

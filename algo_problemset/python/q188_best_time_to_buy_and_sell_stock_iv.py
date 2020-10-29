import math
from itertools import product

from typing import List


class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # handle some basic cases
        if (n == 0) or (k == 0): return 0
        # effectively can run any transaction wanted
        if 2 * k > n:
            return sum(max(0, prices[i] - prices[i-1]) for i in range(1, n))

        # store the max profit keyed by tuple (start, k, holding stock flag)
        maxProfitMatrix = [[[-math.inf] * 2 for j in range(k)] for i in range(n)]

        # on the last day
        for t in range(k):
            maxProfitMatrix[n-1][t][True] = prices[n-1]     # sell at last day's price
            maxProfitMatrix[n-1][t][False] = 0              # cannot sell if not holding

        # with one transactions left
        maxPrice, profitTracker = prices[n-1], 0
        for day in reversed(range(n)):
            maxPrice = max(maxPrice, prices[day])
            profitTracker = max(profitTracker, maxPrice - prices[day])
            maxProfitMatrix[day][1][True] = maxPrice            # sell at max price
            maxProfitMatrix[day][1][False] = profitTracker      # get largest single diff

        for t, day in product(range(1, k), reversed(range(n-1))):
            # holding the stock
            maxProfitMatrix[day][t][True] = max(
                prices[day] + maxProfitMatrix[day+1][t-1][False],   # sell the stock
                maxProfitMatrix[day+1][t][True])                    # continue holding

            # not holding the stock
            maxProfitMatrix[day][t][False] = max(
                -prices[day] + maxProfitMatrix[day+1][t][True],     # buy the stock
                maxProfitMatrix[day+1][t][False])                   # continue not holding

        return maxProfitMatrix[0][k-1][False]

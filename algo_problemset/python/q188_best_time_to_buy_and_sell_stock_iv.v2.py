import math
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if (k == 0) or (n == 0): return 0

        transactions = list()
        # capture all contiguous increasing subsequences
        prev, buyPoint = 0, 0
        for i in range(1, n):
            # if decrease then start new transaction
            if prices[prev] > prices[i]:
                if buyPoint != prev:
                    transactions.append([buyPoint, prev])
                buyPoint = i
            prev = i
        if prices[n-1] - prices[buyPoint] > 0:
            transactions.append([buyPoint, n-1])

        while len(transactions) > k:

            # determine loss for deleting a transaction
            deleteInd, deleteProfitLoss = None, math.inf
            for ind, (i, j) in enumerate(transactions):
                loss = prices[j] - prices[i]
                if loss < deleteProfitLoss:
                    deleteInd, deleteProfitLoss = ind, loss

            # determine loss for merging two transactions
            mergeInd, mergeProfitLoss = None, math.inf
            for ind, (t1, t2) in enumerate(zip(transactions[:-1], transactions[1:])):
                loss = t1[1] - t2[0]
                if loss < mergeProfitLoss:
                    mergeInd, mergeProfitLoss = ind, loss

            if deleteProfitLoss <= mergeProfitLoss:
                transactions.pop(deleteInd)
            else:
                t2 = transactions.pop(mergeInd+1)
                transactions[mergeInd][1] = t2[1]

        return sum(prices[j] - prices[i] for i, j in transactions)

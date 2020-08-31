from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0

        for x, y in zip(prices[:-1], prices[1:]):
            if y > x:
                profits += y - x

        return profits

"""

901. Online Stock Span
Medium
"""


class StockSpanner:

    def __init__(self):
        # lists of tuple (max-price, span)
        self.max_prices = list()

    def next(self, price: int) -> int:
        todays_span = 1

        while (len(self.max_prices) > 0) and (self.max_prices[-1][0] <= price):
            max_price, span = self.max_prices.pop()
            todays_span += span

        self.max_prices.append((price, todays_span))
        return todays_span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

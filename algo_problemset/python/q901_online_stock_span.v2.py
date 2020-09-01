class StockSpanner:

    def __init__(self):
        self.stack = list()

    def next(self, price: int) -> int:
        if (len(self.stack) == 0) or (price < self.stack[-1][0]):
            self.stack.append((price, 1))
        else:
            untilIndex = self.bisectLeft(price)
            accumulated = self.accumulateStack(untilIndex)
            self.stack.append((price, accumulated))

        return self.stack[-1][1]

    def bisectLeft(self, price: int) -> int:
        """
        Find index for which all prices left of index are higher than price
        Note: stack will be in sorted in reverse order
        """
        left, right = 0, len(self.stack)-1

        while (right - left) > 1:
            mid = (left + right) // 2
            if price <= self.stack[mid][0]:
                left = mid
            else:
                right = mid

        if price >= self.stack[left][0]:
            return left
        else:
            return right

    def accumulateStack(self, untilIndex: int) -> int:
        accumulated = 1
        numToAccumulate = len(self.stack) - untilIndex
        for i in range(numToAccumulate):
            accumulated += self.stack.pop()[1]
        return accumulated


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

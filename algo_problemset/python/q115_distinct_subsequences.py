
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.cache = dict()
        return self.recursiveNumDistinct(s, t)

    def recursiveNumDistinct(self, s: str, t: str) -> int:
        if (s, t) in self.cache:
            return self.cache[(s, t)]

        n, m = len(s), len(t)

        if (m == 0):
            self.cache[(s, t)] = 1
        elif (n < m):
            self.cache[(s, t)] = 0
        elif (m == 1):
            self.cache[(s, t)] = s.count(t)
        elif n == m:
            self.cache[(s, t)] = int(s == t)
        else:
            distinctCount = sum(
                self.recursiveNumDistinct(s[i+1:], t[1:])
                for i in range(n-m+1)
                if s[i] == t[0])
            self.cache[(s, t)] = distinctCount
        return self.cache[(s, t)]

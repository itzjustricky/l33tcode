from typing import List


class Solution:

    def partition(self, s: str) -> List[List[str]]:
        self.cache = dict()
        return self.recursivePartition(s)

    def recursivePartition(self, s: str) -> List[List[str]]:
        if len(s) == 0: return [[]]
        if len(s) == 1: return [[s]]

        if s in self.cache:
            return self.cache[s]

        partitions = list()

        n = len(s)
        for i in range(1, n+1):
            if self.isPalindrome(s[:i]):
                partitions.extend([
                    [s[:i]] + partition
                    for partition in self.recursivePartition(s[i:])])

        self.cache[s] = partitions
        return partitions

    @staticmethod
    def isPalindrome(s: str) -> bool:
        if len(s) == 1: return True

        leftInd, rightInd = 0, len(s)-1

        while leftInd < rightInd:
            if s[leftInd] != s[rightInd]:
                return False
            leftInd += 1; rightInd -= 1

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.partition("bb"))

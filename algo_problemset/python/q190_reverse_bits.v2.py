class Solution:
    def reverseBits(self, n: int) -> int:
        numberOfBits = 0, 32

        for ind in range(numberOfBits // 2):
            n = self.swapBits(ind, numberOfBits-ind-1, n)
        return n

    def swapBits(self, i: int, j: int, num: int) -> int:
        bit1 = (num >> i) & 1
        bit2 = (num >> j) & 1

        bitXor = bit1 ^ bit2
        return num ^ ((bitXor << i) | (bitXor << j))

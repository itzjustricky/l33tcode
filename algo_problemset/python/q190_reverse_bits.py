class Solution:
    def reverseBits(self, n: int) -> int:
        reversedBit, numberOfBits = 0, 32

        num = n
        backwardsCounter = numberOfBits - 1

        for ind in range(numberOfBits):
            bit = num % 2
            num //= 2

            if bit: reversedBit += 2**backwardsCounter
            backwardsCounter -= 1

        return reversedBit

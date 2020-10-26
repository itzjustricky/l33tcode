from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0: return 0
        n, m = len(matrix), len(matrix[0])

        # matrix to stores:
        # max length of square extending right/bottom from cell
        # sums of 1s going below
        # sums of 1s going to the right
        cacheMatrix = [[None for j in range(m)] for i in range(n)]

        maxSquareArea = 0

        bit = None
        # set cacheMatrix
        downSum = 0
        # most right column
        for i in reversed(range(n)):
            bit = 0 if matrix[i][m-1] == '0' else 1
            downSum = 0 if bit == 0 else downSum + 1
            cacheMatrix[i][m-1] = (bit, downSum, bit)
            if bit > 0: maxSquareArea = 1

        # bottom row
        rightSum = 0
        for j in reversed(range(m)):
            bit = 0 if matrix[n-1][j] == '0' else 1
            rightSum = 0 if bit == 0 else rightSum + 1
            # note rightSum for bottom row does not matter
            cacheMatrix[n-1][j] = (bit, bit, rightSum)
            if bit > 0: maxSquareArea = 1

        for i in reversed(range(0, n-1)):
            for j in reversed(range(0, m-1)):
                if matrix[i][j] == '0':
                    cacheMatrix[i][j] = (0, 0, 0)
                else:
                    downSum = cacheMatrix[i+1][j][1] + 1
                    rightSum = cacheMatrix[i][j+1][2] + 1

                    maxSquareLength = min(
                        downSum, rightSum,
                        cacheMatrix[i+1][j+1][0] + 1)

                    cacheMatrix[i][j] = (maxSquareLength, downSum, rightSum)
                    maxSquareArea = max(maxSquareArea, maxSquareLength**2)

        for x in cacheMatrix: print(x)
        return maxSquareArea


print(Solution().maximalSquare([
    ["0","1","1","0","0","1","0","1","0","1"],  # noqa
    ["0","0","1","0","1","0","1","0","1","0"],  # noqa
    ["1","0","0","0","0","1","0","1","1","0"],  # noqa
    ["0","1","1","1","1","1","1","0","1","0"],  # noqa
    ["0","0","1","1","1","1","1","1","1","0"],  # noqa
    ["1","1","0","1","0","1","1","1","1","0"],  # noqa
    ["0","0","0","1","1","0","0","0","1","0"],  # noqa
    ["1","1","0","1","1","0","0","1","1","1"],  # noqa
    ["0","1","0","1","1","0","1","0","1","1"]   # noqa
]))

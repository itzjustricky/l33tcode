from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        # bottom up approach
        minPathSum = triangle[-1]

        for i in reversed(range(n-1)):
            m = len(minPathSum)
            minPathSum = [
                min(triangle[i][j]+minPathSum[j], triangle[i][j]+minPathSum[j+1])
                for j in range(m-1)]

        return minPathSum[0]

"""

63. Unique Paths II
Medium
"""

import itertools
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])

        # if the starting point is an obstacle, then there is no way to move
        if obstacleGrid[0][0] == 1: return 0

        dp_matrix = [[1 for j in range(m)]
                     for i in range(n)]

        for i in range(1, n):
            dp_matrix[i][0] = 0 if obstacleGrid[i][0] else dp_matrix[i-1][0]
        for j in range(1, m):
            dp_matrix[0][j] = 0 if obstacleGrid[0][j] else dp_matrix[0][j-1]

        for i, j in itertools.product(range(1, n), range(1, m)):
            if obstacleGrid[i][j]:
                dp_matrix[i][j] = 0
            else:
                dp_matrix[i][j] = dp_matrix[i-1][j] + dp_matrix[i][j-1]

        return dp_matrix[n-1][m-1]

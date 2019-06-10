"""

64. Minimum Path Sum
Medium
"""

import itertools
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        dp_matrix = [[0 for j in range(m)]
                     for i in range(n)]

        dp_matrix[0][0] = grid[0][0]
        for j in range(1, m): dp_matrix[0][j] = dp_matrix[0][j-1] + grid[0][j]
        for i in range(1, n): dp_matrix[i][0] = dp_matrix[i-1][0] + grid[i][0]
        for i, j in itertools.product(range(1, n), range(1, m)):
            dp_matrix[i][j] = grid[i][j] + min(dp_matrix[i-1][j], dp_matrix[i][j-1])

        return dp_matrix[n-1][m-1]

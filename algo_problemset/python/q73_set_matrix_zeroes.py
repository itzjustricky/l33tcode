"""

73. Set Matrix Zeroes
Medium
"""

import itertools

from typing import List


class Solution:

    @staticmethod
    def setRowToZero(row: int, matrix: List[List[int]]):
        m = len(matrix[0])
        for i in range(m):
            matrix[row][i] = 0

    @staticmethod
    def setColToZero(col: int, matrix: List[List[int]]):
        n = len(matrix)
        for i in range(n):
            matrix[i][col] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        rows = [False for i in range(n)]
        cols = [False for i in range(m)]

        for i, j in itertools.product(range(n), range(m)):
            if matrix[i][j] == 0:
                rows[i], cols[j] = True, True

        for ind, row_bool in enumerate(rows):
            if row_bool: self.setRowToZero(ind, matrix)
        for ind, col_bool in enumerate(cols):
            if col_bool: self.setColToZero(ind, matrix)

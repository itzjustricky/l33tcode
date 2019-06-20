"""

73. Set Matrix Zeroes
Medium
"""

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

        # use the first row & col as special markers,
        # so must preserve this information
        zero_first_row = any((matrix[0][i] == 0) for i in range(m))
        zero_first_col = any((matrix[i][0] == 0) for i in range(n))

        # for i, j in itertools.product(range(1, n), range(1, m)):
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0

        for i in range(1, m):
            if matrix[0][i] == 0: self.setColToZero(i, matrix)
        for i in range(1, n):
            if matrix[i][0] == 0: self.setRowToZero(i, matrix)
        if zero_first_row: self.setRowToZero(0, matrix)
        if zero_first_col: self.setColToZero(0, matrix)

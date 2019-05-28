"""

48. Rotate Image
Medium
"""

from typing import List


class Solution:

    @staticmethod
    def _rotate_elements(row_ind: int, col_ind: int, matrix: List[List[int]]) -> None:
        n = len(matrix)

        def _convert_index(r: int, c: int):
            """ Return the index pair for the rotated element """
            return c, n - r - 1

        i, j = row_ind, col_ind
        stored_val = matrix[i][j]
        for ind in range(4):
            i2, j2 = _convert_index(i, j)
            # swap values
            stored_val, matrix[i2][j2] = matrix[i2][j2], stored_val
            # go to next rotated index
            i, j = i2, j2

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for i in range(0, n//2):
            for j in range(i, n-i-1):
                self._rotate_elements(i, j, matrix)


if __name__ == "__main__":

    sol = Solution()

    mat = [[1,2,3],[4,5,6],[7,8,9]]     # noqa [E231]
    sol.rotate(mat)

    print(mat)

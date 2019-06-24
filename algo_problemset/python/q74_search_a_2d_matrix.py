"""

74. Search a 2D Matrix
Medium
"""

from typing import List


class Solution:

    def binarySearchLeft(self, l: List[int], target: int):
        """ Find the index that is the largest number that is <= the target.
            If the target is the sorted list l then the index of the left-most
            number is returned.
        """
        left, right = 0, len(l)-1
        while (right-left) > 1:
            center = (left + right) // 2
            if target <= l[center]:
                right = center
            else:
                left = center
        if l[right] <= target:
            return right
        else:
            return left

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        elif len(matrix[0]) == 0:
            return False

        n_rows, n_cols = len(matrix), len(matrix[0])
        row_ind = self.binarySearchLeft(
            [matrix[i][0] for i in range(n_rows)], target)
        col_ind = self.binarySearchLeft(
            [matrix[row_ind][i] for i in range(n_cols)], target)
        return matrix[row_ind][col_ind] == target

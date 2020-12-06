from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        # only go up or go down
        i, j = 0, m-1
        while (i < n) and (j >= 0):
            val = matrix[i][j]
            if val == target:
                return True
            elif val < target:
                i += 1  # go down
            else:   # matrix[i][j] > target
                j -= 1  # go left

        return False

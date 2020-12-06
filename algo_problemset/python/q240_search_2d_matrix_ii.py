from typing import List


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n, m = len(matrix), len(matrix[0])
        if (n == 1) and (m == 1):
            return matrix[0][0] == target
        # has only one row
        elif (n == 1):
            col = binarySearch(target, 0, m, matrix[0])
            return (col < m) and (matrix[0][col] == target)
        # has only one column
        elif (m == 1):
            row = binarySearch(target, 0, n, [row[0] for row in matrix])
            return (row < n) and (matrix[row][0] == target)

        current = [0, 0]
        boundary = [n, m]

        while (current[0] < boundary[0]) and (current[1] < boundary[1]):

            # first binary search the row; update boundary on column
            boundary[1] = binarySearch(target, current[1], boundary[1], matrix[current[0]])
            if (boundary[1] < m) and (matrix[current[0]][boundary[1]] == target):
                return True
            # then binary search the column; update boundary on row
            boundary[0] = binarySearch(
                target, current[0], boundary[0],
                [row[current[1]] for row in matrix])
            if (boundary[0] < n) and (matrix[boundary[0]][current[1]] == target):
                return True

            current = [current[0] + 1, current[1] + 1]

        return False


def binarySearch(
        target: int,
        start: int,
        end: int,
        arr: List[int]) -> int:
    """ Inclusive on start, exclusive on end """

    l, r = start, end
    while (r - l) > 1:
        mid = (l + r) // 2

        if target <= arr[mid]:
            r = mid
        else:
            l = mid
    return l if target <= arr[l] else r


if __name__ == "__main__":

    Solution().searchMatrix(
        [[1,4],[2,5]],  # noqa
        6
    )

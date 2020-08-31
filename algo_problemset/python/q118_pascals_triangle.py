from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []

        triangle = [None] * numRows
        triangle[0] = [1]

        for i in range(1, numRows):
            triangle[i] = self.generateFromRow(triangle[i-1])
        return triangle

    def generateFromRow(self, previousRow: List[int]) -> List[int]:
        return \
            [1] + \
            [x+y for x, y in zip(previousRow[:-1], previousRow[1:])] + \
            [1]

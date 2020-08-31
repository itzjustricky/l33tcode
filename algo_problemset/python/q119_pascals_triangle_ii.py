from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowValues = [1]
        for ind in range(rowIndex):
            rowValues = self.generateFromRow(rowValues)

        return rowValues

    def generateFromRow(self, previousRow: List[int]) -> List[int]:
        return \
            [1] + \
            [x+y for x, y in zip(previousRow[:-1], previousRow[1:])] + \
            [1]

from typing import List
from math import factorial


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numerator = factorial(rowIndex)
        return [
            numerator // (factorial(rowIndex-ind) * factorial(ind))
            for ind in reversed(range(rowIndex+1))]

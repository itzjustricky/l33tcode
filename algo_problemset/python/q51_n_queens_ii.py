"""

51. N-Queens
Hard
"""

import math
from typing import List


class Solution:

    @staticmethod
    def eliminateSpaces(i: int, j: int, bit_map: List[List[bool]]) -> List[List[bool]]:
        """ Eliminate the spaces coming from a Queen at coordinate (i, j).
            Will only consider the lower rows because the upper rows are assumed to
            be taken.
        """
        n = len(bit_map)

        new_bit_map = bit_map.copy()
        # make copy of the rows below i
        for ind in range(i, n): new_bit_map[ind] = new_bit_map[ind].copy()

        # going down vertically
        _i = i+1
        while (_i < n):
            new_bit_map[_i][j] = False
            _i = _i+1

        _i, _j = i+1, j-1
        # going down lower left diagonal
        while (_i < n) and (_j >= 0):
            new_bit_map[_i][_j] = False
            _i, _j = _i+1, _j-1

        _i, _j = i+1, j+1
        # going down lower right diagonal
        while (_i < n) and (_j < n):
            new_bit_map[_i][_j] = False
            _i, _j = _i+1, _j+1

        return new_bit_map

    def backTrackAndSolve(
            self, row: int, bit_map: List[List[bool]]) -> int:
        """ Solve for solutions assuming upper rows are taken. """
        n = len(bit_map)

        # we are on last row
        if row == (n-1):
            n_solutions = sum(bit_map[row])
            return n_solutions

        n_solutions = 0
        for j in range(n):
            if bit_map[row][j]:
                _bit_map = self.eliminateSpaces(row, j, bit_map)
                n_solutions += self.backTrackAndSolve(row+1, _bit_map)
        return n_solutions

    def totalNQueens(self, n: int) -> int:
        if (n <= 0): return 0
        if (n == 1): return 1

        # represents the positions on the board that are free
        bit_map = [
            [True for j in range(n)]
            for i in range(n)]

        n_is_odd = (n % 2) != 0

        total_n_solutions = 0
        # small optimization, for the first row we only have to go
        # half the way by taking advantage of reflection
        for j in range(math.ceil(n / 2)):
            new_bit_map = self.eliminateSpaces(0, j, bit_map)
            n_solutions = self.backTrackAndSolve(1, new_bit_map)
            total_n_solutions += n_solutions
            # double count the solutions for the solutions reflected over middle
            if not (n_is_odd and j == (n // 2)):
                total_n_solutions += n_solutions

        return total_n_solutions


if __name__ == "__main__":
    from pprint import pprint

    sol = Solution()
    four_queens_sol = sol.solveNQueens(5)
    for sol_grid in four_queens_sol:
        for x in sol_grid:
            pprint(x)

        print()

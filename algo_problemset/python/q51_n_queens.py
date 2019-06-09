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
            self, row: int, bit_map: List[List[bool]], taken_positions: List[str]) -> List[List[str]]:
        """ Solve for solutions assuming upper rows are taken. """
        n = len(bit_map)

        # we are on last row
        if row == (n-1):
            solutions = [
                taken_positions + [self.createString(j, n)]
                for j in range(n) if bit_map[row][j]]
            return solutions

        solutions = []
        for j in range(n):
            if bit_map[row][j]:
                pos = self.createString(j, n)
                _bit_map = self.eliminateSpaces(row, j, bit_map)
                solutions.extend(
                    self.backTrackAndSolve(row+1, _bit_map, taken_positions + [pos]))
        return solutions

    @staticmethod
    def createString(j: int, n: int) -> str:
        return "{}{}{}".format(
            '.' * j, 'Q', '.' * (n-j-1))

    @staticmethod
    def reflectSolution(sols: List[List[str]]) -> List[List[str]]:
        def _reflect(sol: List[str]):
            return [''.join(reversed(s)) for s in sol]

        reflected_sols = [_reflect(sol) for sol in sols]
        return reflected_sols

    def solveNQueens(self, n: int) -> List[List[str]]:

        if (n <= 0): return [[]]
        if (n == 1): return [['Q']]

        # represents the positions on the board that are free
        bit_map = [
            [True for j in range(n)]
            for i in range(n)]

        n_is_odd = (n % 2) != 0

        solutions = []
        # small optimization, for the first row we only have to go
        # half the way by taking advantage of reflection
        for j in range(math.ceil(n / 2)):
            new_bit_map = self.eliminateSpaces(0, j, bit_map)
            new_solutions = self.backTrackAndSolve(1, new_bit_map, [self.createString(j, n)])
            if len(new_solutions) > 0:
                solutions.extend(new_solutions)

                # only reflect solutions that are not from placing queen
                # in the middle of the first row
                if not (n_is_odd and j == (n // 2)):
                    solutions.extend(self.reflectSolution(new_solutions))

        return solutions


if __name__ == "__main__":
    from pprint import pprint

    sol = Solution()
    four_queens_sol = sol.solveNQueens(5)
    for sol_grid in four_queens_sol:
        for x in sol_grid:
            pprint(x)

        print()

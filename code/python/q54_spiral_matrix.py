"""
    54. Spiral Matrix: Medium

    Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

    Example 1:
    Input:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    Output: [1,2,3,6,9,8,7,4,5]

    Example 2:
    Input:
    [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

from enum import Enum
from typing import List

from collections import namedtuple

# from functools import partial


class Move(Enum):
    up = 0
    down = 1
    left = 2
    right = 3

Boundary = namedtuple("Boundary", ["upper", "lower", "left", "right"])

_MOVE_MAP = {
    Move.up: lambda i, j: ((i-1), j),
    Move.down: lambda i, j: ((i+1), j),
    Move.left: lambda i, j: (i, (j-1)),
    Move.right: lambda i, j: (i, (j+1)),
}


class Solution:

    def _decideNextMove(
            self,
            i: int, j: int,
            *,
            last_move: Move,
            bounds: Boundary) -> tuple:
        """ This is a helper function to decide to output the new coordinates
            and the last move.
        """
        new_move = last_move
        # TODO: need to write code to fix move if hit boundary

        i, j = _MOVE_MAP[new_move](i, j)
        return (i, j, new_move)

    def spiralMatrix(self, initial_boundary: Boundary):
        coord, move = (0, 0), Move.right
        bounds = initial_boundary

        # while can move ...
        coord, move, bounds = self._decideNextMove(
            *coord, last_move=move, bounds=bounds)
        yield coord

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        initial_boundary = Boundary(0, len(matrix), 0, len(matrix[0]))
        return [
            matrix[i][j]
            for i, j in self.spiralMatrix(initial_boundary)]


if __name__ == "__main__":
    sol = Solution()

    sol.spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    sol.spiralOrder([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])

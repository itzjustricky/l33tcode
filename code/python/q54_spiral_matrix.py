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

import pprint
from enum import Enum
from typing import List

from collections import namedtuple


class Move(Enum):
    up = 0
    down = 1
    left = 2
    right = 3


MOVE_MAP = {
    Move.up: lambda i, j: ((i-1), j),
    Move.down: lambda i, j: ((i+1), j),
    Move.left: lambda i, j: (i, (j-1)),
    Move.right: lambda i, j: (i, (j+1)),
}


Boundary = namedtuple("Boundary", ["upper", "lower", "left", "right"])


def ternary_op(condition: bool, true_val, false_val):
    if condition:
        return true_val
    else:
        return false_val


class Solution:

    def _decideNextMove(
            self,
            i: int, j: int, *,
            move: Move, bounds: Boundary) -> tuple:
        """ This is a helper function to decide to output the new
            coordinates and the last move.
        """

        if move == Move.right:
            if (j+1 > bounds.right):
                bounds = bounds._replace(upper=bounds.upper+1)
                i += 1
                move = ternary_op(i > bounds.lower, None, Move.down)
                return (i, j, move, bounds)
        elif move == Move.down:
            if (i+1 > bounds.lower):
                bounds = bounds._replace(right=bounds.right-1)
                j -= 1
                move = ternary_op(j < bounds.left, None, Move.left)
                return (i, j, move, bounds)
        elif move == Move.left:
            if (j-1 < bounds.left):
                bounds = bounds._replace(lower=bounds.lower-1)
                i -= 1
                move = ternary_op(i < bounds.upper, None, Move.up)
                return (i, j, move, bounds)
        elif move == Move.up:
            if (i-1 < bounds.upper):
                bounds = bounds._replace(left=bounds.left+1)
                j += 1
                move = ternary_op(j > bounds.right, None, Move.right)
                return (i, j, move, bounds)
        else:
            raise ValueError("Unsupported move was passed.")

        i, j = MOVE_MAP[move](i, j)
        return (i, j, move, bounds)

    def _spiralMatrix(self, initial_boundary: Boundary):
        bounds = initial_boundary
        coord, move = (0, 0), Move.right

        while move is not None:
            yield coord
            *coord, move, bounds = self._decideNextMove(
                *coord, move=move, bounds=bounds)

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0: return []

        initial_boundary = Boundary(0, len(matrix)-1, 0, len(matrix[0])-1)
        return [
            matrix[i][j]
            for i, j in self._spiralMatrix(initial_boundary)]


if __name__ == "__main__":
    sol = Solution()

    mat1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("For matrix:\n{}\nGot solution:{}"
          .format(pprint.pformat(mat1), sol.spiralOrder(mat1)))

    mat2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print("For matrix:\n{}\nGot solution:{}"
          .format(pprint.pformat(mat2), sol.spiralOrder(mat2)))

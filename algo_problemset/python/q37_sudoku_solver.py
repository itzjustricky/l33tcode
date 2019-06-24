"""

37. Sudoku Solver
Hard
"""

import itertools

from typing import Set
from typing import List
from typing import Dict
from typing import Tuple

from typing import Union
from typing import NamedTuple


class Move(NamedTuple):
    """ A move in Sudoku is characterized by row, col to indicate the coordinate
        and a value from 1-9 to indicate what value is put at the coordinate.
    """
    row: int
    col: int
    value: int


# mapping from a 'box' to the row and columns indexed
# below rows/columns would be grouped, e.g. columns indexed by [0, 1, 2]
# will be one group and indexed by [3, 4, 5] will be another

GROUPS = {
    0: (0, 1, 2),
    1: (3, 4, 5),
    2: (6, 7, 8),
}

BOX_IND_MAP = {
    # mapping to tuple of (row-group, col-group)
    0: (0, 0),
    1: (0, 1),
    2: (0, 2),
    3: (1, 0),
    4: (1, 1),
    5: (1, 2),
    6: (2, 0),
    7: (2, 1),
    8: (2, 2),
}


class InvalidSudokuState(ValueError):
    """ Exception to signal a bad state """
    pass


class Solution:

    def findAvailableMoves(self, board: List[List[str]]) -> Dict[tuple, List[Move]]:
        """ Find all available moves which is just a cartesian product between
            available rows and available columns.
        """
        available_moves = dict()

        N = 9
        for i, j in itertools.product(range(N), range(N)):
            box_ind = self.convertToBoxInd(i, j)

            if board[i][j] == '.':
                available_moves[(i, j)] = [
                    Move(i, j, x)
                    for x in set.intersection(
                        self.rows[i], self.cols[j], self.boxes[box_ind])]

                if len(available_moves[(i, j)]) == 0:
                    raise InvalidSudokuState(
                        "For coordinate ({}, {}) there is no valid move available."
                        .format(i, j))
        return available_moves

    def findDeterministicMoves(self, board) -> Set[Move]:
        """ Find all the moves that definitely have to be made. Two types of
            determinstic moves are searched for:

                1. for any row/column/box, that only has one free number left then
                   then number must go in the only available spot left.
                2. for any free cell, if the free cell only has one 'available' move
                   then it is determinstic.
                3. for a given number in a box, it can only be put in one
                   coordinate within the box.
        """

        N = 9
        det_moves = set()
        # 1. for any row/column/box for which there is only element left
        for ind in range(N):
            if len(self.cols[ind]) == 1:
                x, = self.cols[ind]
                move = Move(*self.findEmptyCellInCol(ind, board), x)
                if not self.moveIsValid(move, board):
                    raise InvalidSudokuState(
                        "Last value available {} at column {} is not a valid move."
                        .format(x, ind))
                det_moves.add(move)
            if len(self.rows[ind]) == 1:
                x, = self.rows[ind]
                move = Move(*self.findEmptyCellInRow(ind, board), x)
                if not self.moveIsValid(move, board):
                    raise InvalidSudokuState(
                        "Last value available {} at row {} is not a valid move."
                        .format(x, ind))
                det_moves.add(move)
            if len(self.boxes[ind]) == 1:
                x, = self.boxes[ind]
                move = Move(*self.findEmptyCellInBox(ind, board), x)
                if not self.moveIsValid(move, board):
                    raise InvalidSudokuState(
                        "Last value available {} at box {} is not a valid move."
                        .format(x, ind))
                det_moves.add(move)

        # 2. for any free cell, there is only one available number
        available_moves = self.findAvailableMoves(board)
        for (i, j), moves in available_moves.items():
            if len(moves) == 1: det_moves.add(moves[0])

        # 3. within a box, there is one number that can only be put in one coordinate
        for box_ind in range(N):
            row_grp_ind, col_grp_ind = BOX_IND_MAP[box_ind]
            row_inds, col_inds = GROUPS[row_grp_ind], GROUPS[col_grp_ind]

            for num in self.boxes[box_ind]:
                allowed_inds = [
                    (i, j) for i, j in itertools.product(row_inds, col_inds)
                    if self.moveIsValid(Move(i, j, num), board)]
                if len(allowed_inds) == 0:
                    raise InvalidSudokuState(
                        "For value {}, there is no valid spot to place it in box {}."
                        .format(num, box_ind))
                if len(allowed_inds) == 1:
                    det_moves.add(Move(*allowed_inds[0], num))

        return det_moves

    def findEmptyCellInBox(
            self, box_ind: int, board: List[List[str]]) -> Tuple[int, int]:
        """ For a given box, return back the index of row, column which is empty """

        row_group_ind, col_group_ind = BOX_IND_MAP[box_ind]

        for i, j in itertools.product(GROUPS[row_group_ind], GROUPS[col_group_ind]):
            if board[i][j] == '.': return i, j

        raise ValueError("There is no empty cell in the Box indexed by {}."
                         .format(box_ind))

    def findEmptyCellInRow(self, row: int, board: List[List[str]]) -> int:
        """ For a given row, return back the index of the row, column which is empty """
        N = 9
        for i in range(N):
            if board[row][i] == '.':
                return row, i
        raise ValueError("There is no empty cell in the Box indexed by {}."
                         .format(row))

    def findEmptyCellInCol(self, col: int, board: List[List[str]]) -> int:
        """ For a given col, return back the index of the row, column which is empty """
        N = 9
        for i in range(N):
            if board[i][col] == '.':
                return i, col
        raise ValueError("There is no empty cell in the column indexed by {}."
                         .format(col))

    @staticmethod
    def convertToBoxInd(row: int, col: int) -> int:
        """ Get the index of the box for the passed coordinate """
        return 3 * (row//3) + col//3

    def executeMove(self, move: Move, board: List[List[str]]):
        """ Execute a move onto the board """
        i, j, val = move
        box_ind = self.convertToBoxInd(i, j)

        self.rows[i].remove(val)
        self.cols[j].remove(val)
        self.boxes[box_ind].remove(val)
        board[i][j] = val

    def undoMove(self, move: Move, board: List[List[str]]):
        """ Undo a move onto the board """
        i, j, val = move
        box_ind = self.convertToBoxInd(i, j)

        self.rows[i].add(val)
        self.cols[j].add(val)
        self.boxes[box_ind].add(val)
        board[i][j] = '.'

    def moveIsValid(self, move: Move, board: List[List[str]]) -> bool:
        i, j, val = move
        box_ind = self.convertToBoxInd(i, j)
        return (board[i][j] == '.') and \
            (val in self.rows[i]) and \
            (val in self.cols[j]) and \
            (val in self.boxes[box_ind])

    def isCompleted(self, board) -> bool:
        N = 9
        return all(
            board[i][j] != '.'
            for i, j in itertools.product(range(N), range(N)))

    def recursiveSolveSudoku(
            self,
            board: List[List[str]],
            available_moves: Union[None, dict] = None) -> bool:
        """ Recursively solve the Sudoku board

        :returns: True if was able to solve the board
        """

        # execute all moves that are deterministic given the current state of the board
        # all_definite_moves = set()
        definite_moves_executed = set()
        while True:
            try:
                definite_moves = self.findDeterministicMoves(board)

                if len(definite_moves) == 0: break
                for ind, move in enumerate(definite_moves):
                    if self.moveIsValid(move, board):
                        definite_moves_executed.add(move)
                        self.executeMove(move, board)
                    else:
                        raise InvalidSudokuState(
                            "Found deterministic move ({}) that was invalid.".format(move))
            except InvalidSudokuState:
                # got a deterministic move that is invalid, board is
                # a state such that it cannot be completed, revert and return False
                for move in definite_moves_executed: self.undoMove(move, board)
                return False

        if available_moves is None:
            available_moves = self.findAvailableMoves(board)

        if len(available_moves) == 0:
            if self.isCompleted(board): return True
            else:
                for move in definite_moves_executed:
                    self.undoMove(move, board)

        _available_moves = available_moves.copy()
        for (i, j), moves in available_moves.items():

            _available_moves.pop((i, j))
            for move in moves:
                if self.moveIsValid(move, board):
                    self.executeMove(move, board)
                else:
                    continue

                if self.recursiveSolveSudoku(board, _available_moves):
                    return True
                else:
                    # the move could not lead to solving the sudoku board
                    self.undoMove(move, board)

        # Executing any of the available moves did not work so undo everything
        for move in definite_moves_executed:
            self.undoMove(move, board)
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N = 9

        self.rows = [set(map(str, range(1, 10))) for i in range(N)]
        self.cols = [set(map(str, range(1, 10))) for i in range(N)]
        self.boxes = [set(map(str, range(1, 10))) for i in range(N)]

        # initialize state according to the configured board
        for i, j in itertools.product(range(N), range(N)):
            x = board[i][j]
            box_ind = self.convertToBoxInd(i, j)
            if x != '.':
                self.rows[i].remove(x)
                self.cols[j].remove(x)
                self.boxes[box_ind].remove(x)

        self.recursiveSolveSudoku(board)


if __name__ == "__main__":

    # board = [
    #     ['.','9','.','.','.','.','.','.','2'],    # noqa [E231]
    #     ['.','.','.','7','.','5','.','9','8'],    # noqa [E231]
    #     ['.','.','8','3','.','.','4','.','.'],    # noqa [E231]
    #     ['.','1','.','8','7','9','3','2','5'],    # noqa [E231]
    #     ['.','.','2','5','.','4','7','.','.'],    # noqa [E231]
    #     ['7','5','9','2','3','6','.','1','.'],    # noqa [E231]
    #     ['.','.','3','.','.','7','5','.','.'],    # noqa [E231]
    #     ['2','7','.','4','.','3','.','.','.'],    # noqa [E231]
    #     ['9','.','.','.','.','.','.','7','.'],    # noqa [E231]
    # ]

    # board = [
    #     ["5","3",".",".","7",".",".",".","."],    # noqa [E231]
    #     ["6",".",".","1","9","5",".",".","."],    # noqa [E231]
    #     [".","9","8",".",".",".",".","6","."],    # noqa [E231]
    #     ["8",".",".",".","6",".",".",".","3"],    # noqa [E231]
    #     ["4",".",".","8",".","3",".",".","1"],    # noqa [E231]
    #     ["7",".",".",".","2",".",".",".","6"],    # noqa [E231]
    #     [".","6",".",".",".",".","2","8","."],    # noqa [E231]
    #     [".",".",".","4","1","9",".",".","5"],    # noqa [E231]
    #     [".",".",".",".","8",".",".","7","9"]     # noqa [E231]
    # ]

    # board = [
    #     [".",".","9","7","4","8",".",".","."],    # noqa [E231]
    #     ["7",".",".",".",".",".",".",".","."],    # noqa [E231]
    #     [".","2",".","1",".","9",".",".","."],    # noqa [E231]
    #     [".",".","7",".",".",".","2","4","."],    # noqa [E231]
    #     [".","6","4",".","1",".","5","9","."],    # noqa [E231]
    #     [".","9","8",".",".",".","3",".","."],    # noqa [E231]
    #     [".",".",".","8",".","3",".","2","."],    # noqa [E231]
    #     [".",".",".",".",".",".",".",".","6"],    # noqa [E231]
    #     [".",".",".","2","7","5","9",".","."]     # noqa [E231]
    # ]

    # board = [
    #     ['6','7','.','.','5','.','.','.','.'],      # noqa [E231]
    #     ['.','.','.','7','.','6','8','.','4'],      # noqa [E231]
    #     ['.','.','.','.','.','3','2','.','.'],      # noqa [E231]
    #     ['8','.','.','6','2','.','.','.','.'],      # noqa [E231]
    #     ['4','2','.','1','.','5','.','9','8'],      # noqa [E231]
    #     ['.','.','.','.','9','7','.','.','1'],      # noqa [E231]
    #     ['.','.','6','3','.','.','.','.','.'],      # noqa [E231]
    #     ['1','.','2','5','.','9','.','.','.'],      # noqa [E231]
    #     ['.','.','.','.','4','.','.','6','5'],      # noqa [E231]
    # ]

    board = [
        [".",".",".","2",".",".",".","6","3"],        # noqa [E231]
        ["3",".",".",".",".","5","4",".","1"],        # noqa [E231]
        [".",".","1",".",".","3","9","8","."],        # noqa [E231]
        [".",".",".",".",".",".",".","9","."],        # noqa [E231]
        [".",".",".","5","3","8",".",".","."],        # noqa [E231]
        [".","3",".",".",".",".",".",".","."],        # noqa [E231]
        [".","2","6","3",".",".","5",".","."],        # noqa [E231]
        ["5",".","3","7",".",".",".",".","8"],        # noqa [E231]
        ["4","7",".",".",".","1",".",".","."]         # noqa [E231]
    ]

    from pprint import pprint

    sol = Solution()
    sol.solveSudoku(board)
    pprint(board)

"""

79. Word Search
Medium
"""

import itertools

from typing import List
from typing import Tuple


class Solution:

    def getNeighbors(
            self, coord: Tuple[int, int], visited: List[List[bool]]):

        neighbors = list()
        n, m = len(visited), len(visited[0])

        row, col = coord
        if (row > 0) and (not visited[row-1][col]):
            neighbors.append((row-1, col))
        if (row < n-1) and (not visited[row+1][col]):
            neighbors.append((row+1, col))
        if (col > 0) and (not visited[row][col-1]):
            neighbors.append((row, col-1))
        if (col < m-1) and (not visited[row][col+1]):
            neighbors.append((row, col+1))

        return neighbors

    def searchBoardDFS(self, start_coords: List[Tuple[int, int]], board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        visited = [
            [False for j in range(m)]
            for i in range(n)]

        n_letters = len(word)

        path = []
        # stack will store Lists of coordinates; each list will
        # store neighboring coordinates of those popped from list below it
        stack = [start_coords]

        while len(stack) > 0:
            if len(path) == n_letters:
                return True

            if len(stack[-1]) == 0:
                if len(path) > 0:
                    row, col = path.pop()
                    visited[row][col] = False
                stack.pop()
            else:
                row, col = stack[-1].pop()
                if board[row][col] == word[len(path)]:
                    path.append((row, col))
                    stack.append(self.getNeighbors((row, col), visited))
                    visited[row][col] = True
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        first_letter = word[0]
        start_coords = [
            (i, j) for i, j in itertools.product(range(n), range(m))
            if board[i][j] == first_letter]

        return self.searchBoardDFS(start_coords, board, word)

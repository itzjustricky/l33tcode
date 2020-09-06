from typing import List
from typing import Tuple


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n == 0: return
        m = len(board[0])
        if m == 0: return

        visited = [[False] * m for i in range(n)]

        oPointsAlongBorder = self.findOPointsAlongBorder(board)

        for point in oPointsAlongBorder:
            self.bfsFromPoint(point, board, visited)

        for i in range(1, n-1):
            for j in range(1, m-1):
                if not visited[i][j]:
                    board[i][j] = 'X'

    def findOPointsAlongBorder(self, board: List[List[str]]) -> List[Tuple[int, int]]:

        n, m = len(board), len(board[0])
        oPoints = list()

        for i in range(n):
            if board[i][0] == 'O':
                oPoints.append((i, 0))
            if board[i][m-1] == 'O':
                oPoints.append((i, m-1))
        for j in range(m):
            if board[0][j] == 'O':
                oPoints.append((0, j))
            if board[n-1][j] == 'O':
                oPoints.append((n-1, j))

        return oPoints

    def bfsFromPoint(
            self,
            startPoint: Tuple[int, int],
            board: List[List[str]],
            visited: List[List[bool]]):

        pointsToVisit = [startPoint]
        while len(pointsToVisit) > 0:

            newPointsToVisit = []
            for point in pointsToVisit:
                for neighbor in self.getNeighbors(point, board):
                    ni, nj = neighbor
                    if not visited[ni][nj]:
                        newPointsToVisit.append(neighbor)
                        visited[ni][nj] = True

            pointsToVisit = newPointsToVisit

    def getNeighbors(self, point: Tuple[int, int], board: List[List[str]]):

        n, m = len(board), len(board[0])
        neighbors = list()

        i, j = point
        if (i > 0) and (board[i-1][j] == 'O'):
            neighbors.append((i-1, j))
        if (i < n-1) and (board[i+1][j] == 'O'):
            neighbors.append((i+1, j))
        if (j > 0) and (board[i][j-1] == 'O'):
            neighbors.append((i, j-1))
        if (j < m-1) and (board[i][j+1] == 'O'):
            neighbors.append((i, j+1))
        return neighbors

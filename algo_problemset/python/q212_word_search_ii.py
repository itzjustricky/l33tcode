from typing import List
from typing import Tuple

from itertools import product
from collections import defaultdict


class TrieNode:

    __slots__ = ["charDict", "isWordEnd"]

    def __init__(self):
        self.charDict = dict()
        self.isWordEnd = False

    def insert(self, word: str):
        nodePtr = self

        for char in word:
            if char not in nodePtr.charDict:
                nodePtr.charDict[char] = TrieNode()
            nodePtr = nodePtr.charDict[char]
        nodePtr.isWordEnd |= True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(words) == 0: return []

        self.trieHead = TrieNode()
        self.lettersMap = defaultdict(list)
        for word in words:
            self.trieHead.insert(word)

        self.board = board

        self.presentWords = set()
        n, m = len(board), len(board[0])
        for i, j in product(range(n), range(m)):
            c = board[i][j]
            if c in self.trieHead.charDict:
                self.searchTrieInBoard((i, j), c, self.trieHead.charDict[c])

        return list(self.presentWords)

    def searchTrieInBoard(
            self,
            start: Tuple[int, int],
            trackedWord: str,
            trieNode: TrieNode):
        i, j = start
        self.board[i][j] = '#'   # mark as taken

        if trieNode.isWordEnd:
            self.presentWords.add(trackedWord)

        if len(trieNode.charDict) > 0:
            neighbors = getNeighbors(start, self.board)
            for neighbor in neighbors:
                i2, j2 = neighbor
                c = self.board[i2][j2]
                if c in trieNode.charDict:
                    self.searchTrieInBoard(neighbor, trackedWord + c, trieNode.charDict[c])

        self.board[i][j] = trackedWord[-1]  # unmark


def getNeighbors(
        coord: Tuple[int, int],
        board: List[List[str]]) -> List[Tuple[int, int]]:
    n, m = len(board), len(board[0])

    i, j = coord
    neighbors = list()
    if (i+1 < n) and (board[i+1][j] != '#'):
        neighbors.append((i+1, j))
    if (i-1 >= 0) and (board[i-1][j] != '#'):
        neighbors.append((i-1, j))
    if (j+1 < m) and (board[i][j+1] != '#'):
        neighbors.append((i, j+1))
    if (j-1 >= 0) and (board[i][j-1] != '#'):
        neighbors.append((i, j-1))
    return neighbors

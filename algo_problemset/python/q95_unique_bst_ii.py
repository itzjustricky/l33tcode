from itertools import product
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n <= 0: return []

        self.generatedTreeHash = dict()
        return self.recursiveGenerateTrees(1, n)

    def recursiveGenerateTrees(self, start: int, end: int) -> List[TreeNode]:
        if (start, end) in self.generatedTreeHash:
            return self.generatedTreeHash[(start, end)]

        if (end - start) < 0:
            return [None]
        elif (end - start) == 0:
            self.generatedTreeHash[(start, end)] = [TreeNode(end)]
            return self.generatedTreeHash[(start, end)]

        generatedTrees = list()
        for splitInd in range(start, end+1):
            leftSubtrees = self.recursiveGenerateTrees(start, splitInd-1)
            rightSubtrees = self.recursiveGenerateTrees(splitInd+1, end)

            for leftStree, rightSTree in product(leftSubtrees, rightSubtrees):
                newTree = TreeNode(splitInd)
                newTree.left, newTree.right = leftStree, rightSTree
                generatedTrees.append(newTree)

        self.generatedTreeHash[(start, end)] = generatedTrees
        return self.generatedTreeHash[(start, end)]

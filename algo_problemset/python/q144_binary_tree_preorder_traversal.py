from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: return []

        nodePtr, nodeStack = None, deque([root])

        traversalList = list()

        while len(nodeStack) > 0:
            nodePtr = nodeStack.pop()
            traversalList.append(nodePtr.val)

            if nodePtr.right is not None:
                nodeStack.append(nodePtr.right)
            if nodePtr.left is not None:
                nodeStack.append(nodePtr.left)

        return traversalList

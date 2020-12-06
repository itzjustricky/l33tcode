from enum import Enum


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class PathDirection(Enum):
    LEFT = 1
    RIGHT = 2


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pPath = findTreePathTo(root, p)
        qPath = findTreePathTo(root, q)

        nodePtr = root
        for pPathDir, qPathDir in zip(pPath, qPath):
            if pPathDir != qPathDir:
                return nodePtr

            if pPathDir == PathDirection.LEFT:
                nodePtr = nodePtr.left
            else:   # pPathDir == PathDirection.RIGHT
                nodePtr = nodePtr.right

        # for the case that one of the nodes is the LCA
        # the path of one node is longer than the other
        return nodePtr


def findTreePathTo(root: 'TreeNode', node: 'TreeNode'):
    if root is None:
        return None
    if root == node:
        return []

    leftPath = findTreePathTo(root.left, node)
    if leftPath is not None:
        return [PathDirection.LEFT] + leftPath

    rightPath = findTreePathTo(root.right, node)
    if rightPath is not None:
        return [PathDirection.RIGHT] + rightPath

    return None

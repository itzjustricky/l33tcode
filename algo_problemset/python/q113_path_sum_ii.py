from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        return self.recursivePathSum(root, sum, [])

    def recursivePathSum(self, root: TreeNode, sum: int, trackedPath: list) -> List[List[int]]:

        if root is None: return []

        collectedPathSums = list()

        hasLeftChild, hasRightChild = root.left is not None, root.right is not None
        isLeaf = (not hasLeftChild) and (not hasRightChild)

        if isLeaf:
            if sum == root.val:
                collectedPathSums.append(trackedPath + [root.val])
        else:
            if hasLeftChild:
                collectedPathSums.extend(
                    self.recursivePathSum(root.left, sum-root.val, trackedPath + [root.val]))
            if hasRightChild:
                collectedPathSums.extend(
                    self.recursivePathSum(root.right, sum-root.val, trackedPath + [root.val]))

        return collectedPathSums

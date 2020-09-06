import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # it is assumed that the binary tree passed is non-empty
        self.maxPathSumTracker = -math.inf
        self.recursiveDownPathSum(root)
        return self.maxPathSumTracker

    def recursiveDownPathSum(self, node: TreeNode) -> int:
        """
        This returns the max path sum going down either left or right child.
        With a side-effect of update to the self.maxPathSumTracker value
        """
        leftForkSum, rightForkSum = 0, 0
        maxPathSumSplitOnNode = node.val

        if not self.isLeaf(node):
            if node.left is not None:
                leftForkSum = self.recursiveDownPathSum(node.left)
                maxPathSumSplitOnNode = max(
                    maxPathSumSplitOnNode, maxPathSumSplitOnNode+leftForkSum)
            if node.right is not None:
                rightForkSum = self.recursiveDownPathSum(node.right)
                maxPathSumSplitOnNode = max(
                    maxPathSumSplitOnNode, maxPathSumSplitOnNode+rightForkSum)

        # update max path sum so far with using the current node as the 'split node'
        self.maxPathSumTracker = max(self.maxPathSumTracker, maxPathSumSplitOnNode)

        # return the max path sum that can be achieved without splitting on current node
        #   (i.e. going only down either left or right and potentially splitting
        #    someone higher up the tree)
        return max(node.val, node.val+leftForkSum, node.val+rightForkSum)

    @staticmethod
    def isLeaf(node: TreeNode):
        return (node.left is None) and (node.right is None)

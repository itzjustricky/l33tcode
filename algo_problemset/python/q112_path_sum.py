# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if root is None: return False

        hasLeftChild, hasRightChild = root.left is not None, root.right is not None
        isLeaf = (not hasLeftChild) and (not hasRightChild)
        if isLeaf and (sum == root.val):
            return True
        if hasLeftChild and self.hasPathSum(root.left, sum-root.val):
            return True
        if hasRightChild and self.hasPathSum(root.right, sum-root.val):
            return True

        return False

"""
226. Invert Binary Tree
Easy
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def recursiveInvert(self, node: TreeNode):
        if node is None:
            return

        node.left, node.right = node.right, node.left
        self.recursiveInvert(node.left)
        self.recursiveInvert(node.right)

    def invertTree(self, root: TreeNode) -> TreeNode:
        self.recursiveInvert(root)
        return root

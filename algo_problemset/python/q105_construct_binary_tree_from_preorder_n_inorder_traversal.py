from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])

        # the next node in preorder is the right subtree root
        if root.val == inorder[0]:
            root.right = self.buildTree(preorder[1:], inorder[1:])
        # the next node in preorder is the left subtree root
        else:
            leftSubtreeSize = inorder.index(root.val)
            root.left = self.buildTree(preorder[1:leftSubtreeSize+1], inorder[:leftSubtreeSize])
            root.right = self.buildTree(preorder[leftSubtreeSize+1:], inorder[leftSubtreeSize+1:])

        return root

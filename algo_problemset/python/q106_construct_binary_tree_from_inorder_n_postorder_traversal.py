from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        if len(postorder) == 0: return None
        if len(postorder) == 1: return TreeNode(postorder[0])

        root = TreeNode(postorder[-1])

        leftSubtreeSize = inorder.index(root.val)
        if leftSubtreeSize == 0:
            root.right = self.buildTree(inorder[1:], postorder[:-1])
        else:
            root.left = self.buildTree(inorder[:leftSubtreeSize], postorder[:leftSubtreeSize])
            root.right = self.buildTree(inorder[leftSubtreeSize+1:], postorder[leftSubtreeSize:-1])

        return root

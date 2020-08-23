import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None: return root

        stack = list()
        badNode, prevNode, iterNode = None, TreeNode(-math.inf), root

        # inorder traversal of tree using stack
        while (iterNode is not None) or (len(stack) > 0):
            while iterNode is not None:
                stack.append(iterNode)
                iterNode = iterNode.left

            iterNode = stack.pop()
            if badNode is not None:
                if (badNode.val < iterNode.val):
                    self.swapNodeValues(badNode, prevNode)
                    return
            elif prevNode.val > iterNode.val:
                badNode = prevNode
            prevNode = iterNode

            iterNode = iterNode.right

        # swap was not done means the found badNode is larger than all
        # nodes in the tree, must swap with last node in tree
        self.swapNodeValues(badNode, prevNode)
        return

    @staticmethod
    def swapNodeValues(node1: TreeNode, node2: TreeNode):
        node1.val, node2.val = node2.val, node1.val

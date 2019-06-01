"""

101. Symmetric Tree
Easy
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    @staticmethod
    def extractValue(root: TreeNode):
        if root is None:
            return None
        else:
            return root.val

    def isSymmetric(self, root: TreeNode) -> bool:

        if root is None:
            return True

        left_queue = [root.left]
        right_queue = [root.right]

        while (len(left_queue) > 0) and (len(right_queue) > 0):

            left_node = left_queue.pop(0)
            right_node = right_queue.pop(0)
            if self.extractValue(left_node) != self.extractValue(right_node):
                return False

            if left_node is not None:
                left_queue.extend([left_node.left, left_node.right])
            if right_node is not None:
                right_queue.extend([right_node.right, right_node.left])

        if (len(left_queue) > 0) or (len(right_queue) > 0):
            return False
        else:
            return True

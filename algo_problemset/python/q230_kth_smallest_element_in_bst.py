import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        nodePtr, nodeStack = root, deque()

        while (nodePtr is not None) or len(nodeStack) > 0:

            while nodePtr is not None:
                nodeStack.append(nodePtr)
                nodePtr = nodePtr.left

            nodePtr = nodeStack.pop()
            k -= 1
            if k == 0:
                return nodePtr.val
            nodePtr = nodePtr.right

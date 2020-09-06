"""
117. Populating Next Right Pointers in Each Node II
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.recursiveConnect(root)
        return root

    def recursiveConnect(self, node: 'Node') -> 'Node':
        if node is None: return

        if node.left is not None:
            if node.right is not None:
                node.left.next = node.right
            else:
                node.left.next = self.findNextFromParent(node)

        if node.right is not None:
            node.right.next = self.findNextFromParent(node)

        self.recursiveConnect(node.right)
        self.recursiveConnect(node.left)

    def findNextFromParent(self, node: 'Node') -> 'Node':
        nodePtr = node.next
        while nodePtr is not None:
            if nodePtr.left is not None: return nodePtr.left
            if nodePtr.right is not None: return nodePtr.right
            nodePtr = nodePtr.next

        return None

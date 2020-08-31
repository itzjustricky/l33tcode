# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: return
        self.recursiveConnect(root)
        return root

    def recursiveConnect(self, node: 'Node') -> 'Node':
        if node.left is None: return

        node.left.next = node.right
        if node.next is not None:
            node.right.next = node.next.left

        self.recursiveConnect(node.left)
        self.recursiveConnect(node.right)

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
        if root is None: return

        self.badNode, self.lastVisitedNode = None, None
        self.swapped = False

        self.inOrderTraversal(root)
        # the found bad node is larger than all nodes encountered
        # then swap it with last node in InOrder traversal
        if not self.swapped:
            swapNodeValues(self.badNode, self.lastVisitedNode)

    def inOrderTraversal(self, node: TreeNode) -> TreeNode:
        if self.swapped: return

        if node.left is None:
            self.visitAndUpdate(node)
        else:
            self.inOrderTraversal(node.left)
            self.visitAndUpdate(node)
        if node.right is not None:
            self.inOrderTraversal(node.right)

    def visitAndUpdate(self, currNode: TreeNode):
        """
        When entering this function, it should be thought of as
        the currNode being 'visited'.

        This function either:
        * updates the badNode or
        * does the swapping and flip the swapped flag
        """
        if self.swapped: return

        if self.lastVisitedNode is None:
            self.lastVisitedNode = currNode
            return

        if self.badNode is None:
            if self.lastVisitedNode.val > currNode.val:
                self.badNode = self.lastVisitedNode
        else:
            if self.badNode.val <= currNode.val:
                swapNodeValues(self.badNode, self.lastVisitedNode)
                self.swapped = True
        self.lastVisitedNode = currNode


def isLeaf(node: TreeNode) -> bool:
    return (node.left is None) and (node.right is None)


def swapNodeValues(node1: TreeNode, node2: TreeNode):
    node1.val, node2.val = node2.val, node1.val

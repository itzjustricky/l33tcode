from typing import Tuple


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor, _ = helper(root, p, q)
        return ancestor


def helper(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Tuple['TreeNode', int]:
    if root is None:
        return (None, 0)

    if (root == p) and (root == q):
        return (root, 2)

    leftCommon = helper(root.left, p, q)
    rightCommon = helper(root.right, p, q)

    holdCount = leftCommon[1] + rightCommon[1]

    # the root is one of the nodes: p, q
    # and left or right subtree holds the other node
    if (root == p) or (root == q):
        # increment the hold count since one of the nodes is the root
        holdCount += 1
        if holdCount == 2:
            return root, 2

    if holdCount == 2:
        if leftCommon[1] == 2:
            return leftCommon
        elif rightCommon[1] == 2:
            return rightCommon
        # left subtree holds one of the nodes and
        # right subtree holds the other one
        else:
            return (root, 2)
    # the root passed does not hold both of the nodes: p, q
    # more precisely holds either one or none of them
    else:
        return (None, holdCount)

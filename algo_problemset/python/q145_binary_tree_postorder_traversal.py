from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: return []

        nodePtr = root
        # nodeStack is a stack to store nodes
        # countStack is to keep track of a certain event:
        #       when a node has both left and right children
        #       as we need to visit the left subtree first, We
        #       will push a number into the countStack that tracks
        #       the count for how down we moved down from that split
        #   It will be used to identify as we pop nodes off the nodeStack
        #       how far up we can go back up the tree before looking at right
        #       child of a node.
        nodeStack, countStack = deque(), deque()

        traversalList = list()
        while (nodePtr is not None) or (len(nodeStack) > 0):
            # go as far down the tree as possible, with going down left being priority
            while nodePtr is not None:
                nodeStack.append(nodePtr)
                hasLeft, hasRight = nodePtr.left is not None, nodePtr.right is not None

                if hasLeft and hasRight:
                    nodePtr = nodePtr.left
                    countStack.append(1)
                elif hasLeft:
                    if len(countStack) > 0: countStack[-1] += 1
                    nodePtr = nodePtr.left
                elif hasRight:
                    if len(countStack) > 0: countStack[-1] += 1
                    nodePtr = nodePtr.right
                else:
                    nodePtr = None

            # take things out of the stack and put it into traversalList

            # there is right child up the tree that needs to be 'searched'
            if len(countStack) > 0:
                count = countStack.pop()
                for i in range(count):
                    traversalList.append(nodeStack.pop().val)

                nodePtr = nodeStack[-1].right
                if len(countStack) > 0: countStack[-1] += 1
                # else let nodePtr stay None and let nodeStack be emptied out
            # there's no more nodes needed to visit besides the
            # ones on the nodeStack
            else:
                while len(nodeStack) > 0:
                    traversalList.append(nodeStack.pop().val)

        return traversalList

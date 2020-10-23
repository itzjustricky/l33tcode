# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        n = self.getLinkedListSize(head)
        nodePtr = head

        def recursiveTransform(start: int, end: int) -> TreeNode:
            """ Return the root of the subtree coming from
                start to end of the ListNode
            """
            nonlocal nodePtr

            diff = end - start
            if diff == 0:
                return None
            if diff == 1:
                subRootNode = toTreeNode(nodePtr)
                nodePtr = nodePtr.next
                return subRootNode

            mid = (start + end) // 2
            leftChild = recursiveTransform(start, mid)
            rootNode = toTreeNode(nodePtr)
            rootNode.left = leftChild

            nodePtr = nodePtr.next
            rootNode.right = recursiveTransform(mid+1, end)

            return rootNode

        rootNode = recursiveTransform(0, n)
        return rootNode

    def getLinkedListSize(self, head: ListNode) -> int:
        cnt = 0
        while head is not None:
            head = head.next
            cnt += 1
        return cnt


def toTreeNode(node: ListNode) -> TreeNode:
    return TreeNode(node.val)

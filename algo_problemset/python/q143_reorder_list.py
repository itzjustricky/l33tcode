from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodePtr, nodeDeque = head, deque()

        # get all the nodes into a deque
        while nodePtr is not None:
            nodeDeque.append(nodePtr)
            nodePtr = nodePtr.next

        while len(nodeDeque) > 0:
            leftPtr = nodeDeque.popleft()
            rightPtr = nodeDeque.pop() if len(nodeDeque) > 0 else None

            leftPtr.next = rightPtr
            if rightPtr is not None:
                rightPtr.next = nodeDeque[0] if len(nodeDeque) > 0 else None

        return head

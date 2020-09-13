import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        if head is None: return None

        sortedHead, nodePtr = ListNode(-math.inf), head

        while nodePtr is not None:
            # severe connection to nodePtr
            tmpNode, nodePtr.next = nodePtr.next, None
            self.insertSorted(nodePtr, sortedHead)

            nodePtr = tmpNode
        return sortedHead.next

    @staticmethod
    def insertSorted(nodeToInsert: ListNode, head: ListNode):
        """
        Insertion sort, has an assumption that the head passed
        that head passed is a Dummy Head with value negative inf
        """
        nodeLeft, nodeRight = head, head.next
        while (nodeRight is not None) and (nodeToInsert.val >= nodeRight.val):
            nodeLeft, nodeRight = nodeLeft.next, nodeRight.next

        nodeLeft.next, nodeToInsert.next = nodeToInsert, nodeRight

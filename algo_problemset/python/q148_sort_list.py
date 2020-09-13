import math
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None: return None

        nodePtr = head
        nodeGroups = list()
        # gather all the nodes into a list and severe links
        while nodePtr is not None:
            nodeGroups.append(nodePtr)
            nodePtr.next, nodePtr = None, nodePtr.next

        while len(nodeGroups) > 1:
            n = len(nodeGroups) + 1
            nodeGroups = [
                self.mergeSort(nodeGroups[i], self.getGroup(j, nodeGroups))
                for i, j in zip(range(0, n, 2), range(1, n, 2))]

        return nodeGroups[0]

    def mergeSort(self, sortedHead1: ListNode, sortedHead2: ListNode) -> ListNode:
        if sortedHead2 is None: return sortedHead1

        dummyNode = ListNode(-math.inf, sortedHead1)

        insertFromNode, nodePtr = dummyNode, sortedHead2
        while nodePtr is not None:
            tmpNode = nodePtr.next
            self.insertSorted(nodePtr, insertFromNode)
            insertFromNode, nodePtr = nodePtr, tmpNode

        return dummyNode.next

    @staticmethod
    def insertSorted(nodeToInsert: ListNode, sortedHead: ListNode) -> None:
        """
        Insertion sort, has an assumption that the head passed
        that head passed is a Dummy Head with value negative inf
        """
        nodeLeft, nodeRight = sortedHead, sortedHead.next
        while (nodeRight is not None) and (nodeToInsert.val >= nodeRight.val):
            nodeLeft, nodeRight = nodeLeft.next, nodeRight.next
        nodeLeft.next, nodeToInsert.next = nodeToInsert, nodeRight

    @staticmethod
    def getGroup(ind: int, groupList: List[ListNode]):
        return None if ind >= len(groupList) else groupList[ind]

"""

61. Rotate List
Medium
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    @staticmethod
    def findLengthOfList(head: ListNode) -> int:
        list_length, node_ptr = 0, head
        while node_ptr is not None:
            list_length += 1
            node_ptr = node_ptr.next
        return list_length

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        n = self.findLengthOfList(head)
        if (n == 0) or (k == 0):
            return head

        k = k % n
        if k == 0:
            return head

        p1, p2 = head, head
        # move 2nd pointer k ahead
        for i in range(k):
            p2 = p2.next
        for i in range(n-k-1):
            p1, p2 = p1.next, p2.next

        p2.next = head
        new_head, p1.next = p1.next, None
        return new_head

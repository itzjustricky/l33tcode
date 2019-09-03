"""

92. Reverse Linked List II
Medium
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverseNNodes(self, n: int, head: ListNode):
        if n == 0: return

        # from where to start reversing
        start_node = head.next

        # assume list is large enough for reversal
        left, mid, right = start_node, start_node.next, start_node.next.next

        for i in range(n):
            mid.next = left
            left, mid = mid, right
            if right is not None: right = right.next

        head.next = left
        start_node.next = mid

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head

        node_ptr = dummy_head
        # iterate m-1 nodes forward
        for i in range(m-1):
            node_ptr = node_ptr.next

        self.reverseNNodes(n-m, node_ptr)
        return dummy_head.next

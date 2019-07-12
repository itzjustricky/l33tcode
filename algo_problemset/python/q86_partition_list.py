"""

86. Partition List
Medium
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def partition(self, head: ListNode, x: int) -> ListNode:
        # the left & right partitions
        left_head, right_head = None, None
        left_ptr, right_ptr = None, None

        node_ptr = head
        while (node_ptr is not None):
            if node_ptr.val < x:
                if left_ptr is not None:
                    left_ptr.next = node_ptr
                    left_ptr = left_ptr.next
                else:
                    left_ptr = left_head = node_ptr
            else:
                if right_ptr is not None:
                    right_ptr.next = node_ptr
                    right_ptr = right_ptr.next
                else:
                    right_ptr = right_head = node_ptr

            node_ptr = node_ptr.next

        # there are no values less than the passed x
        if left_ptr is None:
            left_head = right_head
        else:
            left_ptr.next = right_head

        if right_ptr is not None:
            right_ptr.next = None

        return left_head

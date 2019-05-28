"""

25. Reverse Nodes in k-Group
Hard
"""

from typing import Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    @staticmethod
    def reverseList(head: ListNode) -> Tuple[ListNode, ListNode]:
        """ Reverse the list starting at the passed node.
            Will return the head and tail of the Reversed List.
        """
        p1, p2, p3 = head, head.next, head.next.next

        while p3 is not None:
            p2.next = p1
            p1, p2, p3 = p2, p3, p3.next

        p2.next = p1
        return p2, head

    @staticmethod
    def disconnectAtK(node: ListNode, k: int) -> ListNode:
        """ Will iterate k-1 times to the right and disconnect from the next node.
            Will return the next node.

        :param node: the node pointing to the start of list
        """
        node_ptr = node
        for i in range(k-1):
            node_ptr = node_ptr.next

        next_head = node_ptr.next
        node_ptr.next = None
        return next_head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        if k == 1:
            return head

        try:
            next_head = self.disconnectAtK(head, k)
        except AttributeError:
            # the list is smaller than size k, nothing to reverse
            return head

        new_head, _tail = self.reverseList(head)
        _tail.next = next_head

        prev_tail = _tail
        while True:
            try:
                next_head = self.disconnectAtK(next_head, k)
                # retrieve the new head and tail of the just Reversed Group
                _head, _tail = self.reverseList(prev_tail.next)
                # set the previous tail to the head of the Reversed Group
                prev_tail.next = _head
                # move prev_tail to point to node right before group to reverse
                # & set the tail of the just Reversed Group to the head of the next Group
                prev_tail, _tail.next = _tail, next_head
            except AttributeError:
                break

        return new_head

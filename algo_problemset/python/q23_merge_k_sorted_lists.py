"""
23. Merge k Sorted Lists
"""

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def _merge(self, head1: ListNode, head2: ListNode) -> ListNode:
        dummy_head = ListNode(None)
        merged_list = dummy_head

        node1, node2 = head1, head2

        while (node1 is not None) and (node2 is not None):
            if node1.val <= node2.val:
                merged_list.next = node1
                node1 = node1.next
            else:
                merged_list.next = node2
                node2 = node2.next
            merged_list = merged_list.next

        # at least one of the nodes should point to None here
        if node1 is not None:
            merged_list.next = node1
        elif node2 is not None:
            merged_list.next = node2
        return dummy_head.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        merged_list = lists[0]
        for head in lists[1:]:
            merged_list = self._merge(merged_list, head)

        return merged_list

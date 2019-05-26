"""
23. Merge k Sorted Lists
"""

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# this is a stupid solution, but it takes advantage of the fact
# that the python sorted function has some optimizations
class Solution:

    def _extract_values(self, head: ListNode):
        node = head
        while node is not None:
            yield node.val
            node = node.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        vals = [x for node in lists for x in self._extract_values(node)]
        vals = sorted(vals)

        merged_head = ListNode(0)
        merged_list = merged_head

        for x in vals:
            merged_list.next = ListNode(x)
            merged_list = merged_list.next

        return merged_head.next

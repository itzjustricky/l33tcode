"""

83. Remove Duplicates from Sorted List
Easy
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None: return head

        prev_node, curr_node = head, None
        while prev_node.next is not None:
            curr_node = prev_node.next
            if curr_node.val == prev_node.val:
                prev_node.next = curr_node.next
            else:
                prev_node = prev_node.next

        return head

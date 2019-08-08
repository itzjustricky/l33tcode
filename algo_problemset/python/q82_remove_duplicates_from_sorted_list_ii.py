"""

82. Remove Duplicates from Sorted List II
Medium
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head

        p1, p2, p3 = dummy_head, head, None

        while p2 is not None:

            p3 = p2.next
            if p3 is None: break

            # if duplicate is found then remove all
            # nodes with this value from the list
            if p2.val == p3.val:
                val_to_delete = p2.val

                node = p1
                while (node.next is not None) and (node.next.val == val_to_delete):
                    node.next = node.next.next

                p2 = p1.next
            else:
                p1, p2 = p2, p3

        return dummy_head.next

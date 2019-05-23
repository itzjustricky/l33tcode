"""

    19. Remove Nth Node From End of List
    Medium

    Example:
    Given linked list: 1->2->3->4->5, and n=2.
    After removing the second node from the end, the linked list becomes 1->2->3->5.

    Note:
    Given n will always be valid.
    Follow up:
    Could you do this in one pass?

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def move_forward(self, node: ListNode, n_times: int) -> ListNode:
        for i in range(n_times):
            node = node.next
        return node

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        ptr1, ptr2 = head, head
        ptr2 = self.move_forward(ptr2, n)

        if ptr2 is None:
            return head.next

        while ptr2.next is not None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        ptr1.next = ptr1.next.next
        return head


def print_node(head: ListNode):
    def iter_linked_list(head: ListNode):
        node = head
        while node is not None:
            yield node.val
            node = node.next
    print(' -> '.join(map(str, iter_linked_list(head))))


if __name__ == "__main__":

    # create
    # 1->2->3->4->5
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    # end

    sol = Solution()
    new_head = sol.removeNthFromEnd(node1, 5)
    print_node(new_head)

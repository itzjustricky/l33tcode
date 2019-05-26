"""

    24. Swap Nodes in Pairs

    Given a linked list, swap every two adjacent nodes and return its head.
    You may not modify the values in the list's nodes, only nodes itself may be changed.

    Example:
    Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def _swap(self, node: ListNode) -> ListNode:

        # if node1 or node2 are None, there is no swapping to do
        node1 = node.next
        if node1 is None: return None

        node2 = node1.next
        if node2 is None: return None
        node3 = node2.next

        node.next = node2
        node1.next, node2.next = node3, node1
        return node1

    def swapPairs(self, head: ListNode) -> ListNode:

        dummy_head = ListNode(0)
        dummy_head.next = head

        node_ptr = dummy_head
        while node_ptr is not None:
            node_ptr = self._swap(node_ptr)

        return dummy_head.next


def print_list(head: ListNode):

    def _iter_list(head: ListNode):
        node_ptr = head
        while node_ptr is not None:
            yield node_ptr.val
            node_ptr = node_ptr.next

    print(' -> '.join((map(str, _iter_list(head)))))


if __name__ == "__main__":
    node = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)

    node.next = node1; node1.next = node2
    node2.next = node3; node3.next = node4

    print_list(node)

    sol = Solution()
    new_head = sol.swapPairs(node)
    print_list(new_head)

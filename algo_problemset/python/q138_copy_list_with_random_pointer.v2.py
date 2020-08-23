# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        newDummyHead = Node(0)
        oldToNewMap = dict()

        nodePtr, newNodePtr = head, newDummyHead
        while nodePtr is not None:
            newNodePtr.next = Node(nodePtr.val, random=nodePtr.random)
            oldToNewMap[id(nodePtr)] = newNodePtr.next

            nodePtr, newNodePtr = nodePtr.next, newNodePtr.next

        newNodePtr = newDummyHead.next
        while newNodePtr is not None:
            if newNodePtr.random is not None:
                newNodePtr.random = oldToNewMap[id(newNodePtr.random)]
            newNodePtr = newNodePtr.next

        return newDummyHead.next

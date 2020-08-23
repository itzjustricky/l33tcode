# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        newDummyHead = Node(0)
        oldRefToIndexMap, newNodes = dict(), list()

        ind, nodePtr, newNodePtr = 0, head, newDummyHead
        while nodePtr is not None:
            oldRefToIndexMap[id(nodePtr)] = ind
            newNodePtr.next = Node(nodePtr.val, random=nodePtr.random)
            newNodes.append(newNodePtr.next)

            ind, nodePtr, newNodePtr = ind+1, nodePtr.next, newNodePtr.next

        newNodePtr = newDummyHead.next
        while newNodePtr is not None:
            if newNodePtr.random is not None:
                newNodePtr.random = newNodes[oldRefToIndexMap[id(newNodePtr.random)]]
            newNodePtr = newNodePtr.next

        return newDummyHead.next

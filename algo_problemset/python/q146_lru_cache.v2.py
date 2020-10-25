

class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None


def popNode(node: ListNode):
    prevNode, nextNode = node.prev, node.next
    prevNode.next, nextNode.prev = nextNode, prevNode
    node.next, node.prev = None, None
    return node


def insertNodeRightBefore(insertNode: ListNode, newNode: ListNode):
    prevNode = insertNode.prev

    prevNode.next, newNode.prev = newNode, prevNode
    newNode.next, insertNode.prev = insertNode, newNode


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # dictionary mapping key -> ListNode
        self.keyDict = dict()

        # headNode will not actually be the first item, it will point to the first item
        self.headNode = ListNode(None, None)
        # similarly for tailNode
        self.tailNode = ListNode(None, None)
        self.headNode.next, self.tailNode.prev = self.tailNode, self.headNode

    def get(self, key: int) -> int:
        if key in self.keyDict:
            node = self.keyDict[key]
            popNode(node)

            insertNodeRightBefore(self.tailNode, node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyDict:
            popNode(self.keyDict[key])
            self.keyDict.pop(key)

        # cache is about to be full
        if len(self.keyDict) >= self.capacity:
            lruNode = self.headNode.next
            self.keyDict.pop(lruNode.key)
            popNode(lruNode)

        node = ListNode(key, value)
        self.keyDict[key] = node
        insertNodeRightBefore(self.tailNode, node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

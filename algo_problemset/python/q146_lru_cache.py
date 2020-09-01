"""
Question 146: Lru Cache
"""


class ListNode(object):

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class LRUCache:

    def __init__(self, capacity: int):
        # mapping from key -> (ListNode, value)
        self.cache = dict()
        # the Most Recently Used will be on most left
        # the Least Recently Used will be on most right
        # head and tail will be dummy nodes on most left and most right side of list
        self.head, self.tail = ListNode(None), ListNode(None)
        self.head.right, self.tail.left = self.tail, self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            keyNode, value = self.cache.pop(key)
            self.removeNodeFromList(keyNode)

            newNode = ListNode(key)
            self.insertNodeAfter(self.head, newNode)
            self.cache[key] = newNode, value
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            keyNode = self.cache[key][0]
            keyNode, oldValue = self.cache.pop(key)
            self.removeNodeFromList(keyNode)

            newNode = ListNode(key)
            self.insertNodeAfter(self.head, newNode)
            self.cache[key] = newNode, value

        # new key and reached capacity
        elif len(self.cache) == self.capacity:
            self.removeLru()
            newNode = ListNode(key)
            self.insertNodeAfter(self.head, newNode)
            self.cache[key] = (newNode, value)
        else:
            newNode = ListNode(key)
            self.insertNodeAfter(self.head, newNode)
            self.cache[key] = (newNode, value)

    def removeLru(self):
        lruNode = self.tail.left
        self.removeNodeFromList(lruNode)
        self.cache.pop(lruNode.key)

    def insertNodeAfter(self, atNode: ListNode, newNode: ListNode):
        rightNode = atNode.right
        atNode.right, newNode.left = newNode, atNode
        newNode.right, rightNode.left = rightNode, newNode

    def insertNodeBefore(self, atNode, newNode: ListNode):
        leftNode = atNode.left
        atNode.left, newNode.right = newNode, atNode
        newNode.left, leftNode.right = leftNode, newNode

    def removeNodeFromList(self, node: ListNode):
        """ This should never be called on dummy nodes (most left/right nodes) """
        node.left.right, node.right.left = node.right, node.left
        del node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

obj = LRUCache(1)
obj.put(2, 1)
print(obj.get(2))
obj.put(3, 2)
print(obj.get(2))
print(obj.get(3))
# obj.put(key,value)
# obj.put(key,value)

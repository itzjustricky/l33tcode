class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        nodePtr = self.head
        for char in word:
            if char not in nodePtr.charDict:
                nodePtr.charDict[char] = TrieNode()
            nodePtr = nodePtr.charDict[char]
        nodePtr.count += 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        nodePtr = self.head
        for char in word:
            if char in nodePtr.charDict:
                nodePtr = nodePtr.charDict[char]
            else:
                return False
        return nodePtr.count > 0

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        nodePtr = self.head
        for char in prefix:
            if char in nodePtr.charDict:
                nodePtr = nodePtr.charDict[char]
            else:
                return False
        return True


class TrieNode:
    __slots__ = ["charDict", "count"]

    def __init__(self):
        self.charDict = dict()
        self.count = 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

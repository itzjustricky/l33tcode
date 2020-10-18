# make use of a trie with special search
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        nodePtr = self.head
        for char in word:
            if char not in nodePtr.charDict:
                nodePtr.charDict[char] = TrieNode()
            nodePtr = nodePtr.charDict[char]

        nodePtr.count += 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        """
        return self.head.searchWord(word)


class TrieNode:

    __slots__ = ["count", "charDict"]

    def __init__(self):
        self.count = 0
        self.charDict = dict()

    def searchWord(self, word: str) -> bool:
        if len(word) == 0:
            return self.count > 0
        firstChar = word[0]

        if firstChar == '.':
            return any(
                node.searchWord(word[1:])
                for node in self.charDict.values())

        if firstChar in self.charDict:
            return self.charDict[firstChar].searchWord(word[1:])
        else:
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

import math
from typing import List


class StorageNode(object):
    __slots__ = ['val']

    def __init__(self, val):
        self.val = val


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        self.hashDict = dict()
        longestConsecCnt = -math.inf

        for num in nums:
            if num in self.hashDict: continue

            leftNeighbor, rightNeighbor = self.hashDict.get(num-1), self.hashDict.get(num+1)

            currNode = None
            consecutiveCnt = 1

            if (leftNeighbor is not None) and (rightNeighbor is not None):
                leftParent, rightParent = self.getParent(leftNeighbor), self.getParent(rightNeighbor)
                consecutiveCnt += leftParent.val + rightParent.val

                currNode = StorageNode(consecutiveCnt)
                leftParent.val, rightParent.val = currNode, currNode

            elif leftNeighbor is not None:
                leftParent = self.getParent(leftNeighbor)
                consecutiveCnt += leftParent.val
                currNode = StorageNode(consecutiveCnt)
                leftParent.val = currNode
            elif rightNeighbor is not None:
                rightParent = self.getParent(rightNeighbor)
                consecutiveCnt += rightParent.val
                currNode = StorageNode(consecutiveCnt)
                rightParent.val = currNode
            else:
                currNode = StorageNode(consecutiveCnt)

            longestConsecCnt = max(longestConsecCnt, consecutiveCnt)
            self.hashDict[num] = currNode

        return longestConsecCnt

    def getParent(self, storageNode):
        """ Get parent of the node then compress all nodes """

        nodePtr = storageNode

        nodesAlongPath = list()
        while isinstance(nodePtr.val, StorageNode):
            nodesAlongPath.append(nodePtr)
            nodePtr = nodePtr.val

        # compress the paths
        for node in nodesAlongPath: node.val = nodePtr

        return nodePtr

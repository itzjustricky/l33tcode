import math

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # if k is 1 then there will not be any values right of pivot
        # handle this by just getting the max
        if k == 1:
            return max(nums)

        n = len(nums)
        # first put pivot at back and gradually move it to the n-k th index
        # have all elements to the right of it larger than it
        pivotIndex = n-1
        while pivotIndex > n-k:
            if nums[pivotIndex-1] > nums[pivotIndex]:
                swap(pivotIndex-1, pivotIndex, nums)
            pivotIndex -= 1

        # now store all values right of pivot in a minheap
        minHeap = MinHeap()
        for ind, num in enumerate(nums[pivotIndex+1:], pivotIndex+1):
            minHeap.insert(MinHeapNode(num, ind))

        frontCount = 0
        compIndex = pivotIndex - 1
        while frontCount <= compIndex:

            if nums[compIndex] > nums[pivotIndex]:
                # the number at the pivotIndex cannot be the kth largest
                # swap it to the front of the list
                swap(compIndex, pivotIndex, nums)
                swap(frontCount, compIndex, nums)
                frontCount += 1

                # if there is any number smaller than the current pivot
                # to the right of it then swap them
                while minHeap.top().val < nums[pivotIndex]:
                    minNode = minHeap.pop()
                    swap(minNode.index, pivotIndex, nums)
                    minHeap.insert(MinHeapNode(nums[minNode.index], minNode.index))
            else:
                compIndex -= 1

        return nums[pivotIndex]


def findSmallerNumber(target: int, startFrom: int, nums: List[int]):
    for ind, num in enumerate(nums[startFrom:], startFrom):
        if num < target:
            return ind
    return None


class MinHeapNode:
    __slots__ = ["val", "index"]

    def __init__(self, val: int, index: int):
        self.val = val
        self.index = index


class MinHeap:

    def __init__(self):
        self.heapArr = list()

    def insert(self, node: MinHeapNode):
        self.heapArr.append(node)
        self.enforceMinConditionOnInsert()

    def getParent(self, ind: int) -> int:
        level = self.getLevel(ind)
        section = ind - ((2 ** level) - 1)
        return (2 ** level) - 2 - (2**(level-1) - section//2 - 1)

    def getChildrenIndices(self, ind: int) -> int:
        """ Returns the indices of the left and child nodes respectively """
        level = self.getLevel(ind)
        section = ind - ((2 ** level) - 1)

        childIndexStart = ((2 ** (level+1)) - 1)
        return childIndexStart + (section * 2), childIndexStart + (section * 2) + 1

    def getLevel(self, ind: int) -> int:
        return math.floor(math.log2(ind + 1))

    def enforceMinConditionOnInsert(self):
        n = len(self.heapArr)
        nodeIndex = n - 1

        while nodeIndex > 0:
            parentIndex = self.getParent(nodeIndex)

            if self.heapArr[parentIndex].val > self.heapArr[nodeIndex].val:
                swap(parentIndex, nodeIndex, self.heapArr)
                nodeIndex = parentIndex
            else:
                break

    def enforceMinConditionOnPop(self):
        n = len(self.heapArr)

        nodeIndex = 0
        leftChild, rightChild = self.getChildrenIndices(nodeIndex)

        while nodeIndex < n:
            leftChild, rightChild = self.getChildrenIndices(nodeIndex)
            leftChildVal = self.heapArr[leftChild].val if (leftChild < n) else math.inf
            rightChildVal = self.heapArr[rightChild].val if (rightChild < n) else math.inf

            if leftChildVal < rightChildVal:
                minIndex, minValue = leftChild, leftChildVal
            else:
                minIndex, minValue = rightChild, rightChildVal

            if self.heapArr[nodeIndex].val > minValue:
                swap(nodeIndex, minIndex, self.heapArr)
                nodeIndex = minIndex
            else:
                break

    def pop(self):
        n = len(self.heapArr)
        swap(0, n-1, self.heapArr)
        heapNode = self.heapArr.pop()
        self.enforceMinConditionOnPop()
        return heapNode

    def top(self):
        return self.heapArr[0]


def swap(i: int, j: int, nums: List[int]):
    nums[i], nums[j] = nums[j], nums[i]


if __name__ == "__main__":
    print(
        Solution().findKthLargest([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 20)   # noqa
    )

from typing import List
from typing import Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.recursiveSortedArrayToBST(nums, (0, len(nums)))

    def recursiveSortedArrayToBST(self, nums: List[int], indexRange: Tuple[int, int]) -> TreeNode:
        start, end = indexRange
        center, length = (end+start) // 2, end - start
        if length == 0: return None
        if length == 1: return TreeNode(nums[center])

        rootNode = TreeNode(nums[center])
        rootNode.left = self.recursiveSortedArrayToBST(nums, (start, center))
        rootNode.right = self.recursiveSortedArrayToBST(nums, (center+1, end))

        return rootNode

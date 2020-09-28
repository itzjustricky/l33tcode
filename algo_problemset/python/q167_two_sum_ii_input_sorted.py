from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPtr, rightPtr = 0, len(numbers) - 1

        while leftPtr < rightPtr:
            trackedSum = numbers[leftPtr] + numbers[rightPtr]
            if trackedSum < target:
                leftPtr += 1
            elif trackedSum > target:
                rightPtr -= 1
            else:
                return [leftPtr+1, rightPtr+1]

        # failed to find sum to equal target
        return []

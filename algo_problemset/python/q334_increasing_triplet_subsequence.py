"""

    334. Increasing Triplet Subsequence
    Medium

    Given an unsorted array return whether an increasing subsequence of
    length 3 exists or not in the array.

    Formally the function should:
    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
    Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

    Example 1:
    Input: [1,2,3,4,5]
    Output: true

    Example 2:
    Input: [5,4,3,2,1]
    Output: false
"""

from typing import List


class Solution:

    def increasingTriplet(self, nums: List[int]) -> bool:

        mainStack, candStack = list(), list()
        if len(nums) < 3: return False

        mainStack.append(nums[0])

        for num in nums[1:]:

            if len(mainStack) == 1:
                if num < mainStack[0]:
                    mainStack[0] = num
                elif num > mainStack[0]:
                    mainStack.append(num)

            elif len(mainStack) == 2:

                if num < mainStack[-1]:
                    # if number is smaller than both elements in stack
                    # consider a candidate stack
                    if num < mainStack[0]:
                        # create a candidate stack or use it
                        if len(candStack) == 0:
                            candStack.append(num)

                        elif len(candStack) == 1:
                            # number is smaller than the number in the candidate stack
                            # candidate stack should be the new stack
                            if num > candStack[0]:
                                candStack.append(num)
                                mainStack = candStack
                                candStack = list()

                            # if new number is smaller than candidate stack number
                            # just replace the number in the candidate stack
                            elif num < candStack[0]:
                                candStack[0] = num

                        else:
                            raise RuntimeError("Candidate stack is in an invalid state.")

                    # smaller than top number but larger than second number
                    # replace the second number
                    elif num > mainStack[0]:
                        mainStack[-1] = num

                # we reached three numbers
                elif num > mainStack[-1]:
                    return True

            else:
                raise RuntimeError(
                    "Main stack reached invalid state of size {}.".format(len(mainStack)))

        return False

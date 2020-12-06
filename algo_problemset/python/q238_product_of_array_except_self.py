from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        productsList = [None] * n

        # productExceptSelf for index k is the product of
        # P_0,k * P_k+1,n
        # where P_i,j is the product of the numbers from
        # index i to j (inclusive on i, exclusive on j)

        prod = 1
        # prod going forward
        for i in range(n):
            productsList[i] = prod
            prod *= nums[i]

        prod = 1
        # prod going backwards
        for i in reversed(range(n)):
            productsList[i] *= prod
            prod *= nums[i]

        return productsList

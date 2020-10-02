class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0: return 0
        if m == n: return m

        rangeAnd = 0
        # this problem is equivalent of finding
        # the smallest largest matching bit between m and n
        for ind in reversed(range(32)):
            bitM, bitN = getNthBit(ind, m), getNthBit(ind, n)
            if bitM != bitN: break
            rangeAnd |= (bitM << ind)

        return rangeAnd


def getNthBit(n: int, num: int) -> int:
    """ 0-indexed retrieval of bits for int num """
    return (num >> n) & 1

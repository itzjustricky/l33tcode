class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapDict, reverseMapDict = dict(), dict()
        for c1, c2 in zip(s, t):
            if (c1 in mapDict) and (mapDict[c1] != c2):
                return False
            if (c2 in reverseMapDict) and (reverseMapDict[c2] != c1):
                return False

            mapDict[c1] = c2
            reverseMapDict[c2] = c1
        return True


if __name__ == "__main__":
    print(
        Solution().isIsomorphic("ab", "aa")
    )

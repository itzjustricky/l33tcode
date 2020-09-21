"""
Question 165: Compare Version Numbers
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1Ptr, version2Ptr = 0, 0
        n1, n2 = len(version1), len(version2)

        while (version1Ptr < n1) and (version2Ptr < n2):

            # keep moving pointer to remove all leading zeros
            while self.leadingZeroCondition(version1Ptr, version1):
                version1Ptr += 1
            while self.leadingZeroCondition(version2Ptr, version2):
                version2Ptr += 1

            version1Start, version2Start = version1Ptr, version2Ptr
            while (version1Ptr < n1) and (version1[version1Ptr] != '.'):
                version1Ptr += 1
            while (version2Ptr < n2) and (version2[version2Ptr] != '.'):
                version2Ptr += 1

            revision1Len = version1Ptr - version1Start
            revision2Len = version2Ptr - version2Start
            if revision1Len < revision2Len:
                return -1
            if revision1Len > revision2Len:
                return 1

            ptr1, ptr2 = version1Ptr-1, version2Ptr-1
            while (ptr2 >= version2Start) and (ptr1 >= version1Start):

                if version1[ptr1] < version2[ptr2]:
                    return -1
                elif version1[ptr1] > version2[ptr2]:
                    return 1
                ptr1 -= 1; ptr2 -= 1

            # here the pters are either on a dot or
            # on index n (where n is the size of the version)
            version1Ptr += 1; version2Ptr += 1

        # there are still revisions left on version1, if there is any
        # non-zero revision then version1 is greater than version2
        while version1Ptr < n1:
            while self.leadingZeroCondition(version1Ptr, version1):
                version1Ptr += 1
            version1Start = version1Ptr
            while (version1Ptr < n1) and (version1[version1Ptr] != '.'):
                version1Ptr += 1

            ptr = version1Ptr-1
            while ptr >= version1Start:
                if version1[ptr] > '0':
                    return 1
                ptr -= 1
            version1Ptr += 1

        # there are still revisions left on version2, if there is any
        # non-zero revision then version2 is greater than version1
        while version2Ptr < n2:
            while self.leadingZeroCondition(version2Ptr, version2):
                version2Ptr += 1
            version2Start = version2Ptr
            while (version2Ptr < n2) and (version2[version2Ptr] != '.'):
                version2Ptr += 1

            ptr = version2Ptr-1
            while ptr >= version2Start:
                if version2[ptr] > '0':
                    return -1
                ptr -= 1
            version2Ptr += 1

        return 0

    def leadingZeroCondition(self, indexPtr: int, versionStr: str) -> bool:
        """
        Represent the condition for which to continue moving index pointer for
        removing leading zeros.
        For revision 000, only the first 2 0s are considered 'leading'.
        """
        return (
            ((indexPtr+1) < len(versionStr)) and
            (versionStr[(indexPtr+1)] != '.') and
            (versionStr[indexPtr] == '0'))


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.compareVersion("1.0", "1.0.2")
    )

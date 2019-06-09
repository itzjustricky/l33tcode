"""

72. Edit Distance
Hard
"""

from typing import List


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:

        n, m = len(word1), len(word2)

        def gen_min_distance(j: int, prev_min_dist: List[int]):
            """ Generate the min distance for the next row of values
                for the DP matrix.

            :param j: the index to represent sub-word of word2, word2[1...j]
            :param prev_min_dist: list of values for the previous row
            """
            prev_x = j
            yield prev_x

            for i in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    x = prev_min_dist[i-1]
                else:
                    x = 1 + min(
                        prev_min_dist[i-1],
                        prev_min_dist[i],
                        prev_x)
                prev_x = x
                yield x

        # the num. of edits needed to transform word[0 .. i] to an empty string
        # which would require deleting the whole string
        prev_min_dist = [i for i in range(n+1)]
        if m == 0: return prev_min_dist[n]

        for j in range(1, m+1):
            min_distance = [
                x for x in gen_min_distance(j, prev_min_dist)]
            prev_min_dist = min_distance

        return min_distance[n]


if __name__ == "__main__":
    sol = Solution()

    sol.minDistance("", "a")

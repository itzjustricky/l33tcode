"""

72. Edit Distance
Hard
"""

import itertools


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:

        n, m = len(word1), len(word2)
        min_distance = [
            [0 for j in range(m+1)]
            for i in range(n+1)]
        for i in range(n+1): min_distance[i][0] = i
        for j in range(m+1): min_distance[0][j] = j

        for i, j in itertools.product(range(1, n+1), range(1, m+1)):
            if word1[i-1] == word2[j-1]:
                min_distance[i][j] = min_distance[i-1][j-1]

            else:
                min_distance[i][j] = 1 + min(
                    min_distance[i-1][j-1],
                    min_distance[i][j-1],
                    min_distance[i-1][j])

        return min_distance[n][m]


if __name__ == "__main__":
    sol = Solution()

    sol.minDistance("", "a")

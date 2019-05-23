"""
    1039. Minimum Score Triangulation of Polygon
    Medium


    Given N, consider a convex N-sided polygon with vertices labelled
    A[0], A[i], ..., A[N-1] in clockwise order.

    Suppose you triangulate the polygon into N-2 triangles.  For each triangle,
    the value of that triangle is the product of the labels of the vertices,
    and the total score of the triangulation is the sum of these values over
    all N-2 triangles in the triangulation.

    Return the smallest possible total score that you can achieve with some
    triangulation of the polygon.

    Example 1:
    Input: [1,2,3]
    Output: 6
    Explanation: The polygon is already triangulated, and
        the score of the only triangle is 6.

    Example 2:
    Input: [3,7,4,5]
    Output: 144
    Explanation: There are two triangulations, with possible scores:
        3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.  The minimum score is 144.

    Example 3:
    Input: [1,3,1,4,1,5]
    Output: 13
    Explanation: The minimum score triangulation has score
        1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.

    Note:

    3 <= A.length <= 50
    1 <= A[i] <= 100
"""

import math

from typing import List


class Solution:

    def triangle_cost(self, A: List[int], i: int, j: int, k: int):
        return A[i] * A[j] * A[k]

    def rec_triangulation(self, A: List[int], start: int, end: int):

        if (start, end) in self.min_score_hash:
            return self.min_score_hash[(start, end)]

        if (end - start) == 2:
            self.min_score_hash[(start, end)] = \
                self.triangle_cost(A, start, start+1, end)
            return self.min_score_hash[(start, end)]
        elif (end - start) < 2:
            self.min_score_hash[(start, end)] = 0
            return 0

        min_cost = math.inf
        for k in range(start+1, end):
            min_cost = min(
                min_cost,
                self.rec_triangulation(A, start, k) +
                self.rec_triangulation(A, k, end) +
                self.triangle_cost(A, start, end, k))

        self.min_score_hash[(start, end)] = min_cost
        return min_cost

    def minScoreTriangulation(self, A: List[int]) -> int:
        self.min_score_hash = dict()
        return self.rec_triangulation(A, 0, len(A)-1)

if __name__ == "__main__":

    sol = Solution()
    min_score = sol.minScoreTriangulation([1,3,1,4,1,5])    # noqa [E231]
    print(min_score)

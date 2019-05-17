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
import operator
import functools

from typing import List
# from typing import Tuple


def wrap_iter(A: List[int], start: int, end: int) -> List[int]:
    if start > end:
        return A[start:] + A[:(end+1)]
    else:
        return A[start:(end+1)]


def calc_range_length(A: List[int], start: int, end: int) -> int:
    a_length = len(A)
    if start > end:
        return (a_length-start) + end + 1
    else:
        return end - start + 1


def iter_triangles(start: int, end: int):

    def wrap_range(wrap_start: int, wrap_end: int):
        for x in range(wrap_start, end+1):
            yield x
        for x in range(start, wrap_end+1):
            yield x

    range_list = list(range(start, end+1))
    for (i, j) in zip(range_list[:-1], range_list[1:]):
        for k in wrap_range(j+1, i-2):
            yield (i, j, k)


class Solution:

    def recursive_triangulation(self, A: List[int], start: int, end: int):

        if (start, end) in self.min_score_hash:
            return self.min_score_hash[(start, end)]

        # a_range = len(A)
        range_length = calc_range_length(A, start, end)

        if range_length < 3:
            return math.inf
        elif range_length == 3:
            self.min_score_hash[(start, end)] = functools.reduce(
                operator.mul, wrap_iter(A, start, end), 1)
        else:
            pass

    def minScoreTriangulation(self, A: List[int]) -> int:

        self.min_score_hash = dict()
        pass

"""
There is an assumption made that all the matrices are square matrices
"""


from typing import List
from collections import deque


class Solution:

    # solve this problem with Kahn's algorithm
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        # first construct a matrix representation of the implicit graph
        graphMatrix = [[False for j in range(n)] for i in range(n)]
        for afterCourse, beforeCourse in prerequisites:
            # transpose it for small optimization
            graphMatrix[afterCourse][beforeCourse] = True

        orderedCourses = list()
        # get the current courses with no prereqs
        noPreReqCourses = deque(
            ind for ind in range(n)
            if rowSum(ind, graphMatrix) == 0)

        while len(noPreReqCourses) > 0:
            courseId = noPreReqCourses.pop()
            orderedCourses.append(courseId)

            # remove all the outgoing edges from course
            for i in range(n):
                if graphMatrix[i][courseId] is False:
                    continue

                graphMatrix[i][courseId] = False
                # add to courses with no prereq if becomes such
                if rowSum(i, graphMatrix) == 0:
                    noPreReqCourses.append(i)

        # if there are still edges then there is a cycle
        if hasEdges(graphMatrix):
            return []

        return orderedCourses


def rowSum(rowInd: int, matrix: List[List[int]]) -> int:
    n = len(matrix)
    return sum(matrix[rowInd][i] for i in range(n))


def hasEdges(graphMatrix: List[List[int]]) -> bool:
    n = len(graphMatrix)
    return sum(rowSum(i, graphMatrix) for i in range(n)) > 0


if __name__ == "__main__":
    print(
        Solution().findOrder(5, [[1, 0]])
    )

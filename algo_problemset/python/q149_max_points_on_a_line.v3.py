from typing import List
from typing import Tuple
from typing import Union

import math
from fractions import Fraction
from collections import namedtuple

Line = namedtuple("Line", ["intercept", "slope"])

RationalNum = Union[int, Fraction]


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0: return 0

        # there is at least one point then there exists a line with a point
        maxPointsTracker = 1
        # Lines are represented by an intercept & slope. See how intercept
        #       is calculated in the calculateIntercept(...) function

        # Preprocess the count of all the points
        pointCounts = dict()
        for point in points:
            point = tuple(point)
            pointCounts[point] = pointCounts.get(point, 0) + 1
            # infinite # of lines go through duplicate points
            maxPointsTracker = max(maxPointsTracker, pointCounts[point])

        # mapping of (Line) -> (Count of All Points on Line)
        lineCounts = dict()
        # mapping of (Line) -> (Index of the Unique Points on line)
        lineToPointIndexMap = dict()

        uniquePoints = list(pointCounts.keys())
        for ind, point in enumerate(uniquePoints):

            pointsToVisit = [True] * ind
            for prevInd, prevVisitedPoint in enumerate(uniquePoints[:ind]):
                line = self.calculateLine(point, prevVisitedPoint)

                # skip points that are covered by previously visited lines
                if not pointsToVisit[prevInd]: continue

                # set to skip all subsequent points that belong to same line
                for pointInd in lineToPointIndexMap.get(line, []): pointsToVisit[pointInd] = False
                if line in lineToPointIndexMap:
                    lineToPointIndexMap[line].append(ind)
                else:
                    lineToPointIndexMap[line] = [prevInd, ind]

                lineCounts[line] = lineCounts.get(line, pointCounts[prevVisitedPoint]) + pointCounts[point]
                maxPointsTracker = max(maxPointsTracker, lineCounts[line])

        return maxPointsTracker

    def calculateSlope(
            self,
            point1: Tuple[int],
            point2: Tuple[int]) -> RationalNum:
        """
        Represent slopes with fractions or with math.inf when delta_x is 0
        """
        delta_x, delta_y = point1[0] - point2[0], point1[1] - point2[1]
        return math.inf if (delta_x == 0) else Fraction(delta_y, delta_x)

    def calculateIntercept(
            self,
            point: Tuple[int],
            slope: RationalNum) -> Union[Tuple[Fraction]]:
        """
        If the line intersects y-intercept at one point then return the y-intercept.
        If the line intersects the y-intercept infinite number of times then return Origin (0, 0)
        If the line never intersects the y-intersect then return the x-intercept
        """
        if slope == math.inf:
            return (point[0], 0)
        else:
            return (Fraction(0), point[1] - slope * point[0])

    def calculateLine(self, point1: Tuple[int], point2: Tuple[int]) -> Line:
        slope = self.calculateSlope(point1, point2)
        return Line(self.calculateIntercept(point1, slope), slope)


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.maxPoints([[0,-1],[0,3],[0,-4],[0,-2],[0,-4],[0,0],[0,0],[0,1],[0,-2],[0,4]])     # noqa
    )

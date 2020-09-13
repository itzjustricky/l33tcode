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

        # mapping of (Point) -> (List of Lines)
        pointToLineMap = dict()
        # mapping of (Line) -> (List of indices of points that exist in the line)
        lineToPointIndexMap = dict()
        # track the counts of all the points
        pointsTracker = dict()

        for ind, point in enumerate(points):
            point = tuple(point)

            # handle duplicate points
            if point in pointsTracker:
                # have to update all the lines associated with the point
                for line in pointToLineMap.get(point, []):
                    lineToPointIndexMap[line].append(ind)
                    maxPointsTracker = max(maxPointsTracker, len(lineToPointIndexMap[line]))

                pointsTracker[point].append(ind)
                # infinite # of lines go through duplicate points
                maxPointsTracker = max(maxPointsTracker, len(pointsTracker[point]))

                # no need to to continue to loop below as any possible lines
                # with this duplicate point are already created
                continue

            # from here, all points encountered should be from the currently interated point
            pointsToVisit = [True] * ind
            for prevInd, prevVisitedPoint in enumerate(points[:ind]):
                prevVisitedPoint = tuple(prevVisitedPoint)

                if not pointsToVisit[prevInd]:
                    continue

                line = self.calculateLine(point, prevVisitedPoint)
                # found a new line connecting 2 points
                if line not in lineToPointIndexMap:
                    # if point comes up several times then
                    lineToPointIndexMap[line] = pointsTracker[prevVisitedPoint] + [ind]

                    # update mapping of point to line
                    # it only matters to update the first point even if it is duplicated
                    # because all subsequent duplicated points will be skipped
                    pointToLineMap.setdefault(prevVisitedPoint, []).append(line)
                    pointToLineMap.setdefault(point, []).append(line)
                # formed line was previously encountered
                else:
                    # skip all subsequent points that are a part of this line
                    for pointInd in lineToPointIndexMap[line]: pointsToVisit[pointInd] = False
                    # include current index in line -> point map
                    lineToPointIndexMap[line].append(ind)
                    # include the line for the current point
                    # NOTE: this should only be encountered one time per unique line
                    #   because we are skipping all points on this line from here
                    pointToLineMap.setdefault(point, []).append(line)

                # skip all possible duplicate points
                for pointInd in pointsTracker[prevVisitedPoint]:
                    pointsToVisit[pointInd] = False

                # pointsVisited.add(prevInd)
                maxPointsTracker = max(maxPointsTracker, len(lineToPointIndexMap[line]))

            pointsTracker.setdefault(point, []).append(ind)

        return maxPointsTracker

    def calculateSlope(
            self,
            point1: Tuple[int],
            point2: Tuple[int]) -> Union[Fraction, int]:
        """
        Represent slopes with fractions or with math.inf when delta_x is 0
        """
        delta_x, delta_y = point1[0] - point2[0], point1[1] - point2[1]
        return math.inf if (delta_x == 0) else Fraction(delta_y, delta_x)

    def calculateIntercept(
            self,
            point: Tuple[int],
            slope: Union[Fraction, int]) -> Union[Tuple[Fraction]]:
        """
        If the line intersects y-intercept at one point then return the y-intercept.
        If the line intersects the y-intercept infinite number of times then return Origin (0, 0)
        If the line never intersects the y-intersect then return the x-intercept
        """
        if slope == math.inf:
            if point[0] == 0: return (0, 0)
            else:
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

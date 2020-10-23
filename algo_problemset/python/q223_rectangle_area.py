from typing import Tuple


Point = Tuple[int, int]


class Rectangle:
    __slots__ = ["bLeftCorner", "tRightCorner"]

    def __init__(self, bLeftCorner: Point, tRightCorner: Point):
        self.bLeftCorner = bLeftCorner
        self.tRightCorner = tRightCorner

    def height(self) -> Tuple[Point, Point]:
        return self.tRightCorner[1] - self.bLeftCorner[1]

    def width(self) -> Tuple[Point, Point]:
        return self.tRightCorner[0] - self.bLeftCorner[0]


def overlappingXRange(rect1: Rectangle, rect2: Rectangle) -> Tuple[int, int]:
    """ Find the region for which the 2 rectangles overlap """
    return (
        min(rect1.tRightCorner[0], rect2.bLeftCorner[0]),
        min(rect1.tRightCorner[0], rect2.tRightCorner[0]))


def yValueForOverlapRange(rect1: Rectangle, rect2: Rectangle):
    # set rect1 to be the rectangle that starts lower
    if rect1.bLeftCorner[1] > rect2.bLeftCorner[1]:
        rect1, rect2 = rect2, rect1

    # 1st rectangle's y-range completely encompasses the 2nd one's y-range
    if rect1.tRightCorner[1] > rect2.tRightCorner[1]:
        return rect1.tRightCorner[1] - rect1.bLeftCorner[1]
    # 1st rectangle's y-range ends before start of 2nd one's y-range
    elif rect1.tRightCorner[1] <= rect2.bLeftCorner[1]:
        return (rect1.tRightCorner[1] - rect1.bLeftCorner[1]) + \
            (rect2.tRightCorner[1] - rect2.bLeftCorner[1])
    # there is overlap between the 2
    else:
        return rect2.tRightCorner[1] - rect1.bLeftCorner[1]


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        rect1 = Rectangle((A, B), (C, D))
        rect2 = Rectangle((E, F), (G, H))

        # set rect1 to be the rectangle that starts more to the left
        if rect1.bLeftCorner[0] > rect2.bLeftCorner[0]:
            rect1, rect2 = rect2, rect1

        # find the x-range over which the 2 rectangles overlap
        overlap = overlappingXRange(rect1, rect2)

        area = 0
        # take approach of 'integrating' over x-axis

        # first add in the area only coming from 1st rectangle with no overlap
        area += (overlap[0] - rect1.bLeftCorner[0]) * rect1.height()

        # calculate the area for the area which the rectangles have an overlapping x-range
        #   if there is no overlap, then overlap will be of size 0
        area += (overlap[1] - overlap[0]) * yValueForOverlapRange(rect1, rect2)

        # it is possible the 2nd rectangle still has area left after overlap
        area += (rect2.tRightCorner[0] - max(rect2.bLeftCorner[0], overlap[1])) * rect2.height()
        # it is possible the 1st rectangle still has area left after overlap
        area += (rect1.tRightCorner[0] - overlap[1]) * rect1.height()

        return area

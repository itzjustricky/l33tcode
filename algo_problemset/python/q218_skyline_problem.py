import math
import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        def updateFromPQueue(newBuilding: List[int]) -> list:
            nonlocal frontHeight
            nonlocal frontEnd
            nonlocal buildingTailPQueue

            skyLine = list()
            if len(buildingTailPQueue) == 0: return skyLine

            building = buildingTailPQueue.top()

            while (not buildingTailPQueue.empty()) and (frontEnd <= newBuilding[0]):
                # note the building held at front is always tallest
                if building[1] <= frontEnd:
                    buildingTailPQueue.pop()
                    building = buildingTailPQueue.top()
                else:   # end of top of priority queue is ahead of frontEnd
                    skyLine.append((frontEnd, building[2]))
                    frontEnd, frontHeight = building[1], building[2]

                    # only pop from priority queue if the
                    # building ends before the start of current building
                    if building[1] <= newBuilding[0]:
                        buildingTailPQueue.pop()
                        building = buildingTailPQueue.top()

            if buildingTailPQueue.empty() and (frontEnd < newBuilding[0]):
                skyLine.append((frontEnd, 0))
                frontEnd, frontHeight = newBuilding[0], 0

            return skyLine

        # keep priority queue of past buildings based on building height
        buildingTailPQueue = BuildingPQueue()
        frontHeight, frontEnd = 0, None

        skyLine = list()
        for building in buildings:
            start, end, height = building

            skyLine.extend(updateFromPQueue(building))

            if height > frontHeight:
                # if the start matches the last key point then should replace it
                if (len(skyLine) > 0) and (start == skyLine[-1][0]):
                    skyLine.pop()

                skyLine.append((start, height))
                frontHeight, frontEnd = height, end
            # if height is the same then just update the frontEnd
            elif height == frontHeight:
                frontEnd = end

            buildingTailPQueue.add(building)

        skyLine.extend(updateFromPQueue([math.inf, math.inf, 0]))

        return skyLine


class BuildingPQueue:
    """ Keep priority queue of buildings based on building end """

    def __init__(self):
        self.heapList = list()

    def add(self, building: List[int]):
        heapq.heappush(self.heapList, BuildingHeapNode(building))

    def pop(self):
        return heapq.heappop(self.heapList).building

    def top(self):
        if len(self.heapList) == 0: return None
        return self.heapList[0].building

    def __len__(self):
        return len(self.heapList)

    def empty(self):
        return len(self.heapList) == 0


class BuildingHeapNode():
    """ Use this so buildings can be stored in a heap with the end being height """

    def __init__(self, building: List[int]):
        self.building = building

    def __eq__(self, other):
        return self.building[2] == other.building[2]

    def __lt__(self, other):
        # need to negate so that it is max heap
        return -self.building[2] < -other.building[2]

    def __repr__(self):
        return str(self.building)


if __name__ == "__main__":
    print(Solution().getSkyline(
        [[1,2,1],[1,2,2],[1,2,3]]      # noqa
    ))

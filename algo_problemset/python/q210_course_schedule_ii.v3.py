from typing import List
from typing import Dict

from collections import deque
from collections import defaultdict


class Solution:

    # solve this problem with Kahn's algorithm
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        # represent the implicit graph with indegree count and
        # dict with key per node on all outgoing nodes
        graph, indegreeCounts = defaultdict(list), dict()
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegreeCounts[dest] = indegreeCounts.get(dest, 0) + 1

        orderedCourses = list()
        # get the current courses with no prereqs
        noPreReqCourses = deque(
            ind for ind in range(n)
            if indegreeCounts.get(ind, 0) == 0)

        while len(noPreReqCourses) > 0:
            courseId = noPreReqCourses.pop()
            orderedCourses.append(courseId)

            # empty out the out going courses
            for outCourseId in graph[courseId]:
                indegreeCounts[outCourseId] -= 1

                if indegreeCounts[outCourseId] == 0:
                    noPreReqCourses.append(outCourseId)
            graph[courseId] = []

        # if there are still edges then there is a cycle
        if hasEdges(graph):
            return []

        return orderedCourses


def hasEdges(graph: Dict[int, List[int]]) -> bool:
    return any(len(outgoingNodes) > 0 for outgoingNodes in graph.values())

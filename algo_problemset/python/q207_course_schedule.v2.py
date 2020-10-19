from typing import List

from collections import defaultdict
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        indegreeCounts = {ind: 0 for ind in range(numCourses)}
        # create the graph repr. <source> -> List[<destination>]
        for dest, source in prerequisites:
            graph[source].append(dest)
            indegreeCounts[dest] = indegreeCounts.get(dest, 0) + 1

        noPreReqCourses = deque()
        for courseId, indegree in indegreeCounts.items():
            if indegree == 0:
                noPreReqCourses.append(courseId)

        while len(noPreReqCourses) > 0:
            visitingCourseId = noPreReqCourses.pop()

            # delete all outgoing edges
            for dest in graph[visitingCourseId]:
                indegreeCounts[dest] -= 1
                if indegreeCounts[dest] == 0:
                    noPreReqCourses.append(dest)
            graph[visitingCourseId] = []

        # if there are any edges left
        if any(val > 0 for val in indegreeCounts.values()):
            return False
        else:
            return True


print(
    Solution().canFinish(2, [[1,0]])  # noqa
)

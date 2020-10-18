from collections import deque
from collections import defaultdict

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # graph represented by dict from source -> [destinations]
        self.graph = defaultdict(list)
        for dest, src in prerequisites:
            self.graph[src].append(dest)

        self.orderedCourses = deque()
        self.visiting, self.visited = set(), set()

        for ind in range(numCourses):
            # if False is returned, means there is a cycle
            if self.dfs(ind) is False:
                return []

        return list(self.orderedCourses)

    def dfs(self, courseId: int):
        if courseId in self.visited: return True
        if courseId in self.visiting: return False

        self.visiting.add(courseId)

        for outCourseId in self.graph[courseId]:
            if self.dfs(outCourseId) is False:
                return False

        # done visiting
        self.orderedCourses.appendleft(courseId)
        self.visiting.remove(courseId)
        self.visited.add(courseId)
        return True

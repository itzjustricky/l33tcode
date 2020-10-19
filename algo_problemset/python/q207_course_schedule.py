from typing import Dict
from typing import List

from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        # create the graph repr. <source> -> List[<destination>]
        for dest, source in prerequisites:
            graph[source].append(dest)

        self.visiting, self.visited = set(), set()
        for courseId in range(numCourses):
            if (courseId not in self.visited):
                canFinishFlag = self.dfsCanFinish(courseId, graph)
                if not canFinishFlag:
                    return False
        return True

    def dfsCanFinish(self, courseId: int, graph: Dict[int, List[int]]) -> bool:
        """
        Do a depth-first search and return a boolean of
        True, if able to reach a leaf course
        False, if encountering a cycle
        """
        if courseId in self.visited:
            return True
        if courseId in self.visiting:
            return False

        self.visiting.add(courseId)
        for dest in graph.get(courseId, []):
            if not self.dfsCanFinish(dest, graph):
                return False

        self.visiting.remove(courseId)
        self.visited.add(courseId)
        return True

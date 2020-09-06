# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited, graphCopy, nodesToVisit = set(), dict(), {node}

        if node is None: return None

        graphCopy[node.val] = Node(
            node.val,
            [_node.val for _node in node.neighbors])

        # do breadth first search
        while len(nodesToVisit) > 0:
            nextNodesToVisit = set()
            for visitNode in nodesToVisit:
                for neighbor in visitNode.neighbors:
                    if neighbor not in visited:
                        nextNodesToVisit.add(neighbor)
                        visited.add(neighbor)

                        graphCopy[neighbor.val] = Node(
                            neighbor.val,
                            [_node.val for _node in neighbor.neighbors])

            nodesToVisit = nextNodesToVisit

        for visitNode in graphCopy.values():
            visitNode.neighbors = [graphCopy[neighborId] for neighborId in visitNode.neighbors]

        return graphCopy[node.val]

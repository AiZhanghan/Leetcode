import collections


class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        Args:
            numCourses: int
            prerequisites: list[list[int]]
        
        Return:
            list[int]
        """
        in_degrees = [0 for _ in range(numCourses)]
        graph = collections.defaultdict(list)
        for second, first in prerequisites:
            in_degrees[second] += 1
            graph[first].append(second)
        
        res = []
        queue = collections.deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
            
        while queue:
            top = queue.popleft()
            res.append(top)

            for successor in graph[top]:
                in_degrees[successor] -= 1
                if in_degrees[successor] == 0:
                    queue.append(successor)
        
        if len(res) != numCourses:
            return []
        
        return res
        
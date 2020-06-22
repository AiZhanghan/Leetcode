from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """拓扑排序, DFS"""
        self.adjacency = [[] for _ in range(numCourses)]
        self.flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            self.adjacency[pre].append(cur)
        for i in range(numCourses):
            if not self.dfs(i):
                return False
        return True
    
    def dfs(self, i: int) -> bool:
        if self.flags[i] == -1:
            return True
        if self.flags[i] == 1:
            return False
        
        self.flags[i] = 1
        for j in self.adjacency[i]:
            if not self.dfs(j):
                return False
        self.flags[i] = -1
        
        return True


# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         """拓扑排序, BFS"""
#         indegrees = [0 for _ in range(numCourses)]
#         adjacency = [[] for _ in range(numCourses)]
#         queue = deque()

#         for cur, pre in prerequisites:
#             indegrees[cur] += 1
#             adjacency[pre].append(cur)
        
#         for i in range(len(indegrees)):
#             if not indegrees[i]:
#                 queue.append(i)
        
#         while queue:
#             pre = queue.popleft()
#             numCourses -= 1
#             for cur in adjacency[pre]:
#                 indegrees[cur] -= 1
#                 if not indegrees[cur]:
#                     queue.append(cur)
        
#         return not numCourses


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print(Solution().canFinish(numCourses, prerequisites))
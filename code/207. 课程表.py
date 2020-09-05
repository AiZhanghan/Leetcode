import collections 


# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         """拓扑排序, DFS"""
#         self.adjacency = [[] for _ in range(numCourses)]
#         self.flags = [0 for _ in range(numCourses)]
#         for cur, pre in prerequisites:
#             self.adjacency[pre].append(cur)
#         for i in range(numCourses):
#             if not self.dfs(i):
#                 return False
#         return True
    
#     def dfs(self, i: int) -> bool:
#         if self.flags[i] == -1:
#             return True
#         if self.flags[i] == 1:
#             return False
        
#         self.flags[i] = 1
#         for j in self.adjacency[i]:
#             if not self.dfs(j):
#                 return False
#         self.flags[i] = -1
        
#         return True


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        Args:
            numCourses: int
            prerequisites: list[list[int]]
        
        Return:
            bool
        """
        in_degree = [0 for _ in range(numCourses)]
        graph = collections.defaultdict(list)
        
        for cur, pre in prerequisites:
            in_degree[cur] += 1
            graph[pre].append(cur)
        
        queue = collections.deque()
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in graph[pre]:
                in_degree[cur] -= 1
                if in_degree[cur] == 0:
                    queue.append(cur)
        
        return numCourses == 0


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print(Solution().canFinish(numCourses, prerequisites))
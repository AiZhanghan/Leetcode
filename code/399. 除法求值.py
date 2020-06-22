from collections import deque


class Solution:
    def calcEquation(self, equations, values, queries):
        """BFS
        
        Args:
            equations: list[list[str]]
            values = list[float]
            queries = list[list[str]]
        
        Return:
            list[float]
        """
        self.adj = {}
        for (p, q), v in zip(equations, values):
            if p not in self.adj:
                self.adj[p] = set()
            self.adj[p].add((q, v))
            if q not in self.adj:
                self.adj[q] = set()
            self.adj[q].add((p, 1 / v))
        
        res = []
        for p, q in queries:
            res.append(self.bfs(p, q))
        return res

    def bfs(self, p, q):
        if p not in self.adj or q not in self.adj:
            return -1
        if p == q:
            return 1
        queue = deque()
        visited = set()
        queue.append((p, 1))
        while queue:
            node, value = queue.popleft()
            visited.add(node)
            if node == q:
                return value
            for _next, weight in self.adj[node]:
                if _next not in visited:
                    queue.append((_next, value * weight)) 
        return -1


# class Solution:
#     def calcEquation(self, equations, values, queries):
#         """DFS

#         Args:
#             equations: list[list[str]]
#             values = list[float]
#             queries = list[list[str]]
        
#         Return:
#             list[float]
#         """
#         self.res = [1 for _ in range(len(queries))]
#         self.adj = {}
#         for (p, q), v in zip(equations, values):
#             if p not in self.adj:
#                 self.adj[p] = set()
#             self.adj[p].add((q, v))
#             if q not in self.adj:
#                 self.adj[q] = set()
#             self.adj[q].add((p, 1 / v))
        
#         for i, (p, q) in enumerate(queries):
#             if p not in self.adj:
#                 self.res[i] = -1
#                 continue

#             if not self.dfs(p, q, i, set()):
#                 self.res[i] = -1
        
#         return self.res
    
#     def dfs(self, p, q, i, visited):
#         """
#         Args:
#             p: str
#             q: str
#             i: int
#             visited: set(str)
        
#         Return:
#             bool
#         """
#         if p in visited:
#             return False
#         if p == q:
#             return True
        
#         visited.add(p)
#         for node, weight in self.adj[p]:
#             self.res[i] *= weight
#             if self.dfs(node, q, i, visited):
#                 return True
#             self.res[i] /= weight
        
#         return False
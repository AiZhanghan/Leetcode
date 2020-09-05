import collections


class UnionFind:
    def __init__(self, n):
        """
        Args:
            n: int
        """
        self.roots = [i for i in range(n)]
    
    def find(self, i):
        """
        Args:
            i: int
        
        Return:
            int
        """
        if self.roots[i] == i:
            return i
        self.roots[i] = self.find(self.roots[i])
        return self.roots[i]
    
    def is_connected(self, p, q):
        """
        Args:
            p: int
            q: int
        
        Return:
            bool
        """
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """
        Args:
            p: int
            q: int
        """
        self.roots[self.find(p)] = self.find(q)


class Solution:
    def isBipartite(self, graph):
        """
        Args:
            graph: list[list[int]]
        
        Return:
            bool
        """
        uf = UnionFind(len(graph))
        for v in range(len(graph)):
            for w in graph[v]:
                if uf.is_connected(v, w):
                    return False
                uf.union(graph[v][0], w) 
        return True


# class Solution:
#     def isBipartite(self, graph):
#         """
#         Args:
#             graph: list[list[int]]
        
#         Return:
#             bool
#         """
#         visited = [0 for _ in range(len(graph))]
#         for v in range(len(graph)):
#             if visited[v] == 0 and not self.bfs(graph, v, 1, visited):
#                 return False
        
#         return True

#     def bfs(self, graph, v, color, visited):
#         """
#         Args:
#             graph: list[list[int]]
#             v: int
#             color: int
#             visited: list[int]
        
#         Return:
#             bool
#         """
#         if visited[v] != 0:
#             return visited[v] == color
        
#         visited[v] = color
#         queue = collections.deque()
#         queue.append(v)

#         while queue:
#             v = queue.popleft()
#             for w in graph[v]:
#                 if visited[w] == visited[v]:
#                     return False
#                 if visited[w] == 0:
#                     visited[w] = -visited[v]
#                     queue.append(w)
#         return True


# class Solution:
#     def isBipartite(self, graph):
#         """
#         Args:
#             graph: list[list[int]]
        
#         Return:
#             bool
#         """
#         visited = [0 for _ in range(len(graph))]
#         for i in range(len(graph)):
#             if visited[i] == 0 and not self.dfs(graph, i, 1, visited):
#                 return False
        
#         return True
    
#     def dfs(self, graph, v, color, visited):
#         """
#         Args:
#             graph: list[list[int]]
#             v: int
#             color: int
#             visited: list[int]
        
#         Return:
#             bool
#         """
#         if visited[v] != 0:
#             return visited[v] == color
        
#         visited[v] = color
#         for w in graph[v]:
#             if not self.dfs(graph, w, -color, visited):
#                 return False
        
#         return True

from typing import List
from collections import deque


class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        
        if self.rank[p_root] > self.rank[q_root]:
            self.parent[q_root] = p_root
        elif self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        else:
            self.parent[q_root] = p_root
            self.rank[p_root] += 1
        
        self.count -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        
        directions = [(1, 0), (0, 1)]

        dummy_node = row * col
        uf = UnionFind(dummy_node + 1)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "0":
                    uf.union(self.get_index(i, j), dummy_node)
                if grid[i][j] == "1":
                    for direction in directions:
                        new_x = i + direction[0]
                        new_y = j + direction[1]
                        if new_x < row and new_y < col \
                            and grid[new_x][new_y] == "1":
                            uf.union(self.get_index(new_x, new_y), 
                                     self.get_index(i, j))
        return uf.count - 1

    def get_index(self, x, y):
        return x * len(self.grid[0]) + y


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         """BFS"""
#         directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#         m = len(grid)
#         if m == 0:
#             return 0
#         n = len(grid[0])
#         marked = [[False for _ in range(n)] for _ in range(m)]
#         count = 0
#         for i in range(m):
#             for j in range(n):
#                 if not marked[i][j] and grid[i][j] == "1":
#                     count += 1
#                     queue = deque()
#                     while queue:
#                         cur_x, cur_y = queue.popleft()
#                         for direction in directions:
#                             new_i = cur_x + direction[0]
#                             new_j = cur_y + direction[1]
#                             if 0 <= new_i < m and 0 <= new_j < n \
#                                 and not marked[i][j] and grid[i][j] == "1":
#                                 queue.append((new_i, new_j))
#                                 marked[new_i][new_j] = True
#         return count


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         """DFS"""
#         if not grid:
#             return 0
        
#         self.grid = grid
#         self.visited = [[False for _ in range(len(grid[0]))] 
#                                for _ in range(len(grid))]
#         res = 0

#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if self.grid[i][j] == "1" and not self.visited[i][j]:
#                     res += 1            
#                     self.dfs(i, j)
        
#         return res

#     def dfs(self, row: int, col: int):
#         if row < 0 or row >= len(self.grid) \
#             or col < 0 or col >= len(self.grid[0]) \
#             or self.visited[row][col] \
#             or self.grid[row][col] == "0":
#             return
        
#         self.visited[row][col] = True
#         self.dfs(row + 1, col)
#         self.dfs(row - 1, col)
#         self.dfs(row, col + 1)
#         self.dfs(row, col - 1)
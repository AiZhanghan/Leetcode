class UnionFind:
    def __init__(self, n):
        """
        Args:
            n: int
        """
        self.roots = [x for x in range(n + 1)]

    def find(self, i):
        """
        Args:
            i: int
        
        Return:
            int
        """
        if self.roots[i] == i:
            return self.roots[i]
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
    def findRedundantConnection(self, edges):
        """
        Args:
            edges: list[list[int]]
        
        Return:
            list[int]
        """
        uf = UnionFind(len(edges))
        for p, q in edges:
            if uf.is_connected(p, q):
                return [p, q]
            uf.union(p, q)
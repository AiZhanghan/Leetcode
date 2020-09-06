class UnionFind:
    def __init__(self, n):
        """
        Args:
            n: int
        """
        self.roots = [x for x in range(n)]
    
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
    def func(self, n, groups):
        """
        Args:
            n: int
            groups: list[list[int]]
        """
        uf = UnionFind(n)
        for group in groups:
            for i in range(1, len(group)):
                uf.union(group[0], group[i])
        
        res = 1
        for i in range(1, n):
            if uf.is_connected(0, i):
                res += 1
        return res


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    groups = []
    for _ in range(m):
        group = list(map(int, input().split()))
        groups.append(group[1:])
    print(Solution().func(n, groups))

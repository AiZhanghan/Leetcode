class UnionFind:
    def __init__(self, n):
        """
        Args:
            n: int
        """
        self.roots = [x for x in range(n)]
        self.sz = [1 for _ in range(n)]
    
    def find(self, i):
        """
        Args:
            i: int
        
        Return:
            int
        """
        while i != self.roots[i]:
            i = self.roots[i]
        return i
    
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
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        # 将小树的根节点连接到大树的根节点
        if self.sz[p_root] < self.sz[q_root]:
            self.roots[p_root] = self.roots[q_root]
            self.sz[q_root] += self.sz[p_root]
        else:
            self.roots[q_root] = self.roots[p_root]
            self.sz[p_root] += self.sz[q_root]
    

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

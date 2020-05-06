class Solution:
    def makeConnected(self, n, connections):
        # 网线数量
        line_num = len(connections)
        # 网线数量不足
        if line_num < n - 1:
            return -1
        # 建立并查集
        union_find_set = UnionFindSet(n)
        for connection in connections:
            root1 = union_find_set.find(connection[0])
            root2 = union_find_set.find(connection[1])
            if root1 != root2:
                union_find_set.union(root1, root2)
        # 确定连通分量数目
        counter = 0
        for i in range(n):
            if union_find_set.s[i] < 0:
                counter += 1
        
        return counter - 1
    

class UnionFindSet:
    def __init__(self, max_size):
        self.s = [-1 for _ in range(max_size)]

    def find(self, x):
        """查找元素，返回集合根节点"""
        if self.s[x] < 0:
            return x
        else:
            # 路径压缩
            self.s[x] = self.find(self.s[x])
            return self.s[x]

    def union(self, root1, root2):
        if self.s[root2] < self.s[root1]:
            self.s[root2] += self.s[root1]
            self.s[root1] = root2
        else:
            self.s[root1] += self.s[root2]
            self.s[root2] = root1
            
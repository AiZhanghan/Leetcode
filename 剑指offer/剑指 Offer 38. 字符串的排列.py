class Solution:
    def permutation(self, s):
        """
        Args:
            s: str
        
        Return:
            list[str]
        """
        self.c = list(s)
        self.res = []
        self.dfs(0)
        return self.res
    
    def dfs(self, x):
        """
        Args:
            x: int
        """
        if x == len(self.c) - 1:
            self.res.append("".join(self.c))
            return
        
        dic = set()
        for i in range(x, len(self.c)):
            if self.c[i] in dic:
                continue
            dic.add(self.c[i])
            self.c[i], self.c[x] = self.c[x], self.c[i]
            self.dfs(x + 1)
            self.c[i], self.c[x] = self.c[x], self.c[i]


# class Solution:
#     def permutation(self, s):
#         """
#         Args:
#             s: str
        
#         Return:
#             list[str]
#         """
#         self.res = set()
#         self.s = s
#         self.visited = [False for _ in range(len(s))]
#         for i in range(len(s)):
#             self.dfs(i, [])
#         return list(self.res)

#     def dfs(self, index, path):
#         """
#         Args:
#             index: int
#             path: list[str]
#         """
#         self.visited[index] = True
#         path.append(self.s[index])

#         if len(path) == len(self.s):
#             self.res.add("".join(path))
#             self.visited[index] = False
#             path.pop()
#             return
        
#         for i in range(len(self.s)):
#             if not self.visited[i]:
#                 self.dfs(i, path)

#         self.visited[index] = False
#         path.pop()
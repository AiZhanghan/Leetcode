# class Solution:
#     def permutation(self, s):
#         """
#         Args:
#             s: str
        
#         Return:
#             list[str]
#         """
#         self.s = list(s)
#         self.res = []
#         self.dfs(0)
#         return self.res
    
#     def dfs(self, x):
#         """
#         Args:
#             x: int
#         """
#         if x == len(self.s) - 1:
#             self.res.append("".join(self.s))
#             return
#         repeat = set()
#         for i in range(x, len(self.s)):
#             if self.s[i] in repeat:
#                 continue
#             repeat.add(self.s[i])
#             self.s[i], self.s[x] = self.s[x], self.s[i]
#             self.dfs(x + 1)
#             self.s[i], self.s[x] = self.s[x], self.s[i]


class Solution:
    def permutation(self, s):
        """
        Args:
            s: str
        
        Return:
            list[str]
        """
        self.s = s
        self.res = []
        self.visited = [False for _ in range(len(s))]
        self.dfs(0, [])
        return list(self.res)

    def dfs(self, index, path):
        """
        Args:
            index: int
            path: list[str]
        """
        if len(path) == len(self.s):
            # print(path)
            self.res.append("".join(path))
            return
        repeat = set()
        for i in range(len(self.s)):
            if not self.visited[i] and self.s[i] not in repeat:
                repeat.add(self.s[i])
                self.visited[i] = True
                path.append(self.s[i])
                self.dfs(index + 1, path)
                self.visited[i] = False
                path.pop()
        


# if __name__ == "__main__":
#     s = "abc"
#     print(Solution().permutation(s))
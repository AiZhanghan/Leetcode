class Solution:
    def permutation(self, s):
        """
        Args:
            s: str
        Return:
            list[str]
        """
        self.res = []
        self.c = list(s)
        self.dfs(0)
        return self.res

    def dfs(self, x):
        """固定x位
        Args:
            x: int
        """
        if x == len(self.c) - 1:
            self.res.append("".join(self.c))
            return
        visited = set()
        for i in range(x, len(self.c)):
            if self.c[i] in visited:
                continue
            visited.add(self.c[i])
            self.c[x], self.c[i] = self.c[i], self.c[x]
            self.dfs(x + 1)
            self.c[x], self.c[i] = self.c[i], self.c[x]

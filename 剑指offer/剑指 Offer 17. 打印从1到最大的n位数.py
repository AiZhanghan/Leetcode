class Solution:
    def printNumbers(self, n):
        """
        Args:
            n: int
        
        Return:
            list[int]
        """
        self.n = n
        self.num = ["0" for _ in range(n)]
        self.res = []
        self.nine = 0
        self.start = n - 1
        self.dfs(0)
        return self.res
    
    def dfs(self, x):
        """
        Args:
            x: int
        """
        if x == self.n:
            s = "".join(self.num[self.start:])
            if s != "0":
                self.res.append(int(s))
            if self.n - self.start == self.nine:
                self.start -= 1
            return
        for i in range(10):
            if i == 9:
                self.nine += 1
            self.num[x] = str(i)
            self.dfs(x + 1)
        self.nine -= 1


# class Solution:
#     def printNumbers(self, n):
#         """
#         Args:
#             n: int
        
#         Return:
#             list[int]
#         """
#         res = [x for x in range(1, 10 ** n)]
#         return res
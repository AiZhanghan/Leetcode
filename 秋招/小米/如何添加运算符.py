class Solution:
    def func(self, N, M):
        """
        Args:
            N: int
            M: int
        
        Return:
            int
        """
        if N == 0:
            return 0
        self.M = M
        self.nums = [x for x in range(1, N + 1)]
        self.res = 0
        self.dfs(1, [str(self.nums[0])])
        return self.res
    
    def dfs(self, index, path):
        """
        Args:
            index: int
            path: list[str]
        """
        # print(path)
        if index == len(self.nums):
            if self.cal(path) == self.M:
                # print(path)
                self.res += 1
            return
        for op in "+-s":
            if op != "s":
                path.append(op)
                path.append(str(self.nums[index]))
                self.dfs(index + 1, path)
                path.pop()
                path.pop()
            else:
                if path:
                    path[-1] += str(self.nums[index])
                    self.dfs(index + 1, path)
                    path[-1] = path[-1][:-1]
    
    def cal(self, path):
        """
        Args:
            path: list[str]
        
        Return:
            int
        """
        path = "".join(path)
        l = 0
        res = 0
        op = "+"
        for r in range(len(path)):
            if path[r] in "+-":
                if op == "+":
                    res += int(path[l: r])
                elif op == "-":
                    res -= int(path[l: r])
                op = path[r]
                l = r + 1
        if l != len(path):
            if op == "+":
                res += int(path[l:])
            else:
                res -= int(path[l:])
        return res


if __name__ == "__main__":
    # N, M = 7, 0
    N, M = list(map(int, input().split()))
    print(Solution().func(N, M))
    # path = ["1", "+", "2", "3", "-", "5"]
    # print(Solution().cal(path))
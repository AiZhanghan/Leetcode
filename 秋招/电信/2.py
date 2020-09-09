class Solution:
    def func(self):
        """回溯"""
        path = []
        self.dfs(0, path)
    
    def dfs(self, index, path):
        """
        Args:
            index: int
            path: list[str]
        """
        if index == 4:
            if self.helper(path):
                print(" ".join(path))
            return
        
        for x in range(10):
            path.append(str(x))
            self.dfs(index + 1, path)
            path.pop()
    
    def helper(self, path):
        """
        Args:
            path: list[str]
        
        Return:
            bool
        """
        abcd = int("".join(path))
        temp = path[1:] + path[:1]
        bcda = int("".join(temp))
        return abcd + bcda == 8888


if __name__ == "__main__":
    Solution().func()
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """回溯"""
        if not nums:
            return []
        self.res = []
        self.nums = nums
        self.visited = [False for _ in range(len(nums))]
        self.dfs([])
        return self.res
    
    def dfs(self, path: List[int]):
        if len(path) == len(self.nums):
            self.res.append(path[:])
            return
        for i, num in enumerate(self.nums):
            if self.visited[i]:
                continue
            self.visited[i] = True
            path.append(num)
            self.dfs(path)
            path.pop()
            self.visited[i] = False           
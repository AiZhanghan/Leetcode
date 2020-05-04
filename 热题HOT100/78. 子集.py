from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """回溯"""
        nums.sort()
        self.nums = nums
        self.res = []
        self.dfs([], 0)
        return self.res

    def dfs(self, path: List[int], index: int):
        self.res.append(path[:])
        for i in range(index, len(self.nums)):
            path.append(self.nums[i])
            self.dfs(path, i + 1)
            path.pop()

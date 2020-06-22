from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """回溯"""
        if not candidates:
            return []
        self.res = []
        candidates.sort()
        self.candidates = candidates
        self.dfs([], 0, target)
        return self.res
    
    def dfs(self, path: List[int], index: int, target: int):
        if target == 0:
            self.res.append(path[:])
            return
        while index < len(self.candidates):
            residue = target - self.candidates[index]
            if residue < 0:
                break
            path.append(self.candidates[index])
            self.dfs(path, index, residue)
            path.pop()
            index += 1

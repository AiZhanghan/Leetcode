from typing import List
from collections import deque


# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         """回溯"""
#         if not digits:
#             return []
#         self.d = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
#         self.digits = digits
#         self.res = []
#         self.dfs("", 0)
#         return self.res

#     def dfs(self, tmp: str, index: int):
#         if index == len(self.digits):
#             self.res.append(tmp)
#             return
#         c = self.digits[index]
#         letters = self.d[ord(c) - 48]
#         for letter in letters:
#             self.dfs(tmp + letter, index + 1)


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """迭代, 队列"""
        if not digits:
            return []
        dic = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = deque()
        res.append("")
        for digit in digits:
            size = len(res)
            for _ in range(size):
                tmp = res.popleft()
                for char in dic[digit]:
                    res.append(tmp + char)
        return list(res)
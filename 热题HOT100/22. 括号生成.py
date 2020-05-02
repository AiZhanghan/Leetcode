from typing import List

from collections import deque


class Node:
        def __init__(self, path: str, left: int, right: int):
            self.path = path
            self.left = left
            self.right = right


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """广度优先遍历, 队列"""
        res = []
        queue = deque()
        queue.append(Node("", n, n))
        while queue:
            cur_node = queue.popleft()
            if cur_node.left == 0 and cur_node.right == 0:
                res.append(cur_node.path)
            if cur_node.left > 0:
                queue.append(Node(cur_node.path + "(", cur_node.left - 1,
                                  cur_node.right))
            if cur_node.right > 0 and cur_node.right > cur_node.left:
                queue.append(Node(cur_node.path + ")", cur_node.left, 
                                  cur_node.right - 1))
        return res

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         """加法, 回溯"""
#         self.res = []
#         self.n = n
#         self.dfs("", 0, 0)
#         return self.res
    
#     def dfs(self, path, left, right):
#         if left == self.n and right == self.n:
#             self.res.append(path)
#             return
#         if left < self.n:
#             self.dfs(path + "(", left + 1, right)
#         if right < self.n and left > right:
#             self.dfs(path + ")", left, right + 1)


# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         """做减法"""
#         self.res = []
#         self.dfs("", n, n)
#         return self.res
    
#     def dfs(self, path, left, right):
#         if left == 0 and right == 0:
#             self.res.append(path)
#             return
#         if left > 0:
#             self.dfs(path + "(", left - 1, right)
#         if right > 0 and right > left:
#             self.dfs(path + ")", left, right - 1)


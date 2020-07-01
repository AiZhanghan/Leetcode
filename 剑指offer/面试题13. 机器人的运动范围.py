class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        """
        parameter:
            m: int, [1, 100]
            n: int, [1, 100]
            k: int
        return: int
        """
        self.m = m
        self.n = n
        self.k = k
        self.count = 0
        self.visited = set()

        self.dfs(0, 0, 0, 0)
        
        return self.count

    def dfs(self, row, col, row_sum, col_sum):
        """
        parameter:
            row: int
            col: int
            row_sum: int
            col_sum: int
        """
        if not self.pos_available(row, col, row_sum, col_sum) \
            or ((row, col) in self.visited):
            return
        
        self.visited.add((row, col))
        self.count += 1

        self.dfs(row+1, col, row_sum+1 if (row+1)%10 else row_sum-8, col_sum)
        self.dfs(row, col+1, row_sum, col_sum+1 if (col+1)%10 else col_sum-8)

    def pos_available(self, row, col, row_sum, col_sum):
        """
        判断[row, col]位置是否合法
        parameter:
            row: int
            col: int
            row_sum: int
            col_sum: int
        return: bool
        """
        res = False
        if (0 <= row < self.m) and (0 <= col < self.n) and (row_sum + col_sum <= self.k):
                res = True
        return res


# class Solution:
#     def movingCount(self, m: int, n: int, k: int) -> int:
#         """
#         parameter:
#             m: int, [1, 100]
#             n: int, [1, 100]
#             k: int
#         return: int
#         """
#         self.m = m
#         self.n = n
#         self.k = k
#         self.count = 0
#         self.visited = [[False for _ in range(n)] for _ in range(m)]

#         self.dfs(0, 0)
        
#         return self.count

#     def dfs(self, row, col):
#         """
#         parameter:
#             row: int
#             col: int
#         """
#         if not self.pos_available(row, col) or self.visited[row][col]:
#             return
        
#         self.visited[row][col] = True
#         self.count += 1

#         self.dfs(row+1, col)
#         self.dfs(row-1, col)
#         self.dfs(row, col+1)
#         self.dfs(row, col-1)

#     def pos_available(self, row, col):
#         """
#         判断[row, col]位置是否合法
#         parameter:
#             row: int
#             col: int
#         return: int
#         """
#         res = False
#         if (0 <= row < self.m) and (0 <= col < self.n):
#             if self.digit_sum(row) + self.digit_sum(col) <= self.k:
#                 res = True
#         return res

#     def digit_sum(self, num):
#         """
#         各位数之和
#         parameter:
#             num: int, [1, 100]
#         return: int
#         """
#         sum_ = 0
#         while num:
#             sum_ += num % 10
#             num = num // 10
#         return sum_

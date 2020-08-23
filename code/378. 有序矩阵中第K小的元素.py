import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        """
        Args:
            matrix: list[list[int]]
            k: int
        
        Return:
            int
        """
        pq = [(matrix[i][0], i, 0) for i in range(len(matrix))]
        heapq.heapify(pq)

        for _ in range(k - 1):
            _, x, y = heapq.heappop(pq)
            if y < len(matrix) - 1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))
        
        return heapq.heappop(pq)[0]


# class Solution:
#     def kthSmallest(self, matrix, k):
#         """
#         Args:
#             matrix: list[list[int]]
#             k: int
        
#         Return:
#             int
#         """
#         left, right = matrix[0][0], matrix[-1][-1]
#         while left < right:
#             mid = (left + right) // 2
#             if self.counter(matrix, mid) >= k:
#                 right = mid
#             else:
#                 left = mid + 1
#         return left
    
#     def counter(self, matrix, mid):
#         """
#         Args:
#             matrix: list[list[int]]
#             mid: int
        
#         Return:
#             int
#         """
#         i = len(matrix) - 1
#         j = 0
#         count = 0
#         while i >= 0 and j < len(matrix):
#             if matrix[i][j] <= mid:
#                 count += i + 1
#                 j += 1
#             else:
#                 i -= 1
#         return count
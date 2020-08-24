import heapq


class Solution:
    def func(self, matrix, n):
        """
        Args:
            matrix: list[list[int]]
            n: int
        
        Return:
            int
        """
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] -= matrix[i][j - 1]
        
        pq = [(-matrix[i][0], i, 0) for i in range(len(matrix))]
        heapq.heapify(pq)
        res = 0
        for _ in range(n):
            val, x, y = heapq.heappop(pq)
            res -= val
            if y < len(matrix[0]) - 1:
                heapq.heappush(pq, (-matrix[x][y + 1], x, y + 1))
        return res




if __name__ == "__main__":
    m, n = list(map(int, input().split()))
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().split())))
    print(Solution().func(matrix, n))

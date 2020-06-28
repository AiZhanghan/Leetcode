class Solution:
    def spiralOrder(self, matrix):
        """
        Args:
            matrix: list[list[int]]

        Return:
            list[int]
        """
        res = []
        if not matrix:
            return res
        u = 0
        d = len(matrix) - 1
        l = 0
        r = len(matrix[0]) - 1
        while True:
            for i in range(l, r + 1):
                res.append(matrix[u][i])
            u += 1
            if u > d:
                break

            for i in range(u, d + 1):
                res.append(matrix[i][r])
            r -= 1
            if r < l:
                break

            for i in reversed(range(l, r + 1)):
                res.append(matrix[d][i])
            d -= 1
            if d < u:
                break
                
            for i in reversed(range(u, d + 1)):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        
        return res
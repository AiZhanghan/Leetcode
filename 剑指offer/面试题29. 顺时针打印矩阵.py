class Solution:
    def spiralOrder(self, matrix):
        """
        :param matrix: list[list[int]]

        :return: list[int]
        """
        if not matrix:
            return []
        res = []
        l = 0
        r = len(matrix[0]) - 1
        t = 0
        b = len(matrix) - 1

        while True:
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1
            if t > b:
                break

            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                break

            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1
            if t > b:
                break

            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break

        return res

class Solution:
    def generateMatrix(self, n):
        """
        Args:
            n: int
        
        Return:
            list[list[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        u = 0
        d = n - 1
        l = 0
        r = n - 1
        num = 1
        limit = n ** 2
        while num <= limit:
            for i in range(l, r + 1):
                res[u][i] = num
                num += 1
            u += 1

            for i in range(u, d + 1):
                res[i][r] = num
                num += 1
            r -= 1
            
            for i in reversed(range(l, r + 1)):
                res[d][i] = num
                num += 1
            d -= 1
                
            for i in reversed(range(u, d + 1)):
                res[i][l] = num
                num += 1
            l += 1
        
        return res


if __name__ == "__main__":
    n = 3
    print(Solution().generateMatrix(n))
class Solution:
    def isMatch(self, s, p):
        """
        Args:
            s: str
            p: str
        
        Return:
            bool
        """
        n = len(s)
        m = len(p)
        f = [[False for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(m + 1):
                if j == 0:
                    f[i][j] = i == 0
                else:
                    if p[j - 1] != "*":
                        if i > 0 and (s[i - 1] == p[j - 1] or p[j - 1] == "."):
                            f[i][j] = f[i - 1][j - 1]
                    else:
                        if j >= 2:
                            f[i][j] |= f[i][j - 2]
                        if i >= 1 and j >= 2 and \
                            (s[i - 1] == p[j - 2] or p[j - 2] == "."):
                            f[i][j] |= f[i - 1][j]
        return f[n][m]
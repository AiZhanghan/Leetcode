class Solution:
    def isMatch(self, s, p):
        """
        Args:
            s: str
            p: str
        
        Return:
            bool
        """
        if not s or not p:
            return False
        
        rows = len(s)
        columns = len(p)

        dp = [[False for _ in range(columns + 1)] for _ in range(rows + 1)]
        dp[0][0] = True

        for j in range(1, columns + 1):
            if p[j - 1] == "*" and dp[0][j - 2]:
                dp[0][j] = True
        
        for i in range(1, rows + 1):
            for j in range(1, columns + 1):
                nows = s[i - 1]
                nowp = p[j - 1]
                if nows == nowp:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    if nowp == ".":
                        dp[i][j] = dp[i - 1][j - 1]
                    elif nowp == "*":
                        if j >= 2:
                            nowp_last = p[j - 2]
                            if nowp_last == nows or nowp_last ==".":
                                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                            dp[i][j] = dp[i][j] or dp[i][j - 2]
                    else:
                        dp[i][j] = False
        return dp[rows][columns]
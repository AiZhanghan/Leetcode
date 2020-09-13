class Solution:
    def func(self, s):
        """
        Args:
            s: str
        
        Return:
            int
        """
        dic = {}
        l = 0
        r = 0
        res = 0

        for r in range(len(s)):
            if s[r] in dic and dic[s[r]] >= l:
                l = dic[s[r]] + 1
            dic[s[r]] = r
            res = max(res, r - l + 1)
        
        return res


if __name__ == "__main__":
    s = input()
    # s = "abcdab"
    print(Solution().func(s))
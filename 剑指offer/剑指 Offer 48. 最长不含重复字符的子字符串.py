class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Args:
            s: str
        
        Return:
            int
        """
        res = 0
        dic = {}
        l = 0
        for r in range(len(s)):
            if s[r] in dic and dic[s[r]] >= l:
                l = dic[s[r]] + 1
            dic[s[r]] = r
            res = max(res, r - l + 1)
        return res
        
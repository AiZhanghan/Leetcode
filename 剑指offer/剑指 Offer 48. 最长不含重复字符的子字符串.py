class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Args:
            s: str
        
        Return:
            int
        """
        res = 0
        l = 0
        visited = {}
        for r in range(len(s)):
            if s[r] in visited and visited[s[r]] >= l:
                l = visited[s[r]] + 1
            res = max(res, r - l + 1)
            visited[s[r]] = r
        return res
                
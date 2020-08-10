class Solution:
    def longestSubstring(self, s, k):
        """
        Args:
            s: str
            k: int
        
        Return:
            int
        """
        if len(s) < k:
            return 0
        t = min(set(s), key=s.count)
        if s.count(t) >= k:
            return len(s)
        return max(self.longestSubstring(a, k) for a in s.split(t))
        
class Solution:
    def isIsomorphic(self, s, t):
        """
        Args:
            s: str
            t: str
        
        Return:
            bool
        """
        s2t = {}
        t2s = {}
        for i in range(len(s)):
            if s[i] not in s2t and t[i] not in t2s:
                s2t[s[i]] = t[i]
                t2s[t[i]] = s[i]
            elif s[i] not in s2t or t[i] not in t2s:
                return False
            elif s2t[s[i]] != t[i] or t2s[t[i]] != s[i]:
                return False
        return True


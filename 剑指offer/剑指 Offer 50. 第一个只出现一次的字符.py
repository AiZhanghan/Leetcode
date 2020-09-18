class Solution:
    def firstUniqChar(self, s):
        """
        Args:
            s: str
        
        Return:
            str
        """
        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        
        for c in s:
            if dic[c] == 1:
                return c
        
        return " "
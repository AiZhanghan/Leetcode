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
                dic[c] = False
            else:
                dic[c] = True
        
        for key, value in dic.items():
            if value:
                return key
        
        return " "
class Solution:
    def firstUniqChar(self, s):
        """
        Args:
            s: str
        
        Return:
            str
        """
        # Python3.6之后默认dic为OrderedDict()
        dic = {}
        for char in s:
            if char in dic:
                dic[char] = False
            else:
                dic[char] = True
        for key, value in dic.items():
            if value:
                return key
        return " "
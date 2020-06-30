class Solution:
    def reverseWords(self, s):
        """
        Args:
            s: str
        
        Return:
            str
        """
        res = s.split()
        for i in range(len(res)):
            res[i] = res[i][::-1]
        return " ".join(res)
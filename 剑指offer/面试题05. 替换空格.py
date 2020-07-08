class Solution:    
    def replaceSpace(self, s):
        """
        time: O(N)
        space: O(N)
        
        Args:
            s: str
        
        Return: str
        """
        res = []
        for c in s:
            if c == " ":
                res.append("%20")
            else:
                res.append(c)
        return "".join(res)


# class Solution:    
#     def replaceSpace(self, s):
#         """
#         Args:
#             s: str
        
#         Return: str
#         """
#         return s.replace(" ", "%20")
        
class Solution:
    def reverseWords(self, s):
        """
        Args:
            s: str
        
        Return:
            str
        """
        s = s.strip()
        res = []
        r = len(s)
        for l in range(len(s) - 1, -1, -1):
            if s[l] == " ":
                if r - l - 1 > 0:
                    res.append(s[l + 1: r])
                r = l
        res.append(s[: r])
            
        return " ".join(res)


# class Solution:
#     def reverseWords(self, s):
#         """
#         Args:
#             s: str
        
#         Return:
#             str
#         """
        
#         s_list = s.strip().split(" ")
#         return " ".join([c for c in reversed(s_list) if c])


if __name__ == "__main__":
    s = "a good   example"
    print(Solution().reverseWords(s))
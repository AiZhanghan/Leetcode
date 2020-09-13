class Solution:
    def func(self, s):
        """
        Args:
            s: list[int]
        
        Return:
            int
        """
        res = 0

        for i in range(len(s) + 1):
            temp = self.helper(s, i)
            res = max(res, temp)

        return res
    
    def helper(self, s, left_end):
        """
        Args:
            s: str
            left_end: int
        
        Return:
            int
        """
        res = len(s)
        for i in range(len(s)):
            if s[i] == "0" and i < left_end:
                res += 1
            elif s[i] == "1" and i >= left_end:
                res += 1
        return res
    

if __name__ == "__main__":
    s = input()
    print(Solution().func(s))

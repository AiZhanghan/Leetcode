class Solution:
    def func(self, s):
        """
        Args:
            s: str
        
        Return:
            str
        """
        res = ""
        valid = set("5678")
        # [l, r)
        l = 0
        for r in range(len(s)):
            if s[r] not in valid:
                l = r + 1
            elif r - l + 1 >= 2 and r - l + 1 > len(res):
                res = s[l: r + 1]
        return res


if __name__ == "__main__":
    s = input()
    # s = "1234567890477485158"
    print(Solution().func(s))
                


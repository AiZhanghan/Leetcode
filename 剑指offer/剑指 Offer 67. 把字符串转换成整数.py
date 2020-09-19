class Solution:
    def strToInt(self, s):
        """
        Args:
            s: str
        
        Return:
            int
        """
        INT_MAX = 2 ** 31 - 1
        INT_MIN = - (2 ** 31)
        s = s.lstrip()
        if not s:
            return 0
        
        is_positive = True
        index = 0
        if s[0] == "-":
            is_positive = False
            index += 1
        elif s[0] == "+":
            index += 1
        
        res = 0
        while index < len(s) and s[index].isdigit():
            res = res * 10 + ord(s[index]) - ord("0")
            index += 1
        
        if not is_positive:
            res *= -1
        
        if res > INT_MAX:
            return INT_MAX
        elif res < INT_MIN:
            return INT_MIN
        else:
            return res


if __name__ == "__main__":
    s = "  -42"
    print(Solution().strToInt(s))
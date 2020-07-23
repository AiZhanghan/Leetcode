class Solution:
    def strToInt(self, s):
        """
        Args:
            s: str

        Return:
            int
        """
        s = s.lstrip()
        if not s:
            return 0
        
        INT_MIN = - 2 ** 31
        INT_MAX = - INT_MIN - 1
        bound = (INT_MAX + 1)// 10

        i = 0
        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1
        
        num = 0
        while i < len(s) and "0" <= s[i] <= "9":
            if num > bound or num == bound and s[i] > "7":
                return INT_MAX if sign == 1 else INT_MIN
            num = num * 10 + ord(s[i]) - ord("0")
            i += 1
        
        return num * sign


# class Solution:
#     def strToInt(self, s):
#         """
#         Args:
#             s: str

#         Return:
#             int
#         """
#         s = s.lstrip()
#         if not s:
#             return 0
        
#         INT_MIN = - 2 ** 31
#         INT_MAX = - INT_MIN - 1

#         i = 0
#         positive = True
#         if s[i] == "+":
#             i += 1
#         elif s[i] == "-":
#             positive = False
#             i += 1
        
#         num = 0
#         while i < len(s) and s[i].isdigit():
#             num = num * 10 + ord(s[i]) - ord("0")
#             i += 1
        
#         if not positive:
#             num *= -1
        
#         if num > INT_MAX:
#             return INT_MAX
#         elif num < INT_MIN:
#             return INT_MIN
#         else:
#             return num

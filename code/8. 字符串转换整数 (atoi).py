class Solution:
    def myAtoi(self, s):
        """
        Args:
            s: str
        
        Return:
            int
        """
        MIN_INT = - 2 ** 31
        MAX_INT = 2 ** 31 - 1

        index = 0
        while index < len(s) and s[index] == " ":
            index += 1
        
        if index == len(s):
            return 0

        negative = False
        if s[index] == "-":
            negative = True
            index += 1
        elif s[index] == "+":
            index += 1
        elif not s[index].isdigit():
            return 0
        
        res = 0
        while index < len(s) and s[index].isdigit():
            digit = ord(s[index]) - ord("0")
            if res * 10 + digit > MAX_INT:
                return MIN_INT if  negative else MAX_INT
            res = res * 10 + digit
            index += 1
        return -res if negative else res



# class Solution:
#     def myAtoi(self, s):
#         """
#         Args:
#             s: str
        
#         Return:
#             int
#         """
#         s = s.lstrip()
#         if not s:
#             return 0
#         digits = "0123456789"
#         sign = 1
#         if s[0] == "+":
#             s = s[1:]
#         elif s[0] == "-":
#             sign = -1
#             s = s[1:]
#         elif s[0] in digits:
#             pass
#         else:
#             return 0
        
#         has_invalid = False
#         for i, c in enumerate(s):
#             if c not in digits:
#                 has_invalid = True
#                 break
        
#         if has_invalid:
#             s = s[: i]
#         res = (int(s) if s else 0) * sign
#         if res < - 2 ** 31:
#             res = - 2 ** 31
#         if res > 2 ** 31 - 1:
#             res = 2 ** 31 - 1
#         return res
class Solution:
    def strToInt(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        res = 0
        i = 1
        is_positive = True
        max_int = 2 ** 31 - 1
        if s[0] == "-":
            is_positive = False
        elif s[0] != "+":
            i = 0
        for c in s[i: ]:
            if not "0" <= c <= "9":
                break
            res = 10 * res + ord(c) - ord("0")
            if res > max_int:
                return max_int if is_positive else -max_int - 1
        return res if is_positive else -res



# class Solution:
#     def strToInt(self, s: str) -> int:
#         nums = {str(x): x for x in range(10)}
#         # 跳过开头无用空格
#         i = 0
#         while i < len(s) and s[i] == " ":
#             i += 1
#         # 字符串为空或字符串仅包含空白字符
#         if i == len(s):
#             return 0
#         int_max = 2 ** 31 - 1
#         int_min = -(2 ** 31)
#         if s[i] == "+":
#             res = 0
#             i += 1
#             while res < int_max and i < len(s) and s[i] in nums:
#                 res = res * 10 + nums[s[i]]
#                 i += 1
#             return res if res < int_max else int_max
#         elif s[i] == "-":
#             res = 0
#             i += 1
#             while res < -int_min and i < len(s) and s[i] in nums:
#                 res = res * 10 + nums[s[i]]
#                 i += 1
#             return -res if -res > int_min else int_min
#         elif s[i] in nums:
#             res = 0
#             while res < int_max and i < len(s) and s[i] in nums:
#                 res = res * 10 + nums[s[i]]
#                 i += 1
#             return res if res < int_max else int_max
#         else:
#             return 0

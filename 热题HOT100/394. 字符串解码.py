class Solution:
    def decodeString(self, s):
        """
        Args:
            s: str
        
        Return:
            str
        """
        return self.dfs(s, 0)
    
    def dfs(self, s, i):
        """
        Args:
            s: str
            i: int
        
        Return:
            str or (int, str)
        """
        res = ""
        multi = 0
        while i < len(s):
            if "0" <= s[i] <= "9":
                multi = multi * 10 + int(s[i])
            elif s[i] == "[":
                i, tmp = self.dfs(s, i + 1)
                res += multi * tmp
                multi = 0
            elif s[i] == "]":
                return i, res
            else:
                res += s[i]
            i += 1
        return res
        

# class Solution:
#     def decodeString(self, s):
#         """
#         Args:
#             s: str
        
#         Return:
#             str
#         """
#         res = ""
#         multi = 0
#         stack = []
#         for c in s:
#             if c == "[":
#                 stack.append((multi, res))
#                 multi = 0
#                 res = ""
#             elif c == "]":
#                 cur_multi, last_res = stack.pop()
#                 res = last_res + cur_multi * res
#             elif "0" <= c <= "9":
#                 multi = multi * 10 + int(c)
#             else:
#                 res += c
#         return res


# class Solution:
#     def decodeString(self, s):
#         """
#         Args:
#             s: str
        
#         Return:
#             str
#         """
#         num_str = [str(x) for x in range(10)]
#         res = ""
#         lb_count = 0
#         stack = []
        
#         for char in s:
#             if char in num_str:
#                 stack.append(char)
#             elif char == "[":
#                 lb_count += 1
#                 stack.append(char)
#             elif char == "]":
#                 temp = ""
#                 while stack[-1] != "[":
#                     temp += stack.pop()
#                 temp = temp[::-1]
#                 stack.pop()
#                 lb_count -= 1
#                 num = ""
#                 while stack and stack[-1] in num_str:
#                     num += stack.pop()
#                 num = int(num[::-1])
#                 temp *= num
#                 if lb_count:
#                     for i in range(len(temp)):
#                         stack.append(temp[i])
#                 else:
#                     res += temp
#             else:
#                 if lb_count:
#                     stack.append(char)
#                 else:
#                     res += char
#         return res


if __name__ == "__main__":
    s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    print(Solution().decodeString(s))
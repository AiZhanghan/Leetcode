class Solution:
    def isValid(self, s: str) -> bool:
        """栈"""
        dic = {
            "(": ")",
            "[": "]", 
            "{": "}",
            "?": "?"
        }
        stack = ["?"]
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1
        

# class Solution:
#     def isValid(self, s: str) -> bool:
#         """栈"""
#         left_brackets = {"(", "[", "{"}
#         stack = []
#         res = True
#         for bracket in s:
#             if bracket in left_brackets:
#                 stack.append(bracket)
#             elif bracket == ")":
#                 if not stack or stack.pop() != "(":
#                     res = False
#                     break
#             elif bracket == "]":
#                 if not stack or stack.pop() != "[":
#                     res = False
#                     break
#             else:
#                 if not stack or stack.pop() != "{":
#                     res = False
#                     break
#         return res and not stack
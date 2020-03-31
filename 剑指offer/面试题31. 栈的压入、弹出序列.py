class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :param pushed: list[int]
        :param popped: list[int]

        :return: bool
        """
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return not stack


# class Solution:
#     def validateStackSequences(self, pushed, popped):
#         """
#         :param pushed: list[int]
#         :param popped: list[int]

#         :return: bool
#         """
#         i = 0
#         j = 0
#         stack = []
#         while j < len(popped):
#             if not stack or stack[-1] != popped[j]:
#                 if i < len(pushed):
#                     stack.append(pushed[i])
#                     i += 1
#                 else:
#                     break
#             else:
#                 stack.pop()
#                 j += 1
#         res = True
#         if stack:
#             res = False
#         return res

class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        Args:
            pushed: list[int]
            poped: list[int]
        
        Return:
            bool
        """
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
            
        return not stack
        

# class Solution:
#     def validateStackSequences(self, pushed, popped):
#         """
#         Args:
#             pushed: list[int]
#             poped: list[int]
        
#         Return:
#             bool
#         """
#         stack = []
#         push_index = 0
#         pop_index = 0
        
#         while pop_index < len(popped):
#             if not stack or stack[-1] != popped[pop_index]:
#                 if push_index < len(pushed):
#                     stack.append(pushed[push_index])
#                     push_index += 1
#                 else:
#                     return False
#             else:
#                 stack.pop()
#                 pop_index += 1
        
#         return True
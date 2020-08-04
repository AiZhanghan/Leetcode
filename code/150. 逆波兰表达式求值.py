class Solution:
    def evalRPN(self, tokens):
        """
        Args:
            tokens: list[str]
        
        Return:
            int
        """
        stack = [0 for _ in range(len(tokens) // 2 + 1)]
        index = 0
        for x in tokens:
            if x == "+":
                stack[index - 2] += stack[index - 1]
                index -= 1
            elif x == "-":
                stack[index - 2] -= stack[index - 1]
                index -= 1
            elif x == "*":
                stack[index - 2] *= stack[index - 1]
                index -= 1
            elif x == "/":
                stack[index - 2] = int(stack[index - 2] / stack[index - 1])
                index -= 1
            else:
                stack[index] = int(x)
                index += 1
        return stack[0]


# class Solution:
#     def evalRPN(self, tokens):
#         """
#         Args:
#             tokens: list[str]
        
#         Return:
#             int
#         """
#         stack = []
#         operators = set(["+", "-", "*", "/"])
#         for x in tokens:
#             if x not in operators:
#                 stack.append(int(x))
#             else:
#                 val2 = stack.pop()
#                 val1 = stack.pop()
#                 if x == "+":
#                     stack.append(val1 + val2)
#                 elif x == "-":
#                     stack.append(val1 - val2)
#                 elif x == "*":
#                     stack.append(val1 * val2)
#                 elif x == "/":
#                     stack.append(int(val1 / val2))
#         return stack[0]


if __name__ == "__main__":
    token = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(Solution().evalRPN(token))
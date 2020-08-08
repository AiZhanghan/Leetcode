class Solution:
    def calculate(self, s):
        """
        Args:
            s: str

        Return:
            int
        """
        stack = []
        num = 0
        sign = "+"
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            if (not c.isdigit() and c != " ") or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    pre = stack.pop()
                    stack.append(pre * num)
                elif sign == "/":
                    pre = stack.pop()
                    stack.append(int(pre / num))
                sign = c
                num = 0
        
        res = 0
        while stack:
            res += stack.pop()

        return res
                    
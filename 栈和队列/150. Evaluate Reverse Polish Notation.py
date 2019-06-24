# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:52:18 2019

@author: Administrator
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = '+-*/'
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(self.operate(operand1, operand2, tokens[i]))
        
        return int(stack[0])
        
    def operate(self, operand_1, operand_2, operator):
        if operator == '+':
            return int(operand_1) + int(operand_2)
        elif operator == '-':
            return int(operand_1) - int(operand_2)
        elif operator == '*':
            return int(operand_1) * int(operand_2)
        else:
            return int(int(operand_1) / int(operand_2))
        
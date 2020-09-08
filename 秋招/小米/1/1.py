# #!/bin/python
# # -*- coding: utf8 -*-
# import sys
# import os
# import re

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************


def pathInZigZagTree(label):
    """
    Args:
        label: int
    
    Return:
        list[int]
    """
    level = 0
    count = 0
    while label > count:
        level += 1
        count += 2 ** (level - 1)
    res = []
    while level > 0:
        res.append(label)
        index = label2index(level, label)
        parent_index = (index + 1) // 2
        level -= 1
        label = index2label(level, parent_index)
    return res[::-1]

    
def label2index(level, label):
    """
    index 在该层的索引 从1开始

    Args:
        level: int
        label: int
    
    Return:
        int
    """
    if level % 2 == 0:
        return 2 ** level - label
    else:
        return label - 2 ** (level - 1) + 1 


def index2label(level, index):
    """
    index 在该层的索引 从1开始

    Args:
        level: int
        index: int
    
    Return:
        int
    """
    if level % 2 == 0:
        return 2 ** level - index
    else:
        return 2 ** (level - 1) + index - 1

#******************************结束写代码******************************

if __name__ == "__main__":

    _label = int(input())
    # _label = 14

    
    res = pathInZigZagTree(_label)

    for res_cur in res:
        print(str(res_cur))
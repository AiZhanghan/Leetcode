# #!/bin/python
# # -*- coding: utf8 -*-
# import sys
# import os
# import re

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************


def pokersort(pokers):
    dic = {
        "3": 0,
        "4": 1,
        "5": 2,
        "6": 3,
        "7": 4,
        "8": 5,
        "9": 6,
        "10": 7,
        "J": 8,
        "Q": 9,
        "K": 10,
        "A": 11,
        "2": 12,
    }
    # 插入排序
    for i in range(1, len(pokers)):
        j = i
        temp = pokers[j]
        while j > 0 and dic[pokers[j - 1]] > dic[temp]:
            pokers[j] = pokers[j - 1]
            j -= 1
        pokers[j] = temp

    return pokers

#******************************结束写代码******************************

if __name__ == "__main__":
    
    # _pokers_cnt = 0
    # _pokers_cnt = int(input())
    # _pokers = []
    # for _ in range(_pokers_cnt):
    #     _pokers.append(input())
    # _pokers = ["3", "4", "5", "10", "A", "K", "2", "6"]
    _pokers = ["3", "4", "5", "10", "2", "6"]
    res = pokersort(_pokers)

    for res_cur in res:
        print(str(res_cur))


# 10
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# K
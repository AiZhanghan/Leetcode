#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

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
        # "j": 8,
        "Q": 9,
        # "q": 9,
        "K": 10,
        # "k":10,
        "A": 11,
        # "a": 11,
        "2": 12,
    }
    res = sorted(pokers, key= lambda x: dic[x])
    return res

#******************************结束写代码******************************

if __name__ == "__main__":
    
    _pokers_cnt = 0
    _pokers_cnt = int(input())
    _pokers = []
    for _ in range(_pokers_cnt):
        _pokers.append(input())

    res = pokersort(_pokers)

    for res_cur in res:
        print(str(res_cur))
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 22:17:36 2019

@author: Administrator
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Command:
    def __init__(self, s, nested_integer):
        self.s = s
        self.nested_integer = nested_integer

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.res = []
        if not nestedList:
            return 
        
        stack = []
        stack.append(Command('go', nestedList))
        
        while stack:
            command = stack.pop()
            
            if command.s == 'print':
                self.res.append(command.nested_integer.getInteger())
            else:
                for i in range(len(command.nested_integer) - 1, -1, -1):
                    if command.nested_integer[i].isInteger:
                        stack.append(Command('print', command.nested_integer[i]))
                    else:
                        stack.append(Command('go', command.nested_integer[i]))
        

    def next(self):
        """
        :rtype: int
        """
        return self.res.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.res

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())